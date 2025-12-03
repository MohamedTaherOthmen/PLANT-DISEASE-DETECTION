from data_preparation_and_exploration import PlantDiseaseDataset
from dataset_understanding import exploreDataset
import tensorflow as tf

def main():
    DATASET_PATH = "/home/taher/Taher/Plant Disease Detection/plant-disease-detection"
    explore = exploreDataset(DATASET_PATH)
    prePros = PlantDiseaseDataset(DATASET_PATH, (224, 224), 32)
    
    explore.explore()
    (train_Generator, val_Generator) = prePros.create_data_gen()
    

if __name__ == "__main__":
    main()