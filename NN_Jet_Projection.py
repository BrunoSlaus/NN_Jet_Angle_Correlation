import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

import astropy
from astropy.io import fits
import astropy.units as u



import os
import sys
import subprocess
import json


######################################################
JET_Catalogue_Name = 'RPA_Output_Kartesian.fits'

X_Column_Name    = 'X'
Y_Column_Name    = 'Y'
Z_Column_Name    = 'Z'
RPA_Column_Name  = 'RPA'
######################################################

JET_Catalogue     = fits.open('Input/' + JET_Catalogue_Name)[1].data
X   = JET_Catalogue[X_Column_Name]
Y   = JET_Catalogue[Y_Column_Name]
Z   = JET_Catalogue[Z_Column_Name]
RPA = JET_Catalogue[RPA_Column_Name]

positions = np.column_stack((X, Y, Z))
nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(positions)
distances, indices = nbrs.kneighbors(positions)

print(distances, indices)

projections = []
for index in indices:
    phi1 = RPA[index[0]]
    phi2 = RPA[index[1]]
    projection = np.cos(np.deg2rad(phi1 - phi2))
    projections.append(projection)
    
projections = np.array(projections)


z_vals = np.linspace(-0.999,0.999,10000)
distribution = 2 * (np.pi - np.arccos(z_vals)) / (np.pi**2 * np.sqrt(1 - (z_vals**2) ))

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot()
ax.hist(projections, bins=33, density = 'True', label = r'$ Z = cos(X_1 - X_2) $', color = 'grey')
#ax.hist(projections2, bins=400, density = 'True')
ax.plot(z_vals, distribution, color = 'black', linestyle = '--', label = r'$ \frac{2 \left[ -\arccos{(z)}  +\pi \right]}{\pi^2} \frac{1}{\sqrt{1-z^2}} $')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 1.5)
ax.legend(loc="upper left")
ax.set_xlabel('Z')
ax.set_ylabel('N')


# Show plot
plt.savefig('Output_Plots/Test.png', dpi = 300)
plt.close()











