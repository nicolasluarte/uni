library(caret)
library(tidymodels)
library(factoextra)
library(NbClust)
library(ggplot2)
library(tidyverse)
setwd('/home/nicoluarte/uni/PHD/stat_course')
rats <- list.files(pattern = "rat[0-9].csv") %>% 
	map_df(~read_csv(.))
labs <- list.files(pattern = "ratlabs[0-9].csv") %>%
	map_df(~read.csv(.))
dat <- bind_cols(rats, labs)
dat$rat <- as.factor(dat$rat)
dat <- dat %>% drop_na()

# merge factor levels
dat$Behavior <- as.factor(dat$Behavior)
levels(dat$Behavior) <- c("0", "1", "1", "1", "0", "0", "0")

# optimal clusters
opt.k <- dat %>% group_by(rat) %>%
	select(body_x, body_y) %>%
	group_map(~ which.max(fviz_nbclust(.x, kmeans, method="silhouette")$data$y)) %>% unlist()
group.n <- dat %>% group_by(rat) %>% summarise(n = n()) %>% select(n)
aux <- map2(unlist(opt.k), unlist(group.n), ~ rep(.x, .y)) %>% unlist()
dat <- dat %>% mutate(opt.k = aux)

# add features
dat <- dat %>%
	group_by(rat) %>%
	mutate(lag1_x = lag(body_x, k=1)) %>%
	mutate(lag1_y = lag(body_y, k=1))

# k-means considering rat (groups) and optimal center size
dat <- dat %>%
	group_by(rat) %>%
	nest() %>%
	mutate(k.mdl = map(data, ~kmeans(.x %>% select(body_x, body_y), which.max(fviz_nbclust(.x %>% select(body_x, body_y), kmeans, method="silhouette")$data$y)))) %>%
	ungroup()
k.clust <- 1:dim(dat)[1] %>% map(., function(x) dat$k.mdl[[x]]$cluster) %>% unlist()
dat <- dat %>%
	unnest(c(data)) %>%
	mutate(.cluster = k.clust)

# fit knn to each rat and report cross validated accuracy
ctrl <- trainControl(method="repeatedcv",
		     repeats=5,
		     savePredictions="final",
			sampling="down")
dat <- dat %>%
	group_by(rat) %>%
	nest() %>%
	mutate(cv.knn = map(data, function(df) train(Behavior ~ as.factor(.cluster) + lag1_x + lag1_y,
							 data = df,
							 method = "knn",
							 na.action = na.omit,
							 trControl = ctrl,
							 tuneLength = 10))) %>%
	mutate(cv.glm = map(data, function(df) train(Behavior ~ as.factor(.cluster) + lag1_x + lag1_y,
							 data = df,
							 na.action = na.omit,
							 method = "glm",
							 family="binomial",
							 trControl = ctrl))) %>%
	mutate(cv.knn.acc = map_dbl(cv.knn, function(x) max(x$results["Accuracy"]))) %>%
	mutate(cv.glm.acc = map_dbl(cv.glm, function(x) max(x$results["Accuracy"])))
summary(dat$cv.glm[[1]])
dat$cv.knn
dat

# plot by movement by cluster
mov.cluster <- dat %>% unnest(data)
mov.cluster %>% 
	ggplot(aes(x=body_x, y=body_y, color=as.factor(.cluster))) +
	geom_path() + facet_wrap(~rat)
mov.cluster %>% ggplot(aes(.cluster, ..count..)) + geom_bar(aes(fill=Behavior), position="dodge")

# global model
global.dat <- dat %>% unnest(data)
k.folds = 3
folds <- groupKFold(global.dat$rat, k = k.folds) 
global.control <- trainControl(
                        method="repeatedcv", 
                        number=k.folds, 
                        repeats=3,
			preProcOptions=c("center", "scale"),
			sampling="down",
                        index=folds)
global.mdl1 <- train(Behavior ~ as.factor(.cluster) + lag1_x + lag1_y,
							 data = global.dat,
							 method = "knn",
							 na.action = na.omit,
							 trControl = global.control,
							 tuneLength = 10)
global.mdl2 <- train(Behavior ~ as.factor(.cluster) + lag1_x + lag1_y,
							 data = global.dat,
							 method = "rf",
							 metric = "Accuracy",
							 na.action = na.omit,
							 trControl = global.control,
							 tuneLength = 4)
