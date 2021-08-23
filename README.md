# Globant_exercise: Weather API

## Weather API
This is an API built with Django Rest Framework, and allows to retrieve real time weather data for any location including over 200,000 cities from a third API called Open Weather (https://openweathermap.org/api).

The API support the following endpoint: <strong>/weather?city=$City&country=$Country&</strong>.

where the variable "City" is a string. Example: Valledupar, and the variable "Country" is a country code of two characters in lowercase. Example: co



## Content
* [Weather_API](#Weather API)
* [Technologies](#Tecnologies)
* [Setup](#Setup)
* [Usage](#Usage)
* [Testing](#Testing)


## Technologies

This project uses the following Python dependencies:
* Python >=3.8
* Django==3.2.6
* djangorestframework==3.12.4
* pytz==2021.1
* sqlparse==0.4.1
* asgiref==3.4.1
* certifi==2021.5.30
* charset-normalizer==2.0.4
* idna==3.2
* requests==2.26.0
* urllib3==1.26.6
* xmltodict==0.12.0*


## Setup
To run locally

```python
# Within a local folder, Clone this repository

$ git clone https://github.com/NorberMV/Globant_exercise.git

```
```python
# Create and activate a virtual environment in order to install the requirements.txt
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt

```

```python
# Configure the given environment variables in your O.S.
DJANGO_SECRET_KEY='xxxxxxxxxx'
WEATHER_SECRET_APIKEY='xxxxxxxxxx'
```

```python
# Run the database migrations
python manage.py migrate

```
```python
# in order to using the database cache, you must 
# create the cache table with this command:
$python manage.py createcachetable

```

```python
# Run the local server
$python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
Django version 3.2.6, using settings 'api_config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```


## Usage

> Open the browser and go to the endpoint and enter the  requested city and country.
ex:
  > Go to  http://localhost:8000/weather?city=Miami&country=us&


<img src="https://github.com/NorberMV/Globant_exercise/blob/master/pictures/request_api.png" width="700">



## Testing
The tests are using REST framework's test case classes and are defined in the file "weatherAPI/tests.py".
The test will check the correct functioning of the code within the functions of the views and the modules created
sending requests and comparing them with expected values.
In order to carry out the tests, you need to have running the API locally and open another terminal.


```python
# Go to the project file "globant_exercise"
$python manage.py test

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.983s

OK
Destroying test database for alias 'default'...

```




Author: Norberto Moreno | 2021
