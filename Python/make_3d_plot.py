#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 15:48:21 2021

With this script you can make a 3D plot of 2 ROIs and its overlap

@author: lindvoo
"""

# Import libraries
import matplotlib.pyplot as plt
import numpy as np
from nilearn.image import load_img, get_data

# Import 3D projection
from mpl_toolkits.mplot3d import Axes3D 

# Read in images
img1 = load_img('XXX.nii')
img2 = load_img('XXX.nii')
voxels1 = get_data(img1)
voxels2 = get_data(img2)

# Remove slices that do not contain the ROI [reduce comp load and easy plotting]
whichslices=[]
for c,val in enumerate(voxels1[:,0,0]):
    
    if (np.sum(voxels1[c,:,:]))>0:
        whichslices.append(c)

voxels1 = voxels1[whichslices[0]:whichslices[-1],:,:]
voxels2 = voxels2[whichslices[0]:whichslices[-1],:,:]

whichslices=[]
for c,val in enumerate(voxels1[0,0,:]):
    
    if (np.sum(voxels1[:,:,c]))>0:
        whichslices.append(c)

voxels1 = voxels1[:,:,whichslices[0]:whichslices[-1]]
voxels2 = voxels2[:,:,whichslices[0]:whichslices[-1]]

whichslices=[]
for c,val in enumerate(voxels1[0,:,0]):
    
    if (np.sum(voxels1[:,c,:]))>0:
        whichslices.append(c)

voxels1 = voxels1[:,whichslices[0]:whichslices[-1],:]
voxels2 = voxels2[:,whichslices[0]:whichslices[-1],:]

# Make boolean to create a figure with both
bool_voxels1 = np.zeros(voxels1.shape, dtype=bool)
bool_voxels2 = np.zeros(voxels2.shape, dtype=bool)
for x,xval in enumerate(voxels1[:,0,0]):
    for y,yval in enumerate(voxels1[0,:,0]):
        for z,xval in enumerate(voxels1[0,0,:]):
    
            bool_voxels1[x,y,z] = voxels1[x,y,z]>0
            bool_voxels2[x,y,z] = voxels2[x,y,z]>0

# Create overlap
combined = bool_voxels1 | bool_voxels2
overlap = bool_voxels1 & bool_voxels2
 
# Set the colors of each object
colors = np.empty(overlap.shape, dtype=object)
colors[bool_voxels1] = 'blue'   
colors[bool_voxels2] = 'green'    
colors[overlap] = 'red'      

# With np.transpose(overlap, (2, 1, 0)) you can transpose the array

# Plot  
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.voxels(combined, 
          facecolors=colors,
          alpha=.5)
plt.axis('off')
plt.show()
