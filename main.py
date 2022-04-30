import os
from cairosvg import svg2png
import requests
from dotenv import load_dotenv
from time import strftime, localtime
import pytextnow as ptn

load_dotenv()

BASE_PATH = __file__.replace("main.py", "")

RECIPIENT = os.getenv("RECIPIENT")

SID = os.getenv("SID")
USERNAME = os.getenv("PTN_USER")
CSRF = os.getenv("CSRF")
client = ptn.Client(USERNAME, sid_cookie=SID, csrf_cookie=CSRF)

WEATHER_TOKEN = os.getenv("WEATHER")
LAT, LON = os.getenv("LATITUDE"), os.getenv("LONGITUDE")
EXCLUSION = "daily,alerts,minutely"

URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&exclude={EXCLUSION}&appid={WEATHER_TOKEN}&units=imperial"


def createIconPath(icon):
    icon = icon.replace("n", "d")
    return f"{BASE_PATH}assets/icons/{icon}.png"


def getWeather():
    allData = {}

    response = requests.get(URL)
    data = response.json()

    currentResponse = data["current"]

    allData["TEMP0"] = f"{int(currentResponse['temp'])}°F"
    allData["HUMID0"] = f"{currentResponse['humidity']}%"
    allData["ICON0"] = createIconPath(currentResponse["weather"][0]["icon"])
    allData["DESCRIPTION"] = currentResponse["weather"][0]["description"].capitalize()

    for index, hour in enumerate(data["hourly"][:6], start=1):
        time = strftime("%I:%M %p", localtime(hour["dt"]))
        temperature = f"{int(hour['temp'])}°F"
        percipitation = f"{int(hour['pop'] * 100)}%"
        icon = createIconPath(hour["weather"][0]["icon"])

        allData[f"TEMP{index}"] = temperature
        allData[f"ICON{index}"] = icon
        allData[f"TIME{index}"] = time
        allData[f"POP{index}"] = percipitation

    return allData


def createWeatherImage():
    TEMPLATE = f"{BASE_PATH}assets/weatherTemplate.svg"
    data = getWeather()

    with open(TEMPLATE, "r") as file:
        template = file.read()

        for key, value in data.items():
            template = template.replace(key, value)

        svg2png(bytestring=template, write_to=f"{BASE_PATH}output/weatherGraphic.png")


createWeatherImage()
client.send_mms(RECIPIENT, f"{BASE_PATH}output/weatherGraphic.png")