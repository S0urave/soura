# Multi-Gaussian Expansion (MGE) for Galaxy Modeling

The Multi-Gaussian Expansion (MGE) approach, introduced by Cappellari & Emsellem (2002) [1], is a powerful method for modeling the surface brightness of galaxies. It represents galaxy images as a sequence of 2D Gaussian functions, offering several advantages, including the ability to account for convolution effects (such as seeing or Point Spread Function) and deprojection (to obtain the intrinsic star luminosity density from recorded galaxy photometry) in a straightforward and efficient manner.

## Introduction

The MGE parametrization is a valuable tool for accurately describing the surface brightness of multicomponent objects with realistic details. It has been widely used for modeling galaxies, as demonstrated by Emsellem et al. (1994) [2].

## MGE Formulation

Let ($x'$, $y'$, $z'$) be a coordinate system with the center at the galaxy nucleus, where the $z'$ axis points toward the observer. The projected surface brightness in MGE form can be expressed as:

$$\sum_{}^{}(R',\theta') = \sum_{j=1}^{N}\frac{L_j}{2\pi \sigma_j'^{2}}\exp{\Bigg[-\frac{1}{2\sigma_j'^{2}}\Bigg(x'_j{^2}+\frac{y'_j{^2}}{q'_j{^2}}\Bigg)\Bigg]}$$
Where:

$N$ is the number of Gaussian components adopted.
$L_j$ is the total luminosity of the j-th Gaussian.
$0 \leq q_j ′ \leq 1$ is the observed axial ratio.
$\sigma_j$ is the dispersion along the major axis.
$\psi_j$ is the position angle (PA), measured counterclockwise from the $y'$ axis to the major axis of the Gaussian.
In the oblate axisymmetric case ($p = 1$), when an inclination $i > 0$ (for $i = 0$, the deprojection is degenerate) is assumed for the galaxy ($i = 90$ corresponds to edge-on), the axial ratio $q$ can be calculated as:

$q^2 = \frac{q'^2 - \cos^2i}{\sin^2i}$


In the prolate axisymmetric case ($p = q$), the axial ratio $q$ is calculated as:
$q^2 = \frac{\sin^2i}{1/q'^2 - \cos^2i}$


## References

- Cappellari, M., & Emsellem, E. (2002). Parametric Recovery of Line-of-Sight Velocity Distributions from Absorption-Line Spectra of Galaxies Using a Library of Stellar Templates. *Monthly Notices of the Royal Astronomical Society*, 333(2), 400. [Link](https://doi.org/10.1046/j.1365-8711.2002.05412.x)
- Emsellem, E., et al. (1994). Multi-component models for the analysis of spectral lines in composite stellar spectra. I. The problem of template mismatch and biases in decomposition of stellar spectra. *Monthly Notices of the Royal Astronomical Society*, 270(3), 605. [Link](https://doi.org/10.1093/mnras/270.3.605)
-Michele Cappellari. Efficient Multi-Gaussian Expansion of galaxies[Link](https://doi.org/10.48550/arXiv.astro-ph/0201430)





 
![AGC733302_dep](https://user-images.githubusercontent.com/100031717/208244447-47ada34e-e825-4eda-8d1f-38b91957e6c1.png)
![AGC733302](https://user-images.githubusercontent.com/100031717/208244449-aeef76f0-ce33-4ebb-965c-ea1f776ed750.png)
![AGC220901_dep](https://user-images.githubusercontent.com/100031717/208244450-28259876-899a-49d8-a482-70c2e129f8cb.png)
![AGC220901](https://user-images.githubusercontent.com/100031717/208244451-61c0c540-289d-4641-a832-dfaf6d42617d.png)
![AGC191707_dep](https://user-images.githubusercontent.com/100031717/208244453-ab1ab2f8-565f-46d2-b95e-2fc07af9fbac.png)
![AGC191707](https://user-images.githubusercontent.com/100031717/208244454-749fd589-ca9f-44a7-bb29-d8ae2bda8539.png)
![AGC9500_dep](https://user-images.githubusercontent.com/100031717/208244455-545ede8f-c7c9-4cdc-9f6d-b058e099483a.png)
![AGC9500](https://user-images.githubusercontent.com/100031717/208244456-45555e70-6de3-4cb2-a01c-0c3de50bbbc6.png)
![AGC7983_dep](https://user-images.githubusercontent.com/100031717/208244458-6feff57c-faf5-4ab7-b952-8797405764ae.png)
![AGC7983](https://user-images.githubusercontent.com/100031717/208244459-aaab99f1-464c-4d90-a316-057205be7541.png)
![AGC6438_dep](https://user-images.githubusercontent.com/100031717/208244460-3ee774ec-1020-4d0f-846e-4a49ff9a337c.png)
![AGC6438](https://user-images.githubusercontent.com/100031717/208244461-fe486667-3705-4704-a615-bd6be707d0bc.png)

