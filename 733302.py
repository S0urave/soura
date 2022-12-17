import numpy as np 
import matplotlib.pyplot as plt 
from astropy.io import fits
from matplotlib.colors import LogNorm
import mgefit
import pandas as pd
from mgefit.find_galaxy import find_galaxy
from mgefit.mge_fit_1d import mge_fit_1d
from mgefit.sectors_photometry import sectors_photometry
from mgefit.mge_fit_sectors import mge_fit_sectors
from mgefit.mge_print_contours import mge_print_contours
from mgefit.mge_fit_sectors_twist import mge_fit_sectors_twist
from mgefit.sectors_photometry_twist import sectors_photometry_twist
from mgefit.mge_print_contours_twist import mge_print_contours_twist


file = ('/home/sourave/6galaxies/AGC733302/73302_masked.fits')
hdu = fits.open(file)
img = hdu[0].data
df=pd.DataFrame(img)
df = df.replace(np.nan,0, regex=True)
img = df.to_numpy() #converting Nan values to zero,since MGEFit won't work with Nan values
img -=0.023
f=find_galaxy(img,plot=1,nblob=1,fraction = 0.1)
scale=0.3957

plt.pause(1)
plt.clf()
ngauss = 11 
s = sectors_photometry(img, f.eps, f.theta, f.xpeak, f.ypeak,n_sectors=7,plot=1)
    
plt.pause(1)
plt.clf()

m = mge_fit_sectors(s.radius, s.angle, s.counts, f.eps, ngauss=ngauss, plot=1,scale=scale) 
plt.pause(1)
plt.clf()
n = 30
img = img[f.xpeak-n:f.xpeak+n, f.ypeak-n:f.ypeak+n]
xc, yc = n - f.xpeak + f.xmed, n - f.ypeak+ f.ymed
mge_print_contours(img, f.theta, xc, yc, m.sol,scale=scale,sigmapsf=sigmapsf)
plt.pause(1)
plt.clf()
