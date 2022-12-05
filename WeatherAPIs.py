"""
Author: Matt Wolf, Brady Shuck
Course: CMSC495
Purpose: This program is a series of API calls to OpenWeatherAPI for Location and Weather Data.
"""

import requests

API_SECRET = '&appid=c498ab6233adc1ec28ededc44418df6a'


''' 
this function converts zipcode and country code to lat-lon coordinates to build 
'''
def get_location_zip(x,y):
    location_api_url = 'https://api.openweathermap.org/geo/1.0/zip?zip='
    zip_code = x
    country_code = y
    build_location = zip_code + (",") + country_code
    build_geolocation_url = location_api_url + build_location + API_SECRET
    geolocation_response = requests.get(build_geolocation_url)
    geolocation_data = geolocation_response.json()
    latitude_cords = format(geolocation_data["lat"], ".2f")
    longitude_cords = format(geolocation_data["lon"], ".2f")
    coordinates = "lat=" + str(latitude_cords) + "&" + "lon=" + str(longitude_cords)
    return coordinates

"""
This function converts a city name into lat-lon coordinates to build
"""
def get_location_city(x,y):
    location_api_url = 'http://api.openweathermap.org/geo/1.0/direct?q='
    city_code = x
    country_code = y
    build_location = city_code + (",") + country_code
    build_geolocation_url = location_api_url + build_location + API_SECRET
    geolocation_response = requests.get(build_geolocation_url)
    geolocation_data = geolocation_response.json()
    for entry in geolocation_data:
        latitude_cords = format(entry["lat"])
        longitude_cords = format(entry["lon"])
    coordinates = "lat=" + str(latitude_cords) + "&" + "lon=" + str(longitude_cords)
    return coordinates

"""
This function takes in two values, the first is either a zip code or city name, the second is a two character country code
such as GB (great britain) FR (france) or US ( United states)
it then returns coordinate for use by the weather fetchers
"""
def get_location(x,y):
    try:
        coordinate = get_location_zip(x, y)
        return coordinate
    except KeyError:
        pass
    try:
        coordinate = get_location_city(x, y)
        return coordinate
    except:
        return("INVALID INPUT")

"""
this function calls the OpenWeatherAPI for current forecast data
"""
def get_current_forecast(x,y):
    current_api_url = 'https://pro.openweathermap.org/data/2.5/weather?'
    build_current_api_url = current_api_url + get_location(x,y) + API_SECRET
    current_weather_response = requests.get(build_current_api_url)
    current_weather_data = current_weather_response.json()
    return current_weather_data

"""
this function calls the OpenWeatherAPI for hourly forecast data
"""
def get_hourly_forecast(x,y):
    hourly_api_url = 'https://pro.openweathermap.org/data/2.5/forecast/hourly?'
    build_hourly_api_url = hourly_api_url + get_location(x,y) + API_SECRET
    hourly_weather_response = requests.get(build_hourly_api_url)
    hourly_weather_data = hourly_weather_response.json()
    return hourly_weather_data

"""
this function calls the OpenWeatherAPI for daily forecast data
"""
def get_daily_forecast(x,y):
    daily_api_url = 'https://pro.openweathermap.org/data/2.5/forecast/daily?'
    build_daily_api_url = daily_api_url + get_location(x,y) + API_SECRET
    daily_weather_response = requests.get(build_daily_api_url)
    daily_weather_data = daily_weather_response.json()
    return daily_weather_data

"""
this function calls the OpenWeatherAPI for monthly forecast data
"""
def get_monthly_forecast(x,y):
    monthly_api_url = 'https://pro.openweathermap.org/data/2.5/forecast/climate?'
    build_monthly_api_url = monthly_api_url + get_location(x,y) + API_SECRET
    monthly_weather_response = requests.get(build_monthly_api_url)
    monthly_weather_data = monthly_weather_response.json()
    return monthly_weather_data
