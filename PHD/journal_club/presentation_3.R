library(ggplot2)
library(reshape2)
library(tidyverse)

x <- seq(0, 100, 0.1)
y1 <- sin(x)
y2 <- sin(x) * rnorm(100, 1, 0.5)
data <- data.frame(Time = x, Food_value = y1, Motivation = y2) %>%
	gather(key = "variable", value = "value", -Time)
ggplot(data = data, aes(x = Time, y = value)) +
	geom_line(aes(color = variable), alpha = 0.6) + 
	theme_void()
ggsave("fig1.png")
