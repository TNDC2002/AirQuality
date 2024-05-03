import pandas as pd
import glob
import datetime
from data_processing.spike_dealer import remove_spike
import matplotlib.pyplot as plt
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
    
    
    merged_df["ds"] = merged_df["Time(UTC+0)"].apply(lambda x: int(datetime.datetime.strptime(x, '%Y/%m/%d %H:%M:%S').timestamp()))
    # Drop columns
    columns_to_drop = ["Temp(°C)", "RH(%)", "CO2(ppm)", "Time(UTC+0)"]
    merged_df.drop(columns=columns_to_drop, inplace=True)
    
    # Generate unique_id column
    unique_id = "dd5fc1f864bcd715715c54af59bbf21c"
    merged_df["unique_id"] = unique_id
    
    # Rename column
    new_column_names = {"PM2.5(μm/m^3)": "y"}
    merged_df.rename(columns=new_column_names, inplace=True)
    
    merged_df = remove_spike(merged_df, 'y')
    # Rename column
    signal = "y"
    new_column_names = {signal: "old_"+signal}
    merged_df.rename(columns=new_column_names, inplace=True)
    
    new_column_names = {"y_interpolated": signal}
    merged_df.rename(columns=new_column_names, inplace=True)
    
    print(merged_df.head())
    
    # plt.figure(figsize=(10, 6))
    # plt.plot(merged_df['ds'], merged_df['old_y'], label='old_y')
    # plt.plot(merged_df['ds'], merged_df['y'], label='y')
    # plt.xlabel('Date')
    # plt.ylabel('Value')
    # plt.title('Comparison of Value 1 and Value 2')
    # plt.legend()
    # plt.grid(True)
    # plt.show()
    
    # Drop columns
    columns_to_drop = ["old_"+signal, "y_clipped", "y_ewma_fb", "y_remove_outliers", "rand"]
    merged_df.drop(columns=columns_to_drop, inplace=True)
    
    # plt.figure(figsize=(10, 6))
    # plt.plot(merged_df['ds'], merged_df['y'], label='y')
    # plt.xlabel('Date')
    # plt.ylabel('Value')
    # plt.title('Comparison of Value 1 and Value 2')
    # plt.legend()
    # plt.grid(True)
    # plt.show()
    
    # merged_df = merged_df.sort_values(by='timestamp_o')
    # print(dfs)
    return merged_df