from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):

    city = serializers.CharField(max_length=20)
    country = serializers.CharField(max_length=2)



# Example of a requested url:  GET /weather?city=$City&country=$Country&

"""
# Example of fields city and country
- City is a string. Example: Valledupar
- Country is a country code of two characters in lowercase. Example: co

"""