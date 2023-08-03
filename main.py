import eel
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs

appid='5c9d045ef7fdb219b9a14a13959904ac'


@eel.expose
def get_temp(City):
    City = str(City)
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={City}&appid={appid}&units=metric').json()
    temp = r['main']['temp']
    temp = int(temp)+1
    return "Температура в " + City + " " + str(temp)

eel.init("web")
eel.start("index.html", size = (500, 500))
