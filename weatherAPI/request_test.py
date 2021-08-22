
import os
import requests
import pdb
from datetime import datetime
import xmltodict
import json
#import xml.etree.ElementTree as ET


def get_weather(city, country):

    api_key =  os.environ.get('WEATHER_SECRET_APIKEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&mode=xml"
    #pdb.set_trace()
    response = requests.get(url) #.json()
          
    #root = ET.fromstring(response.content)
    
    data_json = json.dumps(xmltodict.parse(response.content)) # JSON string
    #print(root)

    current_data = json.loads(data_json)       # Return all weather data in JSON ALL GOOD SO FAR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    data = current_data['current']
    # Kelvin to Celsius formula: °K − 273.15 = °C
    # Fields units API response:  https://openweathermap.org/current#parameter
    
    #pdb.set_trace()
    #city = data['city']['@name']
    #country = data['city']['country']   
    location_name = "{}, {}".format(data['city']['@name'], data['city']['country'] )
    tempc = float(data['temperature']['@value']) - 273.15
    tempf = (tempc * (9/5)) + 32
    # Wind variables
    wind_name = data['wind']['speed']['@name']  # "Minor" if age < 18 else "Adult"
    wind_descript_name = wind_name if wind_name != None else "No description available"
    wind_val = data['wind']['speed']['@value']
    wind_value = wind_val if wind_val != None else "No description available"
    wind_dir = data['wind']['direction']['@name']
    wind_direction = wind_dir if wind_dir != None else "No description available"

    cloudiness = data['clouds']['@name']
    pressure = data['pressure']['@value']
    humidity = data['humidity']['@value']
    #sunrise_val = data['sys']['sunrise'] # unix
    
    sunrise_list = data['city']['sun']['@rise'].split("T")
    sunrise = sunrise_list[1]
    # datetime.fromtimestamp(int(data['city']['sun']['@rise'])).strftime('%H:%M hrs')
    sunset_list = data['city']['sun']['@set'].split("T") # datetime.fromtimestamp(int(data['city']['sun']['@set'])).strftime('%H:%M hrs')
    sunset = sunset_list[1]
    coord_lat = data['city']['coord']['@lat']
    coord_lon = data['city']['coord']['@lon']
    #dt = data['dt'] # UNIX Timestamp
    requested_time = data['lastupdate']['@value'] # datetime.fromtimestamp(int(dt)).strftime('%b %dth, %Y - %H:%M:%S    hrs')
    # .format(now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')

    # Weather Conditions

    
    


    weather_dict = {

        'location_name': location_name,
        'temperature': '%.2f°C, %.2f°F' % (tempc,tempf), #'{}%.2f °C , {} °F'.format(tempc, tempf),
        'wind': '{}, {} m/s, {}'.format(wind_descript_name, wind_value, wind_direction),                                    # Gentle breeze, 3.6 m/s, west-northwest",
        'cloudiness': cloudiness,                              # "Scattered clouds",
        'pressure': '{} hpa'.format(pressure),
        'humidity': '{} %'.format(humidity),
        'sunrise': sunrise, 
        'sunset': sunset,
        'geo_coordinates': '[{}, {}]'.format(coord_lat, coord_lon),
        'requested_time': requested_time,
        'forecast': '{...}'

    }

    return weather_dict

"""
# Driver code

if __name__=='__main__':

    city = "Medellin"
    country ="co"
    appid = "a6137ea16e87e2bc163535233cefd4e6"

    weather_data = get_weather(appid, city, country)
    print(weather_data)
    pdb.set_trace()


"""


# Expected dict result

"""
Response: {
  "location_name": "Bogota, CO",
  "temperature": "17 °C",
  "wind": Gentle breeze, 3.6 m/s, west-northwest",
  "cloudiness": "Scattered clouds",
  "pressure": "1027 hpa",
  "humidity": "63%",
  "sunrise": "06:07",
  "sunset": "18:00",
  "geo_coordinates": "[4.61, -74.08]",
  "requested_time": "2018-01-09 11:57:00"
  "forecast": {...}
}
"""


"""
city_name = "city here"
api_key = "key here"

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url).json()

    temp = response['main']['temp']
    temp = math.floor((temp * 1.8) - 459.67)  # Convert to °F

    feels_like = response['main']['feels_like']
    feels_like = math.floor((feels_like * 1.8) - 459.67)  # Convert to °F

    humidity = response['main']['humidity']
    
    return {
        'temp': temp,
        'feels_like': feels_like,
        'humidity': humidity
    }
    """