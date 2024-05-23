url= 'https://i.redd.it/21jz7u106okc1.jpeg'

import os
import requests
from pathlib import Path

def download_media(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the current directory
        current_dir = os.getcwd()
        # Get the filename from the URL
        filename = Path(url).name
        # Join the current directory with the filename
        file_path = os.path.join(current_dir, filename)
        # Open a file for writing in binary mode
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print("Downloaded successfully!")
    else:
        print("Failed to download. Status code:", response.status_code)


        