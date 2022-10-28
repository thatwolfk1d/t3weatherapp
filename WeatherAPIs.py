SECRET = '&appid=c498ab6233adc1ec28ededc44418df6a'


''' this function converts zipcode and country code to lat-lon coordinates
 and returns them to pass them into the next function to construct an api call'''
def get_location_coordinates():
    location_main_url = 'https://api.openweathermap.org/geo/1.0/zip?zip='

    print("View current weather of what location?")
    zip_code = input("Enter ZIP Code: ")
    country_code = input("Enter Country Code(US, CAN, FRA, etc.): ")
    # print(zip_code, country_code)
    weather_location = zip_code + ("&") + country_code
    geolocate_location_url = location_main_url + weather_location + SECRET
    geolocate_response = requests.get(geolocate_location_url)
    geolocate_data = geolocate_response.json()
    # print(geolocate_data)
    lat_cords = format(geolocate_data["lat"], ".2f")
    lon_cords = format(geolocate_data["lon"], ".2f")
    coordinates = "lat=" + str(lat_cords) + "&" + "lon=" + str(lon_cords)
    # print(coordinates)
    return coordinates


"""
this function builds an api call to get weather data and returns that data to
 be passed into the next function to be uploaded to an S3 bucket file
"""
def get_current_weather_data():
    current_weather_main_url = 'https://pro.openweathermap.org/data/2.5/weather?'
    get_current_weather_url = current_weather_main_url + get_location_coordinates() + SECRET
    weather_response = requests.get(get_current_weather_url)
    current_weather_data = weather_response.json()
    # print(get_current_weather_url)
    print(weather_response)
    # print(current_weather_data)
    return current_weather_data