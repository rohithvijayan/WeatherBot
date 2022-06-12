import requests


# def response(text_input):
#     user_mssg=str(text_input).lower()
#     if user_mssg in('hi','hello','sup','hey'):
#         return "Hey,This is Trial Bot here :)"
#     if user_mssg in('what are you doing','what are you doing?','whats up','was up'):
#         return "Having a great day! "
#     if user_mssg in ('time','time?'):
#         now=datetime.now()
#         date_time=now.strftime("%d/%m/%y,%H:%M:%S")
#         return str(date_time)
#     return "Sorry,didnt get you"def response(text_input):
#     user_mssg=str(text_input).lower()
#     if user_mssg in('hi','hello','sup','hey'):
#         return "Hey,This is Trial Bot here :)"
#     if user_mssg in('what are you doing','what are you doing?','whats up','was up'):
#         return "Having a great day! "
#     if user_mssg in ('time','time?'):
#         now=datetime.now()
#         date_time=now.strftime("%d/%m/%y,%H:%M:%S")
#         return str(date_time)
#     return "Sorry,didnt get you"

def weather(city):
    city_name = str(city).capitalize()
    api_key = "a833da2ea0ffccd99997fa69e7cf0f81"
    url = "https://api.openweathermap.org/data/2.5/weather?" + "q=" + city + "&appid=" + api_key
    weather_data = requests.get(url)
    weather_condition = weather_data.json()['weather'][0]['main']
    description = weather_data.json()['weather'][0]['description']
    temp_kelvin = round(weather_data.json()['main']['temp'])
    temp_faren = round(1.8 * (temp_kelvin - 273) + 32)
    temp_min_kelv = round(weather_data.json()['main']['temp_min'])
    temp_min_faren = round(1.8 * (temp_min_kelv - 273) + 32)
    temp_max_kelv = round(weather_data.json()['main']['temp_max'])
    temp_max_faren = round(1.8 * (temp_max_kelv - 273) + 32)
    humidity = weather_data.json()['main']['humidity']
    # print(f'The Weather Conditions In {city_name} Is:')
    # print('-------------------------------------------')
    # print('Weather :' + weather_condition + '--' + description)
    # print('Temperature:' + str(temp) + "°F")
    # print('Minimum Temperature:' + str(temp_min) + '°F')
    # print('Maximum Temperature:' + str(temp_max) + '°F')
    # print('Humidity:' + str(humidity) + '%')
    result = (
                'The Weather Conditions In ' + city_name + '\n' + 'Weather :' + weather_condition + '\n' + 'Temperature:' + str(
            temp_faren) + "°F" + '\n' + 'Minimum Temperature:' + str(temp_min_faren) +
                '°F' + '\n' + 'Maximum Temperature:' + str(temp_max_faren) + '°F' + '\n' + 'Humidity:' + str(
            humidity) + '%')
    print(result)
    return result
