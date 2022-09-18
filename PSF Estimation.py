#!/usr/bin/env python

import numpy as np
import astropy.io.fits as fits
import os
from astropy.stats import mad_std
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from lmfit.models import GaussianModel
from astropy.modeling import models, fitting

def gaussian(xycoor,x0, y0, sigma, amp):
    '''This Function is the Gaussian Function'''

    x, y = xycoor # x and y taken from fit function.  Stars at 0, increases by 1, goes to length of axis
    A = 1 / (2*sigma**2)
    eq =  amp*np.exp(-A*((x-x0)**2 + (y-y0)**2)) #Gaussian
    return eq


def fit(image):
    med = np.median(image)
    image = image-med

    max_index = np.where(image >= np.max(image))
    x0 = max_index[1] #Middle of X axis
    y0 = max_index[0] #Middle of Y axis
    x = np.arange(0, image.shape[1], 1) #Stars at 0, increases by 1, goes to length of axis
    y = np.arange(0, image.shape[0], 1) #Stars at 0, increases by 1, goes to length of axis
    xx, yy = np.meshgrid(x, y) #creates a grid to plot the function over
    sigma = np.std(image) #The standard dev given in the Gaussian
    amp = np.max(image) #amplitude
    guess = [x0, y0, sigma, amp] #The initial guess for the gaussian fitting

    low = [0,0,0,0] #start of data array
    #Upper Bounds x0: length of x axis, y0: length of y axis, st dev: max value in image, amplitude: 2x the max value
    upper = [image.shape[0], image.shape[1], np.max(image), np.max(image)*2] 
    bounds = [low, upper]

    params, pcov = curve_fit(gaussian, (xx.ravel(), yy.ravel()), image.ravel(),p0 = guess, bounds = bounds) #optimal fit.  Not sure what pcov is. 

    return params


def plotting(image, params):
    fig, ax = plt.subplots()
    ax.imshow(image)
    ax.scatter(params[0], params[1],s = 10, c = 'red', marker = 'x')
    circle = Circle((params[0], params[1]), params[2], facecolor = 'none', edgecolor = 'red', linewidth = 1)

    ax.add_patch(circle)
    plt.show()


med = np.median(img) 
data = img - med


parameters = fit(data)

#generates a gaussian based on the parameters given
plotting(data, parameters)
