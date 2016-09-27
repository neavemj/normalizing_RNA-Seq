#!/usr/bin/env python

# check different normalization methods for miRNA counts
# Matthew J. Neave 21.09.16

import sys  # carp.miRNA.counts
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

# get counts as pandas dataframe

counts = pd.read_table(sys.argv[1], index_col=0)

counts_1 = counts + 1

counts_log = counts_1.apply(np.log)

#sb.boxplot(counts)
sb.boxplot(counts_log)

counts_log.plot(kind="box")

plt.show()

