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














'''


x_vals = np.linspace(0,1,N_grid)
y_vals = np.linspace(0,1,N_grid)
x_rand = np.random.choice(x_vals, N_rand)
y_rand = np.random.choice(y_vals, N_rand)

positions_rand = np.column_stack((x_rand, y_rand))

phi_vals = np.linspace(0,np.pi,N_grid)
phi_rand = np.random.choice(phi_vals, N_rand)

points_rand = np.column_stack((positions_rand, phi_rand))



# Creating plot
fig, (ax1, ax2, ax3) = plt.subplots(1,3)
fig.set_figheight(4)
fig.set_figwidth(14)

ax1.quiver(points_rand[:,0][0:50], points_rand[:,1][0:50], np.cos(points_rand[:,2][0:50]), np.sin(points_rand[:,2][0:50]),
           headlength=0, pivot='middle', scale=10, linewidth=.05, width=.005, headwidth=1)
ax1.set_title('Quiver plot')




rphi1 = np.random.choice(phi_vals, N_rand)
rphi2 = np.random.choice(phi_vals, N_rand)
z1_vals1 = np.linspace(-np.pi,0,10000)
z1_vals2 = np.linspace(0,np.pi,10000)
distribution1 = (1/np.pi**2) * (z1_vals1 + np.pi)
distribution2 = (1/np.pi**2) * (-z1_vals2 + np.pi)
ax2.hist(rphi1 - rphi2, bins=400, density = 'True', label = r'$ Y = X_1 - X_2 $', color = 'grey')
ax2.plot(z1_vals1, distribution1, color = 'black', linestyle = '--', label = r'$ f_{Y}(y) = \frac{1}{\pi^2} (y + \pi) \ , \ \ \ y \in[-\pi,0] $')
ax2.plot(z1_vals2, distribution2, color = 'black', linestyle = '--', label = r'$ f_{Y}(y) = \frac{1}{\pi^2} (-y + \pi) \ , \ \ \ y \in[0,\pi]  $')
ax2.set_xlim(-np.pi, np.pi)
ax2.set_ylim(0, 0.6)
ax2.legend(loc="upper right")
ax2.set_xlabel('Y')
ax2.set_ylabel('N')




nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(positions_rand)
distances, indices = nbrs.kneighbors(positions_rand)



projections = []
for index in indices:
    phi1 = points_rand[index[0],2]
    phi2 = points_rand[index[1],2]
    projection = np.cos(phi1 - phi2)
    projections.append(projection)
    
projections = np.array(projections)






#projections2 = np.cos(rphi1 - rphi2)



z_vals = np.linspace(-0.999,0.999,10000)
distribution = 2 * (np.pi - np.arccos(z_vals)) / (np.pi**2 * np.sqrt(1 - (z_vals**2) ))
ax3.hist(projections, bins=400, density = 'True', label = r'$ Z = cos(X_1 - X_2) $', color = 'grey')
#ax3.hist(projections2, bins=400, density = 'True')
ax3.plot(z_vals, distribution, color = 'black', linestyle = '--', label = r'$ \frac{2 \left[ -\arccos{(z)}  +\pi \right]}{\pi^2} \frac{1}{\sqrt{1-z^2}} $')
ax3.set_xlim(-1, 1)
ax3.set_ylim(0, 1.5)
ax3.legend(loc="upper left")
ax3.set_xlabel('Z')
ax3.set_ylabel('N')


# Show plot
plt.savefig('Example_09.png', dpi = 300)
plt.close()


'''












