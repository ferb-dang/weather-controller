from mongoengine import *
from fastapi import FastAPI

from connection import mongo_client

from service import daily_weather

app = FastAPI()
mongo_client

@app.get("/Thời tiết hiện tại")
async def root():
    
    data, status_message = daily_weather.get_daily_weather_data()
    #check data 
    daily_weather.save_daily_weather_data(data, status_message)

    weather_status = data["weather"][0]["main"]
    weather_des = data["weather"][0]["description"]
    temp = str(round(data["main"]["temp"]))

    return {"Trạng thái thời tiết": weather_status, "Mô tả": weather_des, "Nhiệt độ": temp +"°C"}

# @app.get("/Thời tiết hiện tại")

'''
Giới hạn request mỗi ngày
1, Exception status code
2, mỗi phút 1 request 

kiểm tra data lấy ra xem có cũ không
1, Lấy trong ngày hôm nay
2, Cách nhau quá 3 tiếng

Model database
1, Thêm 
'''