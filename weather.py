import os
import requests
#72997
key = os.environ.get('API_KEY')

cities = ["Cairo", "Nairobi", "Lagos", "Pretoria", "Addis Ababa", "Rabat", "Accra", "Algiers", "Luanda", "Dakar"]

for city in cities:
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    
    
    response = requests.get(url)
    data = response.json()
    
    
    if response.status_code == 200:
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        clouds = data['clouds']['all']
        
    
        print(f"City: {city} | Weather: {description} | Temp: {temp}C | Clouds: {clouds}%")
    else:
        print(f"Error for {city}: {data['message']}")