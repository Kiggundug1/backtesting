import os
import shutil

root_folder = r"D:\FOREX\Coding\Git_&_Github\GitHub\backtesting\FX-1-Minute-Data"

# Loop through each of the 66 currency pair folders
for pair_folder in os.listdir(root_folder):
    pair_path = os.path.join(root_folder, pair_folder)

    if os.path.isdir(pair_path):
        # Loop through the 6 subfolders in each pair folder
        for subfolder in os.listdir(pair_path):
            subfolder_path = os.path.join(pair_path, subfolder)

            if os.path.isdir(subfolder_path):
                # Move CSV files from subfolder to main folder
                for filename in os.listdir(subfolder_path):
                    if filename.endswith(".csv"):
                        src = os.path.join(subfolder_path, filename)
                        dest = os.path.join(pair_path, filename)
                        shutil.move(src, dest)
                
                # Remove empty subfolder
                os.rmdir(subfolder_path)

print("✅ All files moved from subfolders to main folders across all 66 pairs.")