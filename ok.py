import pandas as pd
import httpx
import time

base_url = "https://www.reddit.com"
# endpiont = "r/NSFW_AI_Images"
endpiont = "r/AnimeAIPorn"
category = "/hot"

url = f"{base_url}/{endpiont}{category}.json"
after_post_id = None

dataset = []

for i in range(5):
    params = {
        'limit': 100,
        't': 'month',
        'after': after_post_id   
    }
    response = httpx.get(url, params=params)
    print(f"fetching {response.url}")
    if response.status_code != 200:
        raise Exception("Error fetching data")
    json_data = response.json()
    dataset.extend(json_data['data']['children'])

    after_post_id = json_data['data']['after']
    time.sleep(0.5)

df = pd.DataFrame([post['data'] for post in dataset])    
df.to_csv('AnimeAIPorn.csv', index=False)
