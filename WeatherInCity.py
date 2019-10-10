import datetime
from FileModule import *
import pyowm

owm = pyowm.OWM('c086658c258da275f0b67500bd7fc58d', language= 'ru')
place = input('Введите город: ')
observation = owm.weather_at_place(place)       # определение города

w = observation.get_weather()

TempNow = w.get_temperature('celsius')['temp']
print('В городе ', place, 'сейчас', round(TempNow),'градусов цельсия')
print('Погодные условия: ', w.get_detailed_status())        # получение погодных условий

if w.get_detailed_status() == 'дождь':
    print('Лучше взять зонтик')
elif w.get_detailed_status() == 'ясно':
    print('отличная погода')
else:
    print('ну такое на улице')      # написание совета

now = datetime.datetime.now()
log = str('В городе ' + place + ' сейчас ' + str(round(TempNow)) + ' градусов цельсия  ' + 'дата: ' + str(now.strftime("%d-%m-%Y %H:%M")) + '\n')
file(log)       # запись лога в файл

input('tap to exit')
