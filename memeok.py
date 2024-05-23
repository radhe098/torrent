import pandas as pd
import requests
import os

# Directory to save files
dir_name = 'C:/Users/Expert/Desktop/torent/scrapy/one/new/nfsw'

# Ensure directory exists or create it
os.makedirs(dir_name, exist_ok=True)

# Read CSV file
df = pd.read_csv('AnimeAIPorn.csv')

# Extract unique URLs from the DataFrame
urls = set(df['url_overridden_by_dest'])

print(f"Total unique URLs: {len(urls)}")

# Download files
for i, url in enumerate(urls):
    if i >= 200:
        break  # Limit to downloading the first 200 URLs
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        filename = url.split('/')[-1]
        file_path = os.path.join(dir_name, filename)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded file {filename} from link {url}")
    except Exception as e:
        print(f"Error downloading file from link {url}: {e}")