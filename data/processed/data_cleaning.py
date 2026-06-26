import pandas as pd
import glob 
files = glob.glob("data/processed/*.csv")
df_list = []
for file in files:
    df = pd.read_csv(file)
    df_list.append(df)
    merged_df = pd.concat(df_list, ignore_index=True)
    merged_df.to_csv("data/processed/all_funds_cleaned.csv", index=False)
    print("files merged successfully!")
    print("Total rows:", len(merged_df))
    

    


    
    
    