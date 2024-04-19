from request.Request_Data import Request_data
import glob

# Request_data(username="16077",password="@De0-Kinh@")
folder_path = sorted(glob.glob("./data" +'/*.csv'))
    # Iterate over files in the folder
for file_path in folder_path:
   print(file_path)