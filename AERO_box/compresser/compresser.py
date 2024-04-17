import pandas as pd
import datetime
df = pd.read_csv('./data/data.csv')
# print(df.head(1)["Time(UTC+0)"].item())

# Convert Time(UTC+0) to timestamp
df["sorter"] = df["Time(UTC+0)"].apply(lambda x: datetime.datetime.strptime(x, '%Y/%m/%d %H:%M:%S').timestamp())

# Sort DataFrame based on the timestamp
df = df.sort_values(by="sorter")

# Calculate the ceiling-rounded average of every sixty rows (representing 1 hour) and store it in a new DataFrame
new_rows = []
for i in range(0, len(df), 360):
    if i + 59 < len(df):
        avg_pm25 = round(df.iloc[i:i+360]["PM2.5(μm/m^3)"].mean(), 2)
        avg_temp = round(df.iloc[i:i+360]["Temp(°C)"].mean(), 2)
        avg_rh = round(df.iloc[i:i+360]["RH(%)"].mean(), 2)
        avg_co2 = round(df.iloc[i:i+360]["CO2(ppm)"].mean(), 2)
        new_rows.append({
            "Time(UTC+0)": df.iloc[i]["Time(UTC+0)"],
            "PM2.5(μm/m^3)": avg_pm25,
            "Temp(°C)": avg_temp,
            "RH(%)": avg_rh,
            "CO2(ppm)": avg_co2
        })

# Create a new DataFrame with the averaged data
new_df = pd.DataFrame(new_rows)

print(new_df.head())