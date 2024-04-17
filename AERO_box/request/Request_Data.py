import requests
import datetime
import os

def get_data_with_cookie(cookie, start_date, end_date):
    base_url = "https://legacy.ideasky.app/device/downloadCsvFile/"
    query_params = {
        "w_id": "dd5fc1f864bcd715715c54af59bbf21c",
        "mean": "r",
        "s_t": start_date.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "e_t": end_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    }
    headers = {
        "Cookie": "sessionid="+cookie  # Include the session cookie in the request headers
    }
    response = requests.get(base_url, params=query_params, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        print("Error:", response.status_code)
        return None

def Request_data(cookie="hutq38pdot7jzmnlq4wgx7xlfx5sxeo6"):
    start_date = datetime.datetime(2022, 9, 1)
    end_date = datetime.datetime(2022, 9, 30, 23, 59, 59, 999000)  # Last millisecond of September 2022
    end_month = datetime.datetime(2024, 4, 1)
    directory = "./data"  # Directory to store the files

    if not os.path.exists(directory):
        os.makedirs(directory)

    while end_date <= end_month:
        data = get_data_with_cookie(cookie, start_date, end_date)
        if data:
            # Save the response content to a file
            filename = end_date.strftime("%Y-%m-%d") + ".csv"
            filepath = os.path.join(directory, filename)
            with open(filepath, "wb") as f:
                f.write(data)
            print("Data saved to:", filepath)
            # Update start_date and end_date for the next iteration
            start_date = end_date + datetime.timedelta(seconds=1)
            end_date += datetime.timedelta(days=30)  # Adding 30 days for the next month (may need adjustment for February)
        else:
            # Break the loop if there's an error fetching data
            break

# Provide your session cookie here
# session_cookie = "hutq38pdot7jzmnlq4wgx7xlfx5sxeo6"

# Request_data(session_cookie)
