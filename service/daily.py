import requests
from datetime import datetime

from config import settings
from schemas import daily_weather_api

class daily():
    def __init__(self):
        ...

    def get_daily_weather_data(self, lat, lon):
        # data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={settings.LATITUDE}&lon={settings.LONGITUDE}&appid={settings.OPENWEATHER_API_KEY}&units=metric&lang=vi')

        mongo_data = daily_weather_api.objects().limit(10).all()
        mongo_data = [mongo_data for i in mongo_data]
        print(mongo_data)

        data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={settings.OPENWEATHER_API_KEY}&units=metric&lang=vi')
        if data.status_code == 200:
            data = data.json()
            weather_location = data["name"]
            weather_status = data["weather"][0]["main"]
            weather_des = data["weather"][0]["description"]
            temp = str(round(data["main"]["temp"]))
            self.save_daily_weather_data(data, "Success")

            return {"Vị Trí": weather_location,"Trạng thái thời tiết": weather_status, "Mô tả": weather_des, "Nhiệt độ": temp +"°C"}
        
        elif 400 <= data.status_code <= 500:
            data = data.json()
            self.save_daily_weather_data(data, "Failed")
            return {"Error code": data["cod"], "Error message": data["message"]}

    def check_daily_weather_data(self):
        ...

    def save_daily_weather_data(self, data, status_message):
        if status_message == "Success":
            daily = daily_weather_api(
                weather_location = data["name"],
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