import os


DATASET_PATH = "/home/taher/Taher/Plant Disease Detection/plant-disease-detection"

def explore(path):
    print("Plant Disease Detection Dataset")
    for dirpath, dir, file in os.walk(path, topdown=True):
        level = dirpath.replace(path, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(dirpath)}/")
        sub_indent = ' ' * 2 * (level + 1)
        for file in file[:3]:
            print(f"{sub_indent}{file}")
        if len(file) > 3:
            print(f"{sub_indent}... and {len(file)-3} more files")
    
    # Count classes
    dataset = os.path.join(path, 'Dataset')
    if os.path.exists(dataset):
        classes = os.listdir(dataset)
        print(f"\nNumber of classes: {len(classes)}")
        print("Sample classes:\n", classes)

explore(DATASET_PATH)