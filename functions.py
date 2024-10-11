import requests
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()

def getCoords(API_KEY, city):
    base_url = "https://api.opencagedata.com/geocode/v1/json"
    params = {
        'q': f'{city}',
        'key': API_KEY
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    lat = data['results'][0]['geometry']['lat']
    lon = data['results'][0]['geometry']['lng']
    country = data['results'][0]['components']['country']
    return lat, lon, country

def getData(API_KEY, latitude, longitude):
    query = f'lat={latitude}&lon={longitude}'

    api_url_weather = f'https://api.api-ninjas.com/v1/weather?{query}'

    weather_response = requests.get(api_url_weather, headers={'X-Api-Key': API_KEY})
    weather_data = weather_response.json()
    
    cloud_pct = weather_data.get('cloud_pct')
    temp = weather_data.get('temp')
    feels_like = weather_data.get("feels_like")
    humidity = weather_data.get('humidity')
    min_temp = weather_data.get('min_temp')
    max_temp= weather_data.get('max_temp')
    wind_speed = weather_data.get('wind_speed')
    
    return cloud_pct, temp, feels_like, humidity, min_temp, max_temp, wind_speed

def getDataTable(cloud_pct, temp, feels_like, humidity, min_temp, max_temp, wind_speed,country, city):
    dataTable = Table(title=f"[bold]{city.upper()}",title_justify="center")
    dataTable.add_column("Data",style="cyan",no_wrap=True)
    dataTable.add_column("Value",style="green",no_wrap=True)

    dataTable.add_row("Country",country)
    dataTable.add_row("Cloud %",f"{cloud_pct}%")
    dataTable.add_row("Temperature",f"{temp}°C")
    dataTable.add_row("Feels like",f"{feels_like}°C")
    dataTable.add_row("Min temperature", f"{min_temp}°C")
    dataTable.add_row("Max temperature", f"{max_temp}°C")
    dataTable.add_row("Humidity",f"{humidity} g/m^3")
    dataTable.add_row("Wind speed",f"{wind_speed} MPH")
    
    return dataTable    