import os
import shutil
import json

# Define paths
SOURCE_DIR = 'rna3db-mmcifs'
DESTINATION_DIR = 'dataset'
SPLIT_FILE = 'outputs/split.json'

# Load the split information
with open(SPLIT_FILE, 'r') as f:
    split_data = json.load(f)

for split in list(split_data.keys()):
    os.makedirs(os.path.join(DESTINATION_DIR, split), exist_ok=True)
    components = list(split_data[split].keys())
    for component in components:
        shutil.copytree(os.path.join(SOURCE_DIR, component), os.path.join(DESTINATION_DIR, split, component))
