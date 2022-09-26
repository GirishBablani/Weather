
from meteostat import Stations, Daily
import pytz
from datetime import datetime,timedelta
import pandas as pd
import time
import numpy as np
import requests
def current_temperature(city):
  
   APi_Key="2ed3a53ba6d040c6a0925be7cfb3bc10"
   response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={APi_Key}")
   result = response.json()
   try:
      sky = result["weather"][0]["main"]
      #print(f"Sky : {sky}")
      temp = result["main"]["temp"]
      celsius = round(temp - 273)
      Centrigrate = u"\u2103"
      #print(f"Temperature : {celsius} {Centrigrate}")
      feels_temp = result["main"]["feels_like"]
      celsius_feel = round(feels_temp - 273)
      #print(f"Feels_Like : {celsius_feel} {Centrigrate}")
      min_temp = result["main"]["temp_min"]
      celsius_min = round(min_temp - 273) 
      #print(f"Min : {celsius_min} {Centrigrate}")  
      max_temp = result["main"]["temp_max"]
      celsius_max = round(max_temp - 273 )
      #print(f"Max : {celsius_max} {Centrigrate}") 
      i_pressure = result["main"]["pressure"]
      pressure = round(i_pressure)
      #print(f"Pressure : {pressure} mb") 
      humidity = result["main"]["humidity"]
      #print(f"Humidity : {humidity} % ")
      Visibility = result['visibility']
      Visibility_km = Visibility/1000
      #print(f"Visibility : {Visibility_km} Km")  
      Wind_Speed = round(result["wind"]["speed"]*3.6)
      #print(f"Wind Speed : {Wind_Speed} km/hr") 
      Sunrise = result["sys"]['sunrise']
      readable_1 = time.ctime(Sunrise)
      #print(f"Sunrise : {readable_1}")
      Sunset = result["sys"]['sunset']
      readable_2 = time.ctime(Sunset)
      #print(f"Sunset : {readable_2}")
      lat = result["coord"]["lat"]
      lon = result["coord"]["lon"]
      return sky,celsius,celsius_feel,celsius_min,celsius_max,pressure,humidity,Visibility_km,Wind_Speed,readable_1,readable_2,lat,lon
   except:
      err = "Please Check the Name of City"
      return err

def forecast_temp(city):
   
  
   response=requests.get(f"https://weatherdbi.herokuapp.com/data/weather/{city}")
   result = response.json()
   try:
      current_image = result["currentConditions"]["iconURL"]
   #return current_image,result
      date=[]
      day=[]
      comment=[]
      max_temp=[]
      min_temp=[]
      icon=[]
      region=result["region"]

      for i in result["next_days"]:
      
       day.append(i["day"])
       comment.append(i["comment"])
       max_temp.append(i["max_temp"]["c"])
       min_temp.append(i["min_temp"]["c"])
       icon.append(i["iconURL"])
       
      return current_image,day,comment,max_temp,min_temp,icon,region
   except:
      return(False)  
def date():

   IST = pytz.timezone('Asia/Kolkata')
   datetime_ist = datetime.now(IST)
   new_date=[]
   for i in range(1,9):
      u_date=datetime_ist+timedelta(days=i)
      new_date.append(u_date.strftime('%Y:%m:%d'))
   return new_date   
def historical_data(lat,lon):

      current_date = datetime.now()
      month_before = datetime.now()-timedelta(days=30) 
      stations = Stations()
      stations = stations.nearby(lat ,lon)
      station = stations.fetch(1)
      data = Daily(station, start = datetime(month_before.year,month_before.month,month_before.day), end =datetime(current_date.year,current_date.month,current_date.day))

# Fetch Pandas DataFrame
      data = data.fetch()
      return data
