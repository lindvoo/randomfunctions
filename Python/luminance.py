#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:51:00 2019

@author: lindvoo
"""


# Libraries
import os
import cv2
import numpy as np

 
def rgba2gray(inputfile, outputfile):
        
    """
    pip install opencv-python 
    import cv2
        
    CONVERTS COLOR IMAGES WITH ALPHA CHANNEL TO GRAY SCALE
        
        
    LdV2019
    """
        
    #read image        
    image = cv2.imread(inputfile, cv2.IMREAD_UNCHANGED)
        
    #make gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
    #merge gray channels (to r,g,b) with the alpha channel
    img_3gray = cv2.merge((gray,gray,gray,image[:,:,3]))

    #save image
    cv2.imwrite(outputfile, img_3gray)


def eqlum(inputfile, outputfile,NEWRANGE,NEWMEAN,NEWSD):
    
    """
    pip install opencv-python 
    import cv2
    
    CHANGES THE AVERAGE PIXEL VALUE OF A GRAY SCALE IMAGE TO A SET AVERAGE
    
    LDV2019
    """
    
    # Read image     
    img = cv2.imread(inputfile, cv2.IMREAD_GRAYSCALE)
    get_alpha = cv2.imread(inputfile, cv2.IMREAD_UNCHANGED)
    
    # display
    print("Old pixel brightnes is: " + str(img.mean()))
    
    # 1) Calculate the new SD of the image [divide by old and multiply by new]
    img=(img/img.std())*NEWSD
    
    # DO NOT USE
    #----------------------
    # Equalize the histogram of the image [figure out if this adds]
    #equ = cv2.equalizeHist(image)          

    # Changes the contrast
    #clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    #img = clahe.apply(img)
    #----------------------
    
    # 2) Calculate new range of the image
    imgMin = img.min()
    imgMax = img.max()
    img = ((img - imgMin)+NEWRANGE[0]) / (imgMax - imgMin) * NEWRANGE[1];

    # 3) Make the average pixal value to a new set value
    tempmean=img.mean()
    while NEWMEAN < tempmean-.5 or NEWMEAN > tempmean+.5:

        if NEWMEAN < img.mean():
            img-=1 #subtract
            tempmean=img.mean() #new mean
            
            
        elif NEWMEAN > img.mean():
            img+=1 #add
            tempmean=img.mean() #new mean

    print("New average pixel brightnes is: " + str(img.mean()))
    
    # Change format for saving
    img=img.astype(np.uint8)
    
    # Merge gray channels (to r,g,b) with the alpha channel
    img_3gray = cv2.merge((img,img,img,get_alpha[:,:,3]))
     
    # Save new image with a fixed average pixel brightness
    cv2.imwrite(outputfile, img_3gray)
    


# RUN
#------------------------------------------------------------------------------

# loop over images
for val in range(7,12):
    
    # MAKE GRAY
    inputfile = os.path.join('/Users/lindvoo/Downloads/Beth/input/color/', str(val)+'.png')
    outputfile = os.path.join('/Users/lindvoo/Downloads/Beth/input/gray', str(val)+'.png')
    
    rgba2gray(inputfile, outputfile)
    
    # CHANGE LUMINCANCE
    #settings you can adjust them a bit and see the outcome
    NEWRANGE=[20,150]
    NEWMEAN=125
    NEWSD=20
    
    inputfile = os.path.join('/Users/lindvoo/Downloads/Beth/input/gray/', str(val)+'.png')
    outputfile = os.path.join('/Users/lindvoo/Downloads/Beth/output', str(val)+'.png')
    eqlum(inputfile, outputfile,NEWRANGE,NEWMEAN,NEWSD)

