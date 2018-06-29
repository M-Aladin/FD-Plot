'''

data.py
-------

Dataset has been loaded and  shape checked to be (6382*59) The first coeficient is omited because it's always 1
Then Enter card number from input.dat file from 0 to 6381
Reshape is made to the array to be (Coefs*4) that are Calculate elliptical Fourier descriptors
Then we plot the dynamometer using pyefd.py

'''

import numpy as np
import pyefd

# load data
x = np.loadtxt("input.dat", delimiter = ' ')
# shape checked to be (6382*59)
print(x.shape)
# Enter card number from input.dat file from 0 to 6381
cardno=4000
# The first coeficient is added
coefs = np.append(1,x[cardno,:])
# Reshape is made to the array
coefs = coefs.reshape(-1,4)
# plot the dynamometer
pyefd.plot_efd(coefs, image=None, n=400)