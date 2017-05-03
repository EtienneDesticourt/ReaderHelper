import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
import config

class DataWrangler(object):

    def __init__(self, image_size=config.IMAGE_SIZE, batch_size=config.BATCH_SIZE):
        self.train_path = config.TRAIN_DIR
        self.val_path = config.VAL_DIR
        self.num_train_samples = len(os.listdir(self.train_path))
        self.num_val_samples = len(os.listdir(self.val_path))
        self.image_size = image_size
        self.batch_size = batch_size

    def get_train_generator(self):
        train_datagen = ImageDataGenerator(
            rescale=1./255,
            shear_range=0.1,
            zoom_range=0.1,
            rotation_range=10.,
            width_shift_range=0.1,
            height_shift_range=0.1,
            horizontal_flip=False)
        train_generator = train_datagen.flow_from_directory(self.train_path,
            target_size = self.image_size,
            batch_size = self.batch_size,
            classes = os.listdir(self.train_path))
        return train_generator

    def get_val_generator(self):
        val_datagen = ImageDataGenerator(rescale=1./255)
        validation_generator = val_datagen.flow_from_directory(self.val_path,
            target_size=self.image_size,
            batch_size=self.batch_size,
            classes = os.listdir(self.train_path))
        return validation_generator


