from data_preparation_and_exploration import PlantDiseaseDataset
import tensorflow as tf

def main():
    print("Tensorflow version:", tf.__version__)
    DATASET_PATH = "/home/taher/Taher/Plant Disease Detection/plant-disease-detection"
    prePros = PlantDiseaseDataset(DATASET_PATH, (224, 224), 32)
    prePros.create_data_gen()



if __name__ == "__main__":
    main()