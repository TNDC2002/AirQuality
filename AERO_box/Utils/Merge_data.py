import pandas as pd
import glob
import datetime
def get_data(folder_path = '../Data/'):
    # Initialize an empty list to store DataFrames
    dfs = []
    folder_path = sorted(glob.glob(folder_path +'/*.csv'))
    # Iterate over files in the folder
    for file_path in folder_path:
        
        # Read CSV file into DataFrame and append to the list
        df = pd.read_csv(file_path)
        df.dropna(axis=0, how='all', inplace=True)        
        dfs.append(df)

    # Merge DataFrames into a single DataFrame
    merged_df = pd.concat(dfs, ignore_index=True)
    # merged_df = merged_df.sort_values(by='timestamp_o')
    # print(dfs)
    return merged_df