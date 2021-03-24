# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:07:31 2019

@author: d8
"""
import csv
from getsvsmask import getsvsmask
import matplotlib.pyplot as plt

slide_no = 2
csv_file_path = './results_Ros_2.csv'

with open(csv_file_path) as f:
    next(f)  # Skip the header
    reader = csv.reader(f, skipinitialspace=True)
    result = dict(reader)
    
OutMask, syn1 = getsvsmask(slide_no,result)

plt.figure()
plt.imshow(syn1)
im = plt.imshow(OutMask, cmap='hot',alpha = 0.6)
plt.colorbar(im)
plt.show()