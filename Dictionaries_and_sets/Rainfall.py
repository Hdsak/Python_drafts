def get_rainfall():
    rainfall = {}
    while True:
        city_name = input('Enter city name: ')
        if not city_name:
            break
        mm_rain = input('Enter mm rain: ')
        rainfall[city_name] = int(mm_rain) + rainfall.get(city_name, 0)
    for city, rain in rainfall.items():
        print(f'{city}: {rain}')


get_rainfall()