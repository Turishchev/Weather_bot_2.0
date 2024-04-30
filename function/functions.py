from aiogram import Router
from requests import get

router = Router()

# функция расчета облачности
def clouds_func(percent):
    if percent == 0:
        return 'Безоблачно'
    elif 70 >= percent >= 20:
        return 'Незначительная облачность'
    elif 70 > percent > 20:
        return 'Облачно'
    else:
        return 'Ну прям очень облачно'


def weather(city):

    url = (
            'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid=fe1b8f738102bf5f18812e7309663d05')

    weather_data = get(url).json()
    code_weather = weather_data['cod']
    global town
    town = weather_data['name']
    if code_weather != 200:
        return 'Error'
    else:
        temp = round(weather_data['main']['temp'])
        temp_feels = round(weather_data['main']['feels_like'])
        pressure_weather = round(weather_data['main']['pressure'] * 0.7506)
        clouds = clouds_func(weather_data['clouds']['all'])

        return (f' Температура воздуха:  {temp}\n'
                f' Как ощущается:  {temp_feels}\n'
                f' Давление: {pressure_weather} мм.р.ст\n'
                f' Облачность: {clouds}')












