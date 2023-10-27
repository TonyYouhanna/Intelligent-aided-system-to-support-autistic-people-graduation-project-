# -*- coding: utf-8 -*-


import os

import keras
from keras.layers import (Activation, BatchNormalization, Conv2D, Dense,
                          Dropout, Flatten, MaxPooling2D)
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator

num_classes = 5
img_rows,img_cols = 48 , 48
batch_size = 2

train_data_dir = "train" #Train images path here
validation_data_dir = "test" #Test images path here

train_data_gen = ImageDataGenerator(rescale = 1./255,
                                    rotation_range = 30,
                                    shear_range = 0.3,
                                    zoom_range = 3.0,
                                    width_shift_range = 0.4,
                                    height_shift_range = 0.4,
                                    horizontal_flip = True)
"""
since my dataset not enough (too small) for training I'm making it different images from this by rotating the image by 30%
and changing the shear angle and zooming range also shifting the wight and height while retaining the dimensions and also by
producing mirror images.
"""
validation_data_gen = ImageDataGenerator(rescale = 1./255)

train_generator = train_data_gen.flow_from_directory(train_data_dir,
                                                    color_mode = "grayscale",
                                                    target_size = (img_cols,img_rows)
                                                    ,batch_size = batch_size,
                                                    class_mode = "categorical",
                                                    shuffle = True)

validation_generator = validation_data_gen.flow_from_directory(validation_data_dir,
                                                                color_mode = "grayscale",
                                                                target_size = (img_cols,img_rows),
                                                                batch_size = batch_size,
                                                                class_mode = "categorical",
                                                                shuffle = True)

model = Sequential() # using sequential modeling

#block1
model.add(Conv2D(32,(3,3),padding="same",kernel_initializer ="he_normal",input_shape=(img_rows,img_cols,1)))
model.add(Activation("elu"))
model.add(BatchNormalization())
model.add(Conv2D(32,(3,3),padding="same",kernel_initializer ="he_normal",input_shape=(img_rows,img_cols,1)))
model.add(Activation("elu"))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.2))

#block2
model.add(Conv2D(64,(3,3),padding="same",kernel_initializer ="he_normal"))
model.add(Activation("elu"))
model.add(BatchNormalization())
model.add(Conv2D(64,(3,3),padding="same",kernel_initializer ="he_normal"))
model.add(Activation("elu"))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.2))

#block3
model.add(Conv2D(128,(3,3),padding="same",kernel_initializer ="he_normal"))
model.add(Activation("elu"))
model.add(BatchNormalization())
model.add(Conv2D(128,(3,3),padding="same",kernel_initializer ="he_normal"))
model.add(Activation("elu"))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.2))

#block4
model.add(Conv2D(256,(3,3),padding="same",kernel_initializer ="he_normal"))
model.add(Activation("elu"))
model.add(BatchNormalization())
model.add(Conv2D(256,(3,3),padding="same",kernel_initializer ="he_normal"))
model.add(Activation("elu"))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.2))

#block5
model.add(Flatten())
model.add(Dense(64,kernel_initializer="he_normal"))
model.add(Activation("elu"))
model.add(BatchNormalization())
model.add(Dropout(0.5))

#block6
model.add(Dense(64,kernel_initializer="he_normal"))
model.add(Activation("elu"))
model.add(BatchNormalization())
model.add(Dropout(0.5))

model.add(Dense(num_classes,kernel_initializer="he_normal"))
model.add(Activation("softmax"))

print(model.summary())

from keras.optimizers import RMSprop , SGD , Adam
from keras.callbacks import ModelCheckpoint , EarlyStopping , ReduceLROnPlateau

checkpoint = ModelCheckpoint("checkpoint1.h5",
                        monitor="val_loss",
                        mode="min",
                        save_best_only=True,
                        verbose=1) # checkpoint file name here in my case checkpoint1.h5

"""
Here we will monitor the val_loss which is minimum and saving it
"""

earlystop = EarlyStopping(monitor="val_loss",
                        min_delta=0,
                        patience=3,
                        restore_best_weights=True,
                        verbose=1)

"""
Here we will monitor the val_loss whith 3 extra epoches and retain the best weighted file
"""

reduce_lr = ReduceLROnPlateau(monitor="val_loss",
                             factor=0.2,
                             patience=3,
                             verbose=1,
                             min_delta=0.0001)

callbacks=[earlystop,checkpoint,reduce_lr]

model.compile(loss="categorical_crossentropy",
             optimizer=Adam(lr=0.001),
             metrics=["accuracy", "loss"] )

nb_train_samples = train_generator.n #obtained after train and validation generators
nb_validation_samples = validation_generator.n #obtained after train and validation generators
epochs = 25

#fitting/training our model

history = model.fit_generator(train_generator,
                             steps_per_epoch=nb_train_samples//batch_size,
                             epochs=epochs,
                             callbacks=callbacks,
                             validation_data=validation_generator,
                             validation_steps=nb_validation_samples//batch_size)