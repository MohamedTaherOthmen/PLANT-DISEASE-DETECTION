import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers, models, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

tf.random.set_seed(42)
np.random.seed(42)

class PlantDiseaseDataset:
    def __init__(self, data_path, image_size=(224, 224), batch_size=32):
        self.data_path = data_path
        self.image_size = image_size
        self.batch_size = batch_size
        self.class_names = []
        self.nbr_classes = 0
    
    def create_data_gen(self):

        train_datagen = preprocessing.image.ImageDataGenerator(
            rescale=1./255,
            rotation_range=40, 
            width_shift_range=0.2,
            height_shift_range=0.2, 
            shear_range=0.2, 
            zoom_range=0.2, 
            horizontal_flip=True, 
            fill_mode='nearest', 
            brightness_range=[0.6, 1.4],
            channel_shift_range=50.0,  
            validation_split=0.2
        )

        val_datagen = preprocessing.image.ImageDataGenerator(
            rescale = 1./255,
            validation_split = 0.2  
        )

        train_generator = train_datagen.flow_from_directory(
            directory = os.path.join(self.data_path, 'Dataset'),
            target_size = self.image_size,
            batch_size = self.batch_size,
            class_mode = 'categorical',
            subset = 'training',
            shuffle = True,
            seed = 42
        )

        val_generator = val_datagen.flow_from_directory( 
            directory = os.path.join(self.data_path, 'Dataset'),
            target_size = self.image_size,
            batch_size = self.batch_size,  
            class_mode = 'categorical',
            subset = 'validation',
            shuffle = False,
            seed = 42
        )

        self.class_names = list(train_generator.class_indices.keys())  
        self.nbr_classes = len(self.class_names)

        print(f"Number of classes = {self.nbr_classes}")
        print(f"Classes : {self.class_names}")

        return train_generator, val_generator