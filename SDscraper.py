import requests
from bs4 import BeautifulSoup

# url of weather underground location:
url = "https://www.wunderground.com/weather/us/oh/youngstown"

# send http request to fetch html content of the page:
response = requests.get(url)

# INITIALIZE BEAUTIFULSOUP :fire::fire::explosion:
soup = BeautifulSoup(response.text, "html.parser")

# print status code
print(f"status code: {response.status_code}")
# print parsed html (optimal to use for page structure !!!)
#! print(soup.prettify())

#* temperatureElement = soup.find("span", class_="wu-value wu-value-to")
temperatureElement = soup.find_all("span", class_="wu-value wu-value-to")
#* temperature = temperatureElement.text if temperatureElement else "N/A"
for element in temperatureElement:
    print(element.text)

# print(f"current temp: {temperature}")
