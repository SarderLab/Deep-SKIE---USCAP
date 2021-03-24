# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:14:04 2019

@author: d8
"""
#
#import sys
#sys.path.append("./Functions/")

import openslide
import numpy as np

def getsvsmask(slide_no,dict_file):

    print(slide_no)
        
    '''Variables'''
    '''=========='''
    w = 250

    '''Get pointer for WSI'''
    ''' ====================='''
    
    source2 = openslide.open_slide("/hdd/d8/Images/Roswell/"+str(slide_no)+".svs")

    print("Opening WSIs in mid resolution...")
    syn = np.array(source2.read_region((0,0),1,source2.level_dimensions[1]),dtype = "uint8")
    
    print("Removing alpha channel...")
    syn1 = syn[:,:,0:3]
                   
    dimX = source2.level_dimensions[1][1]
    dimY = source2.level_dimensions[1][0]
        
    x_startPoints = range(0,dimX,w)
    y_startPoints = range(0,dimY,w)
    OutMask = np.zeros(syn1[:,:,0].shape)

    All_starts = []
    for xpoint in x_startPoints:
        for ypoint in y_startPoints:
            All_starts.append([xpoint,ypoint])
    countPatch  = 0  
    for eachPoint in All_starts:
        
        synMskMR = np.uint8(syn1[int(eachPoint[0]):int(eachPoint[0]+w),int(eachPoint[1]):int(eachPoint[1]+w),0:3])
        if synMskMR[:,:].shape == (w,w,3):  
            print("Saved name = "+str(slide_no)+'_'+str(countPatch))#           
            saved_name = str(slide_no)+'_'+str(countPatch);
            sttx = int(eachPoint[0])
            stpx = int(eachPoint[0]+(w))
            stty = int(eachPoint[1])
            stpy = int(eachPoint[1]+(w))

            for values,keys in dict_file.items():
                print("Saved name = "+str(slide_no)+'_'+str(countPatch)+"Pred_name: "+(values))
                if values == saved_name:
                    OutMask[sttx:stpx,stty:stpy] = int(keys)*np.ones((w,w))
                else: 
                    continue
            countPatch += 1

    return(OutMask,syn1)
#    

