library(easyPubMed)
library(rentrez)
library(tidyverse)
pmids <- c(15987666,23078951)
articles <- read.csv("/home/nicoluarte/uni/PHD/papers/intermittent_food_review/articles_selected.csv")
rec <- parse_pubmed_xml(entrez_fetch(articles$pubmed.id,
                                     db="pubmed",
                                     parsed=TRUE,
                                     rettype="xml"))

df <- rec %>% map_chr(function(x){
  X <- unlist(x$doi)
}) %>% as.data.frame()

colnames(df) <- c("doi")
write_csv(df, "/home/nicoluarte/uni/PHD/papers/intermittent_food_review/doi.csv")
