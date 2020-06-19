from scipy import stats
import math
from metalog import metalog
import numpy as np
import matplotlib.pyplot as plt
import time
'''
Get distribution from percentiles

First, choose a distribution family

2-parameter distributions
	normal
	log-normal
	beta

meta-logistic distribution.

If you provide more than two percentiles for a 2-parameter distribution.
least squares will be used for fitting.
'''

# family can be 'normal', 'lognormal', 'beta', 'metalog'
family = 'metalog'

# a list of (p,x) tuples, where P(X<x)=p
percentiles = [(0.2,8),(0.4,16),(0.6,20),(0.8,22)]

term = len(percentiles)
metalog_obj = metalog.fit (
	x = [tuple[1] for tuple in percentiles],
	probs =[tuple[0] for tuple in percentiles],
	boundedness = 'u',
	term_limit = term)

for x in metalog_obj:
	print(metalog_obj[x])


domain_to_plot = np.linspace(0,100,50)
pdf = metalog.d(m=metalog_obj,term=term,q=domain_to_plot)

cdf = metalog.p(m=metalog_obj,term=term,q=domain_to_plot)



'''
Get percentiles from distribution

Choose a distribution family and provide its parameters
(I can reuse code from bayes-continuous for this)
'''