""" Weather API, and function Tests."""
# Run the API locally is required to carry out the tests

# Django rest framework
from rest_framework import status
from rest_framework.test import APITestCase

# Utils
from . requestapi import get_weather



# Create your tests here.

class WeatherAPITest(APITestCase):
    """ Run test over the our weather API to check
        the response status ."""

    def test_api_url(self):
        """ Make a GET request to the API endpoint."""

        # requested API endpoint with the city=Bogota,country=Medellin
        url = 'http://localhost:8000/weather?city=Bogota&country=co&'  # Weather API endpoint
        response = self.client.get(url)                                # Response object from the API
        
        # Check if the response status code is 200
        self.assertTrue(status.is_success(response.status_code))       
        
        


class FuncThirdAPITest(APITestCase):
    """ Run test over the test_get_weather() function
        from the requestapi.py module."""

    def test_get_weather(self):
        """Test the test_get weather() function."""
        # Testing variables
        city = 'Medellin'
        country = 'co'
        weather_data = get_weather(city, country)                 # Call to the function
       
        # Check if the result dictionary has the correct location_name value
        self.assertEqual(weather_data['location_name'], 'Medellín, CO') 


