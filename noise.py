#!/usr/bin/env python

#Importing Required Liberaries 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import astropy
import scipy 
from scipy.optimize import curve_fit
from astropy.io import fits
from os import path
import sys
#-------------------------------------------------------------------------------------------------------------------

#First Method:- The Fitting Method 

#-------------------------------------------------------------------------------------------------------------------

file = ('/home/sourave/Downloads/Project/NGC7800_sdss.fits') #file directory
hdu = fits.open(file) # Opening the Fits File
img = hdu[0].data # Reading first header of Fits file (which contains pixel values in terms of a 2D array)

#---------------------------------------------------------------------------------------------------------------------
# Only pickup points less than 0.2

wr = np.where(img < 0.2) # picking less than 0.2 data greater than 0.2 doesn't considered as noise
 
img2 = img[wr] # A flat 1D array as output containing 

pts = plt.hist(img2, bins=30, histtype='step', color='b', lw=2) #gives 2D tuple or list as output 
plt.axvline(x=0.0)
#----------------------------------------------------------------------------------------------------------------------
peaks = pts[0] # peakes of Histograms (y-axis)
edges = pts[1] # edges of peakes or bin cordinates (x-axis)

''' A Loop to find Mean point of each peak '''
'''-------------------------------------------------------------------------------------------------------------------'''

centres=list() # creating an empty list 
for i in range(len(peaks)):
	centre = (edges[i]+edges[i+1])/2
	centres.append(centre)
plt.plot(centres,peaks)  
plt.show()
'''-------------------------------------------------------------------------------------------------------------------'''

def gauss(x,H, A, x0, sigma):
    return   H+ A * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))
fitting_params,cov_matrix = scipy.optimize.curve_fit(gauss,centres,peaks) 
print(fitting_params,cov_matrix)
y_output = gauss(np.array(centres),H=fitting_params[0],A = fitting_params[1],x0=fitting_params[2],sigma=fitting_params[3])
plt.plot(centres,peaks,'.')
plt.plot(centres,y_output)
plt.show()


