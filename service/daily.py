import requests
from datetime import datetime

from schemas import daily_weather_api

class daily():
    def __init__(self):
        ...

    def get_daily_weather_data(self):
        # data = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=20.971530&lon=105.765346&appid=6ca743df5e6a3d1d534bdc34ac1b8460&units=metric&lang=vi')
        data = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=20.971530&lon=105.765346&appid=ca743df5e6a3d1d534bdc34ac1b8460&units=metric&lang=vi')
        if data.status_code == 200:
            return data.json(), "Success"
        elif 400 < data.status_code < 500:
            return data.json(), "Failed" 


    def save_daily_weather_data(self, data, status_message):
        if status_message == "Success":
            daily = daily_weather_api(
                weather_time = datetime.fromtimestamp(data["dt"]) if "dt" in data else datetime.now(),
                weather_status = data["weather"][0]["main"],
                weather_des = data["weather"][0]["description"],
                temperature = str(round(data["main"]["temp"])),
                status_code = data["cod"],
                status_message = status_message,
            )
            daily.save()
        else:
            status_message = status_message + ": " + data["message"]
            daily = daily_weather_api(
                status_code = data["cod"],
                status_message = status_message,
            )
            daily.save()

daily_weather = daily()