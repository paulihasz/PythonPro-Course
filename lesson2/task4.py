def is_nice_weather(temp: int, rain: bool) -> bool:
    if  15 <= temp <= 25 and not rain:
        return True
    else:
        return False
    
weather_data = [
    {'temp': 12, 'rain': False},
    {'temp': 15, 'rain': False},
    {'temp': 14, 'rain': True},
    {'temp': 18, 'rain': False},
    {'temp': 20, 'rain': True},
    {'temp': 19, 'rain': False},
    {'temp': 24, 'rain': False},
    {'temp': 21, 'rain': True},
    {'temp': 18, 'rain': True},
    {'temp': 17, 'rain': False},
    {'temp': 24, 'rain': False},
]

nice_weather = []

for i in range(len(weather_data)):
    if is_nice_weather(weather_data[i]['temp'], weather_data[i]['rain']):
        nice_weather.append(weather_data[i])
print(nice_weather)