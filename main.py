from rich.console import Console, Group
from rich.panel import Panel
from rich.align import Align
from dotenv import load_dotenv
import os
from functions import *
import time

console = Console()

load_dotenv()
opencage_API_KEY = os.getenv("opencage_API_KEY")
ninjaapi_API_KEY = os.getenv("ninjaapi_API_KEY")

welcome = Panel(Align.center(f"[bold magenta]Search for information about a city."),border_style="bold purple", title="Welcome To City Info")



def main():
    console.print(welcome)
    console.print("[bold red]NOTE: Invalid or N/A city entries might result in wrong information![/]\n")
    while True:
        city = console.input("[bold green]Search any city: [/]")
        with console.status(" ",spinner="simpleDotsScrolling"):
            
            try:
                lat, lon, country = getCoords(API_KEY=opencage_API_KEY,city=city)
                
                cloud_pct, temp, feels_like, humidity, min_temp, max_temp, wind_speed= getData(API_KEY=ninjaapi_API_KEY,latitude=lat, longitude=lon)
                
                dataTable = getDataTable(cloud_pct, temp, feels_like, humidity, min_temp, max_temp, wind_speed, country, city)
                os.system('cls')
                console.print(dataTable)
                
            except Exception as e:
                console.print(f"\n[bold red]An error occured while fetching data: {e}")
            
        clear = console.input("\n[green]Enter to clear ")
        os.system('cls')
    

if __name__ == "__main__":
    main()