import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

s = pd.Series([1, 3, 5, np.nan, 6, 8])

print (s)

print ('This is the data output table')


a = np.arange(0, 5, 0.01)

b = np.cos (a)

plt.plot(a,b)
plt.plot (a,a)