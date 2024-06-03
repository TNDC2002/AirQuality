import datetime
import pandas as pd
import matplotlib.pyplot as plt
from Utils.Merge_data import get_data
from AQI.AQI_calc import calculate_aqi
import os
# Sample DataFrame creation (replace this with your actual DataFrame)
def plot_hist(path, save_path="./data/Historgram"):
    df = pd.read_csv(path)

    # Convert timestamp to datetime
    df["ds"] = df["Time(UTC+0)"].apply(lambda x: int(datetime.datetime.strptime(x, '%Y/%m/%d %H:%M:%S').timestamp()))
    # Calculate AQI for PM2.5 values
    df['AQI'] = df['PM2.5(μm/m^3)'].apply(lambda x: calculate_aqi(x, 'pm25'))

    # Convert 'ds' timestamp to datetime
    df['Time(UTC+0)'] = pd.to_datetime(df['ds'], unit='s')

    # Extract the date from the datetime column
    df['Date'] = df['Time(UTC+0)'].dt.date

    # Calculate the average AQI for each date
    daily_avg_AQI = df.groupby('Date')['AQI'].mean()

    # Plot histogram for AQI
    plt.figure(figsize=(15, 6))
    plt.bar(daily_avg_AQI.index, daily_avg_AQI.values, color='skyblue', alpha=0.7)
    plt.xlabel('Date')
    plt.ylabel('Average AQI per date')
    plt.title('Histogram of Average AQI per Date')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.grid(True)
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    
    # Save the plot with the same name as the CSV file but with .png extension
    csv_name = os.path.splitext(os.path.basename(path))[0]  # Extract CSV file name without extension
    save_path = save_path+f"{csv_name}.png"  # Save with the same name but with .png extension
    plt.savefig(save_path)
    plt.show()