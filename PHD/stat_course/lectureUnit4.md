# introduction to correlated data

- what's the unit of observation
- independent and correlated observations
- ignoring correlations will cause problems with p-values
- within-cluster, overstimate p-values
- between-cluster, understimate p-values

# what test do I use?

## two-sample t-test

- use pooled unless you have a reason not to
- pooled give a more precise estimate of the standard deviation
- pooled has an extra assumption: variances are equal between two groups
- most statistical programs test for the above assumption
