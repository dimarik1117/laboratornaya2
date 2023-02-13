import requests

city = 'Moscow,RU'
appid = '33344c7d0773f4f21362c8f74a8a665b'

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q':city,'units':'metric','lang':'ru','APPID':appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']),
          "> \r\nПогодные условия <", i['weather'][0]['description'], ">")
    print("Скорость ветра <", i['wind']['speed'], "> \r\nВидимость <", i['visibility'], ">")
    print("____________________________")
