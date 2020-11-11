from django.shortcuts import render
import requests


def index(request):
    appid = '33babf34df7f7a714bc1812bb8445f04'
    city = 'London'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}'
    res = requests.get(url)
    print(res.text)
    return render(request, 'weather/index.html')
