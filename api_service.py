import requests

# Appel à l'API pour récupérer la météo
url = "https://home.openweathermap.org/"
key = " "
response = requests.get(url)
weather = response.json()
url1 = url + key
