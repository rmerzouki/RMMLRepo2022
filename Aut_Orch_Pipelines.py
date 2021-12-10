import os
# For dealing with json responses we receive from the API
from dotenv import load_dotenv
import requests

load_dotenv()

def extract() -> dict:
    
    key=os.getenv('appid')
    
    """Use the Open Weather Map API to fetch Paris weather data.
    Returns:
        dict: a JSON response of many wheather measurements.
    """
    url = "https://api.openweathermap.org/data/2.5/weather"

    # TODO: Use a real API key. You can get a free one from https://openweathermap.org/
    response = requests.request(
    "GET", url, params={"q": "Paris", "appid": key}
    )
    return response.json()

def transform(response: dict) -> float:
    """Process the response and extract windspeed information
    Args:
        response (dict): Response JSON from extract task
    Returns:
        float: current wind speed
    """
    return response.get("wind", {}).get("speed", 0.0)

def load(speed: float):
    """Append data to file
    Args:
        speed (float): Windspeed from transform task
    """
    #'a' open for writing, appending to the end of the file if it exists
    with open("windspeed.txt", "a") as f:
        f.write(str(speed) + "\n")

if __name__ == "__main__":
# Execute tasks in the right order.
    response = extract()
    windspeed = transform(response)
    load(windspeed)