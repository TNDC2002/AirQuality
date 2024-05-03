from request.Request_Data import Request_data
import glob
from data_processing.compresser import Compresser
from Utils.Merge_data import get_data
from data_processing.spike_dealer import remove_spike
import matplotlib.pyplot as plt
# Request_data(username="16077",password="@De0-Kinh@")


# compress data:
# folder_path = sorted(glob.glob("./data" +'/*.csv'))
# print(folder_path)
# for file_path in folder_path:
#     # save_path = None -> save the compressed file in the same location as the original file
#     compressed = Compresser(average=360,path=file_path, save_path=None)
#     print("Compressed file: ", file_path.split("/")[-1], "new df:", compressed)


# Merge data:
merged_df = get_data(folder_path = './data/')
print("Merged data: ", merged_df)

# spike dealer:

# df = get_data("./data")
# df = remove_spike(df, 'y')
# df.to_csv(save_path, index=False)

# # Plotting
# plt.figure(figsize=(10, 6))
# plt.plot(merged_df['ds'], merged_df['y'], label='y')
# plt.xlabel('Date')
# plt.ylabel('Value')
# plt.title('Comparison of Value 1 and Value 2')
# plt.legend()
# plt.grid(True)
# plt.show()