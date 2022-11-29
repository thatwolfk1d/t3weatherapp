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
def get_location():
    location_api_url = 'https://api.openweathermap.org/geo/1.0/zip?zip='
    zip_code = input("Enter ZIP Code: ")
    country_code = input("Enter Country abbreviation(US, CA, FRA etc.): ")
    build_location = zip_code + (",") + country_code
    print(build_location)
    build_geolocation_url = location_api_url + build_location + API_SECRET
    print(build_geolocation_url)
    geolocation_response = requests.get(build_geolocation_url)
    geolocation_data = geolocation_response.json()
    latitude_cords = format(geolocation_data["lat"], ".2f")
    longitude_cords = format(geolocation_data["lon"], ".2f")
    coordinates = "lat=" + str(latitude_cords) + "&" + "lon=" + str(longitude_cords)
    return coordinates

"""
This function is a WIP to get lat lon based on city names instead of postal code
Needs to correctly grab geo data and integrate with other funcitons.
"""
# def get_location_city():
#     location_api_url = 'http://api.openweathermap.org/geo/1.0/direct?q='
#     city_code = input("Enter City Name: ")
#     country_code = input("Enter Country abbreviation(US, CAN, FRA, etc.): ")
#     build_location = city_code + (",") + country_code
#     print(build_location)
#     build_geolocation_url = location_api_url + build_location + API_SECRET
#     print(build_geolocation_url)
#     geolocation_response = requests.get(build_geolocation_url)
#     geolocation_data = geolocation_response.json()
#     latitude_cords = format(geolocation_data["lat"], ".2f")
#     longitude_cords = format(geolocation_data["lon"], ".2f")
#     coordinates = "lat=" + str(latitude_cords) + "&" + "lon=" + str(longitude_cords)
#     return coordinates
"""
this function calls the OpenWeatherAPI for current forecast data
"""
def get_current_forecast():
    current_api_url = 'https://pro.openweathermap.org/data/2.5/weather?'
    build_current_api_url = current_api_url + get_location() + API_SECRET
    current_weather_response = requests.get(build_current_api_url)
    current_weather_data = current_weather_response.json()
    print(current_weather_response)
    print(current_weather_data)
    return current_weather_data

"""
this function calls the OpenWeatherAPI for hourly forecast data
"""
def get_hourly_forecast():
    hourly_api_url = 'https://pro.openweathermap.org/data/2.5/forecast/hourly?'
    build_hourly_api_url = hourly_api_url + get_location() + API_SECRET
    hourly_weather_response = requests.get(build_hourly_api_url)
    hourly_weather_data = hourly_weather_response.json()
    print(hourly_weather_response)
    print(hourly_weather_data)
    return hourly_weather_data

"""
this function calls the OpenWeatherAPI for daily forecast data
"""
def get_daily_forecast():
    daily_api_url = 'https://pro.openweathermap.org/data/2.5/forecast/daily?'
    build_daily_api_url = daily_api_url + get_location() + API_SECRET
    daily_weather_response = requests.get(build_daily_api_url)
    daily_weather_data = daily_weather_response.json()
    print(daily_weather_response)
    print(daily_weather_data)
    return daily_weather_data

"""
this function calls the OpenWeatherAPI for monthly forecast data
"""
def get_monthly_forecast():
    monthly_api_url = 'https://pro.openweathermap.org/data/2.5/forecast/climate?'
    build_monthly_api_url = monthly_api_url + get_location() + API_SECRET
    monthly_weather_response = requests.get(build_monthly_api_url)
    monthly_weather_data = monthly_weather_response.json()
    print(monthly_weather_response)
    print(monthly_weather_data)
    return monthly_weather_data

