import numpy as np

from scipy import stats

from scipy.stats import norm

# Main methods for continuous RVs
# rvs: Random Variables
# pdf: Probability Density Function
# cdf: Cumulative Distribution Function
# sf: Survival Function (1-CDF)
# ppf: Percent Point Function (Inverse of CDF)
# isf: Inverse Survival Function (Inverse of SF)
# stats: Return mean, variance, (Fisher’s) skew, or (Fisher’s) kurtosis
# moment: non-central moments of the distribution

norm.cdf(-1)

norm.cdf([-1., 0, 1])

print stats.nct.ppf(0.5, 10, 2.5)

stats.t.isf([0.1, 0.05, 0.01], [[10], [11]])

stats.t.isf([0.1, 0.05, 0.01], [10, 11, 12])

from scipy.stats import expon

expon.mean(scale=3.)


np.mean(norm.rvs(5, size=500))





