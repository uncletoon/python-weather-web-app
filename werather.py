from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_weather_current(city="New York city"):
     
     request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

     weather_data = requests.get(request_url).json()

     return weather_data


if __name__ == "__main__":
     print('\n***Get Current Weather Conditions***')

     city = input('\nEnter the city: ')

     # CHeck for empty stings or strings with only spaces
     if not bool(city.strip()):
          city = "New York city"

     weather_date = get_weather_current(city)

     print('\n')
     pprint(weather_date)


