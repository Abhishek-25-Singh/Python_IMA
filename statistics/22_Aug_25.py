# Skewness
# Skewness is a statistical measure that describes the symmetry or asymmetry in the distribution of data.
# If a dataset follows a Normal Distribution (bell-shaped curve), it is perfectly symmetrical, and skewness is 0.
# When the data deviates from normality, skewness measures the degree and direction of asymmetry.

#🔑 Key Points About Skewness (before Python use)
# 1. Meaning of Skewness
# 2. Type of Data Required
# 3. Sample Size
# 4. Outliers Effect
# 5.Graph vs. Formula
# 6.Python Functions
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = [10, 12, 12, 13, 12, 11, 15, 20, 25]

# Using Pandas
print("Skewness(pandas) :",pd.Series(data).skew())
# Using Scipy
print("Skewness(scipy) :",stats.skew(data))

print("Scipy skewness (bias=True):", stats.skew(data, bias=True))
print("Scipy skewness (bias=False):", stats.skew(data, bias=False))
