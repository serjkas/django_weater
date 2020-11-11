from django.shortcuts import render
import requests


def index(request):
    appid = '33babf34df7f7a714bc1812bb8445f04'
    city = 'Vladimir'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={appid}'
    res = requests.get(url).json()
    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }
    print(city_info)
    context = {
        'info': city_info
    }
    return render(request, 'weather/index.html', context)
