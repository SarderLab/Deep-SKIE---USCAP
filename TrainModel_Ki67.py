# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:10:11 2019

@author: d8
"""
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model
from keras.applications.inception_v3 import InceptionV3
from keras.layers import Dense, GlobalAveragePooling2D
from keras.optimizers import SGD

img_width, img_height = 250,250
nb_train_samples = 13525
nb_validation_samples = 1400

base_model = InceptionV3(weights='imagenet', include_top=False)
    
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(4, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)


train_datagen = ImageDataGenerator(rescale=1./255)
validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
                        '/hdd/d8/Ki67_3patch/Ki_staintest/Train',
                        target_size=(img_height,img_width),
                        batch_size=batch_size,
                        class_mode='categorical')

validation_generator = validation_datagen.flow_from_directory(
                            '/hdd/d8/Ki67_3patch/Ki_staintest/Validation',
                            target_size=(img_height,img_width),
                            batch_size=batch_size,
                            class_mode='categorical')


EPOCHS = 10
batch_size = 32
lrate = 0.1
decayrate = lrate/EPOCHS
opt = SGD(lr=lrate, momentum = 0.9,decay = decayrate)

model.compile(loss = "categorical_crossentropy", optimizer = opt, metrics=['binary_accuracy'])

history = model.fit_generator(
    train_generator,
    samples_per_epoch=nb_train_samples,
    epochs=EPOCHS,
    validation_data=validation_generator,
    nb_val_samples=nb_validation_samples)


model.summary()

model.save('V3_myModel_KiStain_E10M9B32.h5')  

#f1 = plt.figure()
#plt.plot(history.history['binary_accuracy'])
#plt.plot(history.history['val_binary_accuracy'])
#plt.title('Model accuracy')
#plt.ylabel('Accuracy')
#plt.xlabel('Epoch')
#plt.legend(['Train_acc', 'Validation_acc'], loc='upper left')
#plt.show()
#f1.savefig("KiStain1_E10.png",format='png', dpi=1200)
#
#f2= plt.figure()
#plt.plot(history.history['loss'])
#plt.plot(history.history['val_loss'])
#plt.title('Model loss')
#plt.ylabel('Loss')
#plt.xlabel('Epoch')
#plt.legend(['Train_loss', 'Validation_loss'], loc='upper left')
#plt.show()
#f2.savefig("KiStain2_E10.png",format='png', dpi=1200)
