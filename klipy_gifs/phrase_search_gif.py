# API docs link: https://docs.klipy.com/gifs-api/gifs-search-api

import requests

# CONFIG
with open("klipy_api.key", "r") as f:  # klipy_api.key file contains one line which is the API key (no quotes/no spaces)
    APP_KEY = f.readline().strip()

CUSTOMER_ID = "tempusr"                # random unique ID
LOCALE = "uk"                          
CONTENT_FILTER = "off"                 # off, low, medium, high (content safety, high = fully restricted against nsfw, off = no restrictions) 
PER_PAGE = 1                           

# USER INPUT
query = input("Search for a GIF: ")

# API REQUEST
url = (
    f"https://api.klipy.com/api/v1/{APP_KEY}/gifs/search"
    f"?page=1&per_page={PER_PAGE}&q={query}"
    f"&customer_id={CUSTOMER_ID}&locale={LOCALE}"
    f"&content_filter={CONTENT_FILTER}"
)

response = requests.get(url)
data = response.json()

# GET FIRST RESULT
try:
    gif_obj = data["data"]["data"][0]
    gif_url = gif_obj["file"]["hd"]["gif"]["url"]
except Exception:
    print("No GIF found for that search.")
    exit()

# DOWNLOAD TO SAME DIR
filename = f"{gif_obj['slug']}.gif"

gif_data = requests.get(gif_url).content
with open(filename, "wb") as f:
    f.write(gif_data)

print(f"Downloaded: {filename}")