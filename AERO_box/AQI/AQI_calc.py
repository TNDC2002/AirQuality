

def calculate_aqi(Cp, pollutant):
    """
    Calculate AQI (Air Quality Index) using the given parameters
    Cp: The concentration of the pollutant (in μg/m3 for PM2.5, PM10, SO2, NO2 and O3, and in ppm for CO)
    pollutant: The type of the pollutant. It can be 'pm25', 'pm10', 'so2', 'no2', 'co', or 'o3'
    """
    # Define the breakpoints for PM2.5, PM10, SO2, NO2, CO, and O3 according to the US EPA standard
    breakpoints = {
        'pm25': [(0.0, 12.0, 0, 50), (12.1, 35.4, 51, 100), (35.5, 55.4, 101, 150), (55.5, 150.4, 151, 200), (150.5, 250.4, 201, 300), (250.5, 350.4, 301, 400), (350.5, 500.4, 401, 500)],
        'pm10': [(0, 54, 0, 50), (55, 154, 51, 100), (155, 254, 101, 150), (255, 354, 151, 200), (355, 424, 201, 300), (425, 504, 301, 400), (505, 604, 401, 500)],
        'so2': [(0, 35, 0, 50), (36, 75, 51, 100), (76, 185, 101, 150), (186, 304, 151, 200), (305, 604, 201, 300), (605, 804, 301, 400), (805, 1004, 401, 500)],
        'no2': [(0, 53, 0, 50), (54, 100, 51, 100), (101, 360, 101, 150), (361, 649, 151, 200), (650, 1249, 201, 300), (1250, 1649, 301, 400), (1650, 2049, 401, 500)],
        'co': [(0, 4.4, 0, 50), (4.5, 9.4, 51, 100), (9.5, 12.4, 101, 150), (12.5, 15.4, 151, 200), (15.5, 30.4, 201, 300), (30.5, 40.4, 301, 400), (40.5, 50.4, 401, 500)],
        # something still wrong with the O3 breakpoints
        'o3': [(0, 0.054, 0, 50), (0.055, 0.070, 51, 100), (0.071, 0.085, 101, 150), (0.086, 0.105, 151, 200), (0.106, 0.200, 201, 300)]
    }

    # Find the correct breakpoint for the given pollutant concentration
    for bp in breakpoints[pollutant]:
        if bp[0] <= Cp <= bp[1]:
            Il, Ih, BPl, BPh = bp[2], bp[3], bp[0], bp[1]
            break

    # Calculate the AQI
    aqi = ((Ih - Il) / (BPh - BPl)) * (Cp - BPl) + Il
    return round(aqi)


# For example, to calculate the AQI for SO2 with a concentration of 75
# pm10_aqi = calculate_aqi(12.0, 'no2')
# print(f"The AQI for pm2.5 is {pm10_aqi}")
