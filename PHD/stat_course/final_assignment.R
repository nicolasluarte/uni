library(lme4)
library(mclust)
library(lubridate)
library(tidymodels)
library(NbClust)
library(ggplot2)
library(tidyverse)
library(caret)
setwd('/home/nicoluarte/uni/PHD/stat_course')
rats <- list.files(pattern = "rat[0-9].csv") %>% 
	map_df(~read_csv(.))
labs <- list.files(pattern = "ratlabs[0-9].csv") %>%
	map_df(~read.csv(.))
dat <- bind_cols(rats, labs)
dat$rat <- as.factor(dat$rat)

# merge factor levels
dat$Behavior <- as.factor(dat$Behavior)
levels(dat$Behavior) <- c("0", "1", "1", "1", "0", "0", "0")

# add features
dat <- dat %>%
	group_by(rat) %>%
	mutate(lag1_x = scale(lag(body_x, k=1))) %>%
	mutate(lag1_y = scale(lag(body_y, k=1))) %>%
	mutate(distance = scale(sqrt((lag1_x + lag1_y)))) %>%
	mutate(speed = scale(sqrt((lag1_x + lag1_y))/ 0.5)) %>%
	mutate(rollspeed = scale(zoo::rollmean(sqrt((lag1_x + lag1_y))/ 0.5, 30, fill=NA))) %>%
	ungroup() %>%
	drop_na()
# scale all the variables
dat <- dat %>% mutate_if(is.numeric, scale)

# path plot
plot.data <- dat
plot.data %>% 
	ggplot(aes(x=body_x, y=body_y, )) +
	geom_path(aes(color = Frames)) + facet_wrap(~rat) + 
	theme_bw() +
	labs(x = "Body 'x' position", y = "Body 'y' position")
ggsave("path.png")

# distance plot
plot.data %>% 
	ggplot(aes(x=Frames, y=distance)) +
	geom_smooth() + facet_wrap(~rat) + 
	theme_bw() +
	labs(x = "Frames", y = "Distance traveled in pixels arbitrary units")
ggsave("distance.png")

# speed plot
plot.data %>% 
	ggplot(aes(x=Frames, y=rollspeed)) +
	geom_line() + facet_wrap(~rat) + 
	theme_bw() +
	labs(x = "Frames", y = "Rolling average of speed over 1 second")
ggsave("speed.png")

# distance hist plot
plot.data %>% 
	ggplot(aes(x=distance, fill=rat)) +
	geom_density(alpha=0.5) +
	theme_bw() +
	labs(x = "Distances", y = "Density")
ggsave("density.png")

# distance hist plot
plot.data %>% 
	ggplot(aes(x=Behavior, fill=rat)) +
	geom_bar() +
	theme_bw() +
	labs(x = "Behavior label", y = "Count")
ggsave("behavior.png")

# k-means cluster distribution
kdist <- data.frame(clusters = unlist(k.clust), rat = dat %>% unnest(data) %>% select(rat))
kdist %>% 
	ggplot(aes(x=clusters)) +
	geom_histogram() +
	theme_bw() +
	facet_wrap(~rat) +
	labs(x = "Cluster index", y = "Count over all rats")
ggsave("kdist.png")

# gmm cluster distribution
gmmdist <- data.frame(clusters = unlist(gmm.clust), rat = dat %>% unnest(data) %>% select(rat))
gmmdist %>% 
	ggplot(aes(x=clusters)) +
	geom_histogram() +
	theme_bw() +
	facet_wrap(~rat) +
	labs(x = "Cluster index", y = "Count over all rats")
ggsave("gmmdist.png")

# k-means considering rat (groups) and optimal center size, same for gmm
dat <- dat %>%
	group_by(rat) %>%
	nest() %>%
	mutate(k.mdl = map(data, ~kmeans(.x %>%
					 select(body_x, body_y, head_x, head_y, tail_x, tail_y, distance, rollspeed) %>%
					 drop_na(),
				 which.max(fviz_nbclust(.x %>% select(body_x, body_y, head_x, head_y, tail_x, tail_y, distance, rollspeed), kmeans, method="silhouette")$data$y)))) %>%
	mutate(gmm = map(data, ~ mclust::Mclust(.x %>% select(body_x, body_y, head_x, head_y, tail_x, tail_y, distance, rollspeed) %>% drop_na()))) %>%
	ungroup()
# bind centers and GMM classifications
gmm.clust <- 1:dim(dat)[1] %>% map(., function(x) dat$gmm[[x]]$classification)
k.clust <- 1:dim(dat)[1] %>% map(., function(x) dat$k.mdl[[x]]$cluster)
dat <- dat %>%
	mutate(data = map2(data, k.clust, ~bind_cols(.x, .cluster = .y))) %>%
	mutate(data = map2(data, gmm.clust, ~bind_cols(.x, .gmmcluster = .y)))

# correlation
1:4 %>% map(~chisq.test(dat$data[[.x]]$.cluster, dat$data[[.x]]$Behavior))
1:4 %>% map(~chisq.test(dat$data[[.x]]$.gmmcluster, dat$data[[.x]]$Behavior))
1:4 %>% map(~rcompanion::cramerV(dat$data[[.x]]$.cluster, dat$data[[.x]]$Behavior, bias.correct=TRUE))
1:4 %>% map(~rcompanion::cramerV(dat$data[[.x]]$.gmmcluster, dat$data[[.x]]$Behavior, bias.correct=TRUE))

# knn models
ctrl <- trainControl(method="repeatedcv",
		     repeats = 3)
knn.mdl <- function(df) {
	train(Behavior ~ rollspeed * .gmmcluster,
				 data = df,
				 method = "knn",
				 trControl = ctrl,
				 preProcess = c("center","scale"),
				 tuneLength = 20)
}
dat <- dat %>% mutate(knn = map(data, knn.mdl))

ctrl2 <- trainControl(method="repeatedcv",
		     repeats = 3,
			sampling="down")
knn.mdl2 <- function(df) {
	train(Behavior ~ rollspeed * .gmmcluster,
				 data = df,
				 method = "knn",
				 trControl = ctrl2,
				 preProcess = c("center","scale"),
				 tuneLength = 20)
}
dat <- dat %>% mutate(knn.2 = map(data, knn.mdl2))

global.knn <- knn.mdl2(dat %>% unnest(data))

# plot by movement by cluster
mov.cluster <- dat %>% unnest(data)
mov.cluster %>% 
	ggplot(aes(x=scale(body_x), y=scale(body_y), color=as.factor(.cluster))) +
	geom_path() + facet_wrap(~rat) + theme_bw() + labs(x = "X position", y = "Y position")
ggsave("kmeans.png")

mov.cluster %>% 
	ggplot(aes(x=scale(body_x), y=scale(body_y), color=as.factor(.gmmcluster))) +
	geom_path() + facet_wrap(~rat) + theme_bw() + labs(x = "X position", y = "Y position")
ggsave("gmm.png")

