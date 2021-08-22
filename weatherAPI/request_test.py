
import requests
import pdb
from datetime import datetime


def get_weather(city, country):

    api_key = "a6137ea16e87e2bc163535233cefd4e6"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}"

    response = requests.get(url) #.json()
    data = response.json()       # Return all weather data in JSON

    # Kelvin to Celsius formula: °K − 273.15 = °C
    # Fields units API response:  https://openweathermap.org/current#parameter
    
    
    city = data['name']
    country = data['sys']['country']
    location_name = "{},{}".format(city, country)
    tempc = data['main']['temp'] - 273.15
    tempf = (tempc * (9/5)) + 32
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    sunrise_val = data['sys']['sunrise']
    sunrise = f"{sunrise_val}%"
    sunset = data['sys']['sunset']
    coord_lat = data['coord']['lat']
    coord_lon = data['coord']['lon']
    dt = data['dt'] # UNIX Timestamp
    requested_time = datetime.fromtimestamp(int(dt))
 


    weather_dict = {

        'location_name': location_name,
        'temperature': [ tempc, tempf ],
        'wind': None,
        'cloudiness': None,
        'pressure': pressure,
        'humidity': None,
        'sunrise': sunrise,
        'sunset': sunset,
        'geo_coordinates': [coord_lat, coord_lon],
        'requested_time': requested_time,

    }

    return {
        'weather_dict': weather_dict,
    }

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