""" 
Problem:
    Download and change desktop wallpapers automatically
    
 """
import requests
# from requests import get
import json
import PyWallpaper
api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
# Nasa open api (apod)

# get the json
response = requests.get(api_url)
content = response.content.decode('UTF-8')

# convert string to json
dict_content = json.loads(content) # loads -> load string

# get the image url
image_url = dict_content['url']
# print(image_url)

# download the image 
res = requests.get(image_url)
# print(res)

# save the image
with open('apod.png','wb') as image:  
    image.write(res.content)  # wb = w truncate b for binary

# set as wallpaper
PyWallpaper.change_wallpaper('C:\\Learn Python\\apod.png')