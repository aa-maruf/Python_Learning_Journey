""" 
2. Use web search to find some API to get weather data. 
Use that to get your region’s weather data every 30 minute.

"""

import requests
import time

# Solution - 1
# city = input('input the city name:')
# print ('Displaying weather report for :' + city)

# url = 'https://wttr.in/{}'.format(city)
# res = requests.get(url)

# print(res.text)


# Solution - 2 ( Using ...)
def weather_data():
    ur_template = "https://api.openweathermap.org/data/2.5/weather?q=" # {city name}&appid={API key}
    API_Key = "&appid=fd21bfe4c4df16bacd53e77bf55dd183"
    url = ur_template + city_name + API_Key
    response = requests.get(url)   # gives string or status code
    data = response.json()

    # print weather data
    print (f"Weather forcast : {city_name}")
    print("----------------------------------------")

    print(f'Current Temperature : {data["main"]["temp"]}')
    print(f'Feels like :        : {data["main"]["feels_like"]}')
    print(f'Minimum Temperature : {data["main"]["temp_min"]}')
    print(f'Maximum Temperature : {data["main"]["temp_max"]}')
    print(f'Pressure            : {data["main"]["pressure"]}')
    print(f'Humidity            : {data["main"]["humidity"]}')
    print(f'Wind                : {data["wind"]["speed"]}')
    print(f'Sunrise             : {data["sys"]["sunrise"]}')
    print(f'Sunset              : {data["sys"]["sunrise"] }')
    print("___________________________________")

city_name = input('Enter the city name:')

# Call the function every 30 minutes
while (True):
    weather_data()
    time.sleep (1800) 
    #break

