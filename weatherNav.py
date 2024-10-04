import requests
from bs4 import BeautifulSoup

#? enter city name and state
city = input("city name of weather you'd like to check: ").replace(" ","-").lower()
state = input("state: ").lower()

# url for location (weather underground)
url = "https://www.wunderground.com/weather/us/{state}/{city}"

# get and print weather for location
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    currentTemp = soup.find("span",class_="wu-value wu-value-to").text
    print(f"current temperature in {city.title()}, {state.title()}: ",currentTemp + " F")
else:
    print("weather data fetch failed. status code ", response.status_code,".")


#? GET MORE WEATHER DATA :fire::fire::speaking_head::bangbang::explosion:
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # get current temp, low, high, conditions
    currentTemp = soup.find("span", class_="wu-value wu-value-to").text
    highTemp = soup.find("span", class_="hi").text
    lowTemp = soup.find("span", class_="lo").text
    weatherCons = soup.find("div", class_="condition-icon").text

    # print weather data
    print(f"current temperature in {city.title()}, {state.title()}: {currentTemp} F")
    print(f"high temp: {highTemp} F")
    print(f"low temp: {lowTemp} F")
    print(f"weather conditions: {weatherCons}")