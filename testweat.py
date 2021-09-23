import requests, json

s_city = "Kursk,RU"
city_id = 0
ct_tmp = ''
appid = "4f448ad3ded286828f083726579c1007"
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    city_id = data['list'][0]['id']
except Exception as e:
    pass

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    ct_tmp = str(data['main']['temp'])
except Exception as e:
    pass