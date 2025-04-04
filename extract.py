import os
import pandas as pd

# Dictionary of known shot types
shot_type_translation = {
    "放小球": "net shot",
    "擋小球": "return net",
    "殺球": "smash",
    "點扣": "wrist smash",
    "挑球": "lob",
    "防守回抛": "defensive return lob",
    "長球": "clear",
    "平球": "drive",
    "小平球": "driven flight",
    "後場抽平球": "back-court drive",
    "切球": "drop",
    "過渡切球": "passive drop",
    "推球": "push",
    "撲球": "rush",
    "防守回抽": "defensive return drive",
    "勾球": "cross-court net shot",
    "發短球": "short service",
    "發長球": "long service"
}

# Folder containing CSV files (update path accordingly)
folder_path = "/home/lucia/Documents/GitHub/CoachAI-Projects/ShuttleSet/set"

# Collect unique shot types
unique_shot_types = set()

# Walk through all subdirectories and find CSV files
for root, _, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".csv"):
            file_path = os.path.join(root, file)
            print(f"Processing: {file_path}")
            df = pd.read_csv(file_path, encoding="utf-8")  # Change encoding if needed
            
            # Ensure "shot type" column exists
            if "shot type" in df.columns:
                unique_shot_types.update(df["shot type"].dropna().astype(str))

# Find unknown shot types
unknown_shots = unique_shot_types - set(shot_type_translation.keys())

# Print results
print("Unknown shot types:")
print(unknown_shots)
