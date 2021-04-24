# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:22:10 2019

@author: d8
"""

from keras.models import load_model
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
import pandas as pd
import tensorflow as tf
import keras


img_width, img_height = 250,250
BATCH_SZ = 32
PATH_TO_MODEL = '/home/d8/FINDBESTWSI/V3_myModel_KiStain_E10M9B32.h5'
Path_to_test_folder = "/hdd/d8/Ki67_3patch/Test_USCAP/Test_Ki/" #SynTest,Test_slideByslide, '/hdd/d8/Ki67TF/Test9WSI/'
Path_to_train_folder = '/hdd/d8/Ki67_3patch/Ki_staintest/Train' # Just to get the class labels, #'/hdd/d8/Ki67TF/SortedSyn/Train'
SAVE_AS_CSV = "results_kiO_USCAP.csv" # to be saved as


model = load_model(PATH_TO_MODEL)
test_dir = Path_to_test_folder 
train_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
                        Path_to_train_folder,
                        target_size=(img_width, img_height),
                        batch_size=BATCH_SZ,
                        class_mode='categorical')
test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(img_width, img_height),
        color_mode="rgb",
        shuffle = False,
        class_mode=None,
        batch_size=1)

filenames = test_generator.filenames
nb_samples = len(filenames)

STEP_SIZE_TEST=test_generator.n//test_generator.batch_size
test_generator.reset()
pred=model.predict_generator(test_generator,
steps=STEP_SIZE_TEST,
verbose=1)
predicted_class_indices=np.argmax(pred,axis=1)
labels = (train_generator.class_indices)
labels = dict((v,k) for k,v in labels.items())
predictions = [labels[k] for k in predicted_class_indices]

filenames=test_generator.filenames
results=pd.DataFrame({"Filename":filenames,
                      "Predictions":predictions})
results.to_csv(SAVE_AS_CSV,index=False)
