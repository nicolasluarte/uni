library(tidyverse)
library(randomForest)
setwd('/home/nicoluarte/uni/PHD/stat_course/')
d <- read.csv('mice.csv', header=TRUE) %>% as_tibble()
labs <- read.csv('mice_labels.csv', header = TRUE, sep = ',') %>% select(Behavior)


data <- d %>% mutate(FRAME=str_replace(FRAME_PATH, "^0+(?!_)", "")) %>%
  mutate(FRAME=str_replace(FRAME, "_(.*)", ""))

data <- data %>% bind_cols(labs)
test <- randomForest(as.factor(Behavior) ~ body_x + body_y + head_x + head_y + tail_x + tail_y + ANGLES,
    data = final,
    ntree = 200,
    mtry = 7, 
    importance=TRUE)
test

b.x <- data$body_x
b.y <- data$body_y
a.x <- data$head_x
a.y <- data$head_y
c.x <- data$tail_x
c.y <- data$tail_y

get_angle <- function(a.x, a.y, b.x, b.y, c.x, c.y){
  A <- c(a.x, a.y)
  B <- c(b.x, b.y)
  C <- c(c.x, c.y)
  a <- LearnGeom::Angle(A, B, C)
  return(a)
}
angles <- pmap(list(a.x, a.y, b.x, b.y, c.x, c.y), get_angle) %>% unlist()
final <- data %>% mutate(ANGLES = angles)

p1.x <- data$body_x[1]
p1.y <- data$body_y[1]
p2.x <- data$head_x[1]
p2.y <- data$head_y[1]
p3.x <- data$tail_x[1]
p3.y <- data$tail_y[1]

sum(data$Behavior == 3)
A <- list(c(data$head_x[1], data$head_y[1]))
B <- list(c(data$body_x[1], data$body_y[1]))
C <- list(c(data$tail_x[1], data$tail_y[1]))
LearnGeom::Angle(A[[1]], B[[1]], C[[1]])
