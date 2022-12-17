import numpy as np 
import matplotlib.pyplot as plt 
from astropy.io import fits
from matplotlib.colors import LogNorm
import mgefit
from mgefit.find_galaxy import find_galaxy
from mgefit.mge_fit_1d import mge_fit_1d
from mgefit.sectors_photometry import sectors_photometry
from mgefit.mge_fit_sectors import mge_fit_sectors
from mgefit.mge_print_contours import mge_print_contours
from mgefit.mge_fit_sectors_twist import mge_fit_sectors_twist
from mgefit.sectors_photometry_twist import sectors_photometry_twist
from mgefit.mge_print_contours_twist import mge_print_contours_twist


file =('/home/sourave/6galaxies/AGC6438/AGC6438.fits')
hdu = fits.open(file)
img = hdu[0].data
img -= 0.003 # Noise subtraction 
scale = 0.3957 #in pixels
sigma = 1.3 #
#plt.imshow(img,norm = LogNorm(vmin=0.1,vmax=1))
#mask = dist_circle(1350,990,img.shape)>250
ngauss = 11

f = find_galaxy(img,plot=1,nblob=1,fraction=0.1)

plt.pause(1)
plt.clf()

s = sectors_photometry(img, f.eps, f.theta, f.xpeak, f.ypeak,n_sectors=7,plot=1)

plt.pause(1)
plt.clf()

m = mge_fit_sectors(s.radius, s.angle, s.counts, f.eps, ngauss=ngauss, plot=1,scale=scale,sigmapsf=sigma) 

plt.pause(1)
plt.clf()

mge_print_contours(img, f.theta, f.xpeak, f.ypeak, m.sol,scale=scale,sigmapsf=sigma)

plt.figure(1)
plt.clf()

n = 30
img = img[f.xpeak-n:f.xpeak+n, f.ypeak-n:f.ypeak+n]
xc, yc = n - f.xpeak + f.xmed, n - f.ypeak+ f.ymed

mge_print_contours(img, f.theta, xc, yc, m.sol,scale=scale,sigmapsf=sigma)

plt.pause(1)
plt.clf()
