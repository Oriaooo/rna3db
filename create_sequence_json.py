import json

# Define paths
SPLIT_FILE = "rna3db/split.json"

# Load the split information
with open(SPLIT_FILE, "r") as f:
    split_data = json.load(f)

for dataset_id, dataset in split_data.items():
    sequence_dict = {}
    for component in dataset.values():
        for group in component.values():
            for seq_id, seq_info in group.items():
                sequence_dict[seq_id] = seq_info["sequence"]
    json.dump(sequence_dict, open(f"sequences_{dataset_id}.json", "w"))
