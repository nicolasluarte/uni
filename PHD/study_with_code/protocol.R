pacman::p_load(googledrive, ggplot2, tidyverse, ggrepel, pheatmap, reshape2, manipulate)

workbooks <- drive_find()
print(workbooks)
data <- drive_get(as_id('1GNAltxDkmVb4owjR2g01LWf9V1pBcdrleYrwyAzVTVs'))
drive_download(data, type="csv", overwrite = TRUE)
df <- read.csv('Protocols.csv', header=TRUE)
weights <- rnorm(1 * dim(data)[1], 100, 100)	
data <- df %>% mutate(vol=as.numeric(factor(VOLUMEN, levels=c("BAJO", "MEDIO", "ALTO"))),
		int=as.numeric(factor(INTENSIDAD, levels=c("BAJO", "MEDIO", "ALTO"))))
data <- data %>% bind_cols(weights)

ggplot(data, aes(x=vol, y=int, color=PROTOCOLO, label=PROTOCOLO)) +
	geom_point(alpha=0.3) +
	geom_text_repel() +
	theme(legend.position = "none")


mat <- matrix(0, 3, 3) + 1
meltMat <- melt(mat)
head(meltMat)
ggplot(data=meltMat, aes(x=Var2, y=Var1)) +
	geom_raster(aes(fill=value))

gaussianMat <- matrix(rnorm(dim(data)[1] * dim(data)[2], mean=5, sd=1), dim(data)[1], dim(data)[2])

exploration <- function(x, extra){
  g <- melt(matrix(rnorm(dim(x)[1] * dim(x)[2], mean=5, sd=10), dim(x)[1], dim(x)[2]))
  f <- melt(x)
  f$value <- g$value * f$value
  p <- ggplot(data=f, aes(x=Var2, y=Var1)) +
  	geom_point(aes(size=value)) +
    theme(legend.position = "none")
  print(extra)
  return(p)
}

for(i in 1:10) {
  plot(exploration(mat, 1))
  Sys.sleep(1)
}
  
dst <- dist(data[, c(1, 4, 5)], )
dst <- data.matrix(dst)

dim <- ncol(dst)
par(mar=c(12,12,0,0))
image(1:dim, 1:dim, dst, axes = FALSE, xlab="", ylab="")

axis(1, 1:dim, data[, c(1)], cex.axis = 0.5, las=3)
axis(2, 1:dim, data[, c(1)], cex.axis = 0.5, las=1)

text(expand.grid(1:dim, 1:dim), sprintf("%0.1f", dst), cex=0.6)
