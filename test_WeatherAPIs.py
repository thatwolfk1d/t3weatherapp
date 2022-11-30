"""
Author: Matt Wolf
Course: CMSC495
Purpose: This program is a series of assertion tests utilizing unittest framework in python to test API calls to OpenWeatherAPI for Location and Weather Data.
"""

import json
import requests
from unittest import TestCase


API_SECRET = '&appid=c498ab6233adc1ec28ededc44418df6a'


class TestGetLocation(TestCase):

    def test_get_location(self):
        location_api_url = 'https://api.openweathermap.org/geo/1.0/zip?zip='
        zip_code = input("Enter ZIP Code: ")
        country_code = input("Enter Country abbreviation(US, CA, FR etc.): ")
        build_location = zip_code + (",") + country_code
        print(build_location)
        build_geolocation_url = location_api_url + build_location + API_SECRET
        print(build_geolocation_url)
        geolocation_response = requests.get(build_geolocation_url)
        geolocation_data = geolocation_response.json()
        latitude_cords = format(geolocation_data["lat"], ".2f")
        longitude_cords = format(geolocation_data["lon"], ".2f")
        coordinates = "lat=" + str(latitude_cords) + "&" + "lon=" + str(longitude_cords)

        self.assertEqual(build_location, zip_code + (",") + country_code)
        self.assertTrue(country_code.isupper())

        return coordinates

    def test_get_location_city(self):
        location_api_url = 'http://api.openweathermap.org/geo/1.0/direct?q='
        city_code = input("Enter City Name: ")
        country_code = input("Enter Country abbreviation(US, CA, FR, etc.): ")
        build_location = city_code + (",") + country_code
        print(build_location)
        build_geolocation_url = location_api_url + build_location + API_SECRET
        print(build_geolocation_url)
        geolocation_response = requests.get(build_geolocation_url)
        geolocation_data = geolocation_response.json()
        for entry in geolocation_data:
            latitude_cords = format(entry["lat"])
            longitude_cords = format(entry["lon"])
        print(latitude_cords, longitude_cords)
        coordinates = "lat=" + str(latitude_cords) + "&" + "lon=" + str(longitude_cords)

        self.assertEqual(build_location, city_code + (",") + country_code)
        self.assertTrue(country_code.isupper())

        return coordinates

    def test_get_current_forecast(self):
        current_api_url = 'https://pro.openweathermap.org/data/2.5/weather?'
        build_current_api_url = current_api_url + self.test_get_location() + API_SECRET
        current_weather_response = requests.get(build_current_api_url)
        current_weather_data = current_weather_response.json
        print(current_weather_response)
        print(current_weather_data)

        mock_city_json = {'city'}
        expected_city_return = 'name'
        self.assertEqual(current_weather_data(json.dumps(mock_city_json)), expected_city_return)

        return current_weather_data



    def test_get_hourly_forecast(self):
        hourly_api_url = 'https://pro.openweathermap.org/data/2.5/forecast/hourly?'
        build_hourly_api_url = hourly_api_url + self.test_get_location() + API_SECRET
        hourly_weather_response = requests.get(build_hourly_api_url)
        hourly_weather_data = hourly_weather_response.json()
        print(hourly_weather_response)
        print(hourly_weather_data)

        mock_city_json = {'city'}
        expected_city_return = 'name'
        self.assertEqual(hourly_weather_data(json.dumps(mock_city_json)), expected_city_return)

        return hourly_weather_data


    def test_get_daily_forecast(self):
        daily_api_url = 'https://pro.openweathermap.org/data/2.5/forecast/daily?'
        build_daily_api_url = daily_api_url + self.test_get_location() + API_SECRET
        daily_weather_response = requests.get(build_daily_api_url)
        daily_weather_data = daily_weather_response.json()
        print(daily_weather_response)
        print(daily_weather_data)

        mock_city_json = {'city'}
        expected_city_return = 'name'
        self.assertEqual(daily_weather_data(json.dumps(mock_city_json)), expected_city_return)

        return daily_weather_data


    def test_get_monthly_forecast(self):
        monthly_api_url = 'https://pro.openweathermap.org/data/2.5/forecast/climate?'
        build_monthly_api_url = monthly_api_url + self.test_get_location() + API_SECRET
        monthly_weather_response = requests.get(build_monthly_api_url)
        monthly_weather_data = monthly_weather_response.json()
        print(monthly_weather_response)
        print(monthly_weather_data)

        mock_city_json = {'city'}
        expected_city_return = 'name'
        self.assertEqual(monthly_weather_data(json.dumps(mock_city_json)), expected_city_return)

        return monthly_weather_data