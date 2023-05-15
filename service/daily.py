import requests
from datetime import datetime

from config import settings
from schemas import daily_weather_api

class daily():
    def __init__(self):
        ...

    def get_daily_weather_data(self):
        data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={settings.LATITUDE}&lon={settings.LONGITUDE}.765346&appid={settings.OPENWEATHER_API_KEY}&units=metric&lang=vi')
        print (f'https://api.openweathermap.org/data/2.5/weather?lat={settings.LATITUDE}&lon={settings.LONGITUDE}&appid={settings.OPENWEATHER_API_KEY}&units=metric&lang=vi')
        if data.status_code == 200:
            data.json()
            self.save_daily_weather_data(data, "Success")
            return data
        elif 400 <= data.status_code < 500:
            data.json()
            self.save_daily_weather_data(data, "Failed")
            return data


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