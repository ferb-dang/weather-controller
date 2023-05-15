from mongoengine import *

class daily_weather_api(Document):
    _id = ObjectIdField()
    weather_location = StringField()
    weather_time = DateTimeField()
    weather_status = StringField()
    weather_des = StringField()
    temperature = StringField()
    status_code =  IntField()
    status_message = StringField()
    exception_message = StringField()
    meta = {"collection": "dailyWeather"}