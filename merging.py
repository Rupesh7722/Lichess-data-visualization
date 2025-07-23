import pandas as pd
import glob
import os

# 🔍 Folder where all monthly CSV files are stored
folder_path = "data"  # 🔁 Replace with your actual path

# 🧮 Get all CSV files in the folder (e.g. lichess_jan.csv, lichess_feb.csv, ...)
all_files = glob.glob(os.path.join(folder_path, "*.csv"))

# 🧷 Combine them
df_list = []
for file in all_files:
    df = pd.read_csv(file)
    
    # Optional: Add a 'month' column from the filename
    month_label = os.path.basename(file).split(".")[0]  # Extract name like 'lichess_jan'
    df["source_month"] = month_label
    df_list.append(df)

# 📌 Concatenate all into one DataFrame
merged_df = pd.concat(df_list, ignore_index=True)

# 💾 Save the merged file
merged_df.to_csv("lichess_merged_7months.csv", index=False)
print("✅ Merged CSV saved as 'lichess_merged_7months.csv'")
