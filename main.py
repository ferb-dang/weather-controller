from mongoengine import *
from fastapi import FastAPI

from connection import mongo_client

from service import daily_weather

app = FastAPI()
mongo_client

@app.get("/daily_weather")
async def current_weather(lat="20.96836087786231", lon="107.08350722470679"):
    # 20.96836087786231, 107.08350722470679
    data = daily_weather.get_daily_weather_data(lat, lon)
    # Check data

    return data


'''
kiểm tra data lấy ra xem có cũ không
1, Lấy trong ngày hôm nay
2, Cách nhau quá 3 tiếng

Model database
1, Thêm 

Thêm địa điểm ưa thích cho ng dùng

Kiểm tra thời gian querry lấy data -> đưa ra quyết định có request không
1, Check data base sử dụng trường thời gian so sánh với thời gian hiện tại
    - Record chưa quá 15p so với thời gian hiện tại -> lấy record cũ
    - record quá 15p -> request mới
2, làm cronjob get data mỗi 1 giờ
'''