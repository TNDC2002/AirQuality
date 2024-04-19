import requests
import datetime
import os

import requests
import datetime
import os


def authenticate(username, password):
    login_url = 'https://legacy.ideasky.app/user/login/'
    session = requests.Session()

    # First, send a GET request to the login page to retrieve the CSRF token
    login_page_response = session.get(login_url)
    csrf_token = session.cookies.get('csrftoken')  # Extract CSRF token from cookies

    # Prepare the login form data including the CSRF token
    login_data = {
        'username': username,
        'password': password,
        'csrfmiddlewaretoken': csrf_token,
        'next': '/user/device/dashboard/'  # Redirect URL after login
    }

    # Add the Referer header indicating the login page URL
    headers = {
        'Referer': login_url
    }

    # Perform login by sending a POST request with the login form data
    response = session.post(login_url, data=login_data, headers=headers)

    # Check if the response indicates a successful login
    if response.ok and response.url == 'https://legacy.ideasky.app/user/device/dashboard/':
        print("Authentication successful")
        session_cookie = session.cookies.get('sessionid')  # Extract session cookie after successful login
        return session, session_cookie  # Return the authenticated session and session cookie
    else:
        print("Authentication failed")
        return None, None

# Rest of the code remains the same...

def get_data_with_cookie(session_cookie, csrf_token, start_date, end_date):
    base_url = "https://legacy.ideasky.app/device/downloadCsvFile/"
    query_params = {
        "w_id": "dd5fc1f864bcd715715c54af59bbf21c",
        "mean": "r",
        "s_t": start_date.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "e_t": end_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    }
    headers = {
        "Cookie": f"sessionid={session_cookie}; csrftoken={csrf_token}"
    }
    response = requests.get(base_url, params=query_params, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        print("Error:", response.status_code)
        return None

def Request_data(username, password, directory="./data"):
    session, session_cookie = authenticate(username, password)
    if session and session_cookie:
        start_date = datetime.datetime(2023, 9, 1)
        end_date = datetime.datetime(2023, 9, 30, 23, 59, 59, 999000)  # Last millisecond of September 2023
        end_month = datetime.datetime(2024, 4, 1)

        if not os.path.exists(directory):
            os.makedirs(directory)

        csrf_token = session.cookies.get('csrftoken')

        while end_date <= end_month:
            data = get_data_with_cookie(session_cookie, csrf_token, start_date, end_date)
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
                print("Failed to fetch data")
                break
    else:
        print("Authentication failed")

# Replace 'your_username' and 'your_password' with your actual credentials
# request_data('your_username', 'your_password')
