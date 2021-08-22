
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Serializers
from .serializers import WeatherSerializer
# Utilities
import json
import pdb
from . request_test import get_weather

# Cache
from django.core.cache import cache


@api_view(['GET'])
def weather_detail(request):                               # city and country attached to the request object
    """Return a JSON response with API weather data."""
    #pdb.set_trace()
    # Example request url: api.openweathermap.org/data/2.5/weather?q=London,uk&appid={API key}
    
    
    serializer = WeatherSerializer(data=request.GET) # WeatherSerializer(serializer)  fields country city
    serializer.is_valid()

    country = serializer.validated_data['country']
    city = serializer.validated_data['city']     # SO FAR SO GOOD!
    
    weather_data = get_weather(city, country)
    #pdb.set_trace()
    
    # Cache logic
    if cache_data := cache.get("{}-{}".format(country, city)): # := walrus operator 
        return Response(weather_data)
    
    cache.set("{}-{}".format(country, city), weather_data, timeout=60*2) # cache.set(key="{}-{}".format(country, city), value, timeout=DEFAULT_TIMEOUT, version=None)
    

    return Response(weather_data)

        
    
"""
    # Get
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }

    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )
"""
    
    #return Response(serializer.data) # Agrega content type, header parameter


"""
# Create your views here
@api_view(['GET'])
def apiOverview(request): # Receive the url request


    api_urls = {

        "List":"/motorData-List",
        "Detail View":"/motor-detail/<str:pk>/",
        "Create":"/motor-create/",
        "Update":"/motor-update/<str:pk>/",
        "Delete":"/motor-delete/<str:pk>/",

    }
    return Response(api_urls)

"""