from mongoengine import connect

mongo_client = connect('openweatherAPI', host='127.0.0.1', port=27017)