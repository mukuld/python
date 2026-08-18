import requests
url = 'https://api.weather'
data = requests.get(url)
temp = data(json)
city = temp['name']
print(f'{city}: {temp}C')
