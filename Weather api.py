import requests
import credentials
import re
cities = ["London,uk", "Porto,pt", "Paris,fr"]
weather_dict = {}

def city_forecast(city):
  global cities
  response = requests.get(
          "https://community-open-weather-map.p.rapidapi.com/forecast?q="+city,           headers={
          "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
          "X-RapidAPI-Key": "f43cd014bcmsh8f7a59fd093a882p1e64bajsn45c1faa5e9fe"
         },
   )
  return response.json()
  for city in cities:
    weather_dict[city] = city_forecast(city)


def get_day_weather(pred):
  pattern = re.compile("s(?P<hour>dd):dd:dd")
  t = pattern.search(pred['dt_txt'])
  if int(t.group('hour')) >= 10 and int(t.group('hour')) <= 19:    
        return True
  return False
day_weather = {}
for city in weather_dict.keys():
  day_weather[city] = list(filter(get_day_weather, weather_dict[city]['list']))


def travel_estimator(weather_stat):
  estimation = {}

  for city in weather_stat.keys():    
        estimation[city] = {}
        estimation[city]['clear_sky_count'] = 0
        estimation[city]['av_temp'] = 0

        for prediction in day_weather[city]:
          estimation[city]['av_temp'] += prediction['main']['temp']
          if prediction['weather'][0]['description'] in ['clear sky', 'few clouds']:
            estimation[city]['clear_sky_count'] += 1          

        estimation[city]['av_temp'] = round(estimation[city]['av_temp'] / len(day_weather[city]), 2)
        # convert temperature to celsius
        estimation[city]['av_temp_cels'] = round(estimation[city]['av_temp'] - 273.15, 2)

  return estimation

travel_rating = travel_estimator(day_weather)

# sort cities by clear sky forecasts
sorted_travel_rating = sorted(travel_rating.items() ,  key=lambda x: x[1]['av_temp_cels'] )


for city in sorted_travel_rating:
  print(city[0])
  print('Clear sky forecasts:', city[1]['clear_sky_count'])  
  print('Average temperature:', city[1]['av_temp_cels'], "C")
  print('n')