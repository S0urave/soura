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
import pandas as pd
file = ('/home/sourave/6galaxies/AGC191707/1917_masked.fits')
hdu = fits.open(file)
img = hdu[0].data
df=pd.DataFrame(img)
df = df.replace(np.nan,0, regex=True)
img = df.to_numpy()
img -= 0.013
f=find_galaxy(img,plot=1,nblob=1)
scale= 0.3957 
plt.pause(1)
plt.clf()
ngauss = 11 

s = sectors_photometry(img, f.eps, f.theta, f.xpeak, f.ypeak,n_sectors=7,plot=1)
    
plt.pause(1)
plt.clf()

m = mge_fit_sectors(s.radius, s.angle, s.counts, f.eps, ngauss=ngauss, plot=1,scale=scale,sigmapsf=sigmapsf) 
plt.pause(1)
plt.clf()

plt.clf()

n = 50
img = img[f.xpeak-n:f.xpeak+n, f.ypeak-n:f.ypeak+n]
xc, yc = n - f.xpeak + f.xmed, n - f.ypeak+ f.ymed
mge_print_contours(img, f.theta, xc, yc, m.sol,binning = 5,scale=scale,sigmapsf=sigmapsf)


plt.pause(1)
plt.clf()
