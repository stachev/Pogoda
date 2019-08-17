#!/usr/bin/ python

import pyowm

owm = pyowm.OWM('1e25f90d78f5e77120dde7e04d0dd73b',language='ru')
import pyowm

siti='Красный Мак'
# siti=input('Город? :')

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)

observation = owm.weather_at_place(siti)
w = observation.get_weather()
ww=w.get_temperature('celsius')

s=str(w)
print(siti+'\n'+s.split(',')[-1].split('=')[-1].split('>')[0])
# print(ww)
print(ww['temp'])

fc=owm.three_hours_forecast(siti)#на 5 дней
# fc=owm.daily_forecast(siti,limit=6)#на 14 дней
f = fc.get_forecast()
print(f.get_weathers())
