#!/usr/bin/env python3

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, Activation, Dropout, Flatten, Dense

import keras

train_data_dir = '/home/yash/prog/Programming/ML/Learn/imageClassification1/train/train/cats'
validation_data_dir = '/home/yash/prog/Programming/ML/Learn/imageClassification1/validation/train/cats'

epochs = 50
batch = 32

img_width, img_height = 150, 150

model = Sequential()

model.add(Convolution2D(32, 3, 3, input_shape=(3, img_width, img_height)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Convolution2D(128, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Softmax())

model.compile(
    loss = 'categorical_crossentropy',
    optimizer = 'rmsprop',
    metrics = ['accuracy']
)

train_dg = ImageDataGenerator(
    rescale = 1./255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True
)

test_dg = ImageDataGenerator(
    rescale = 1./255
)

train_generator = train_dg.flow_from_directory(
    train_data_dir,
    target_size = (img_width, img_height),
    batch_size = batch,
    class_mode = 'categorical'
)

validation_generator = test_dg.flow_from_directory(
    validation_data_dir, target_size = batch,
    class_mode = 'categorical'
)

model.fit_generator(
    train_generator, samples_per_epoch = 2000,
    nb_epoch = epochs,
    validation_data = validation_generator,
    nb_val_samples = nb_validation_samples
)

model.save_weights('first.h5')
