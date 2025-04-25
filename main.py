#1 Предсказание возраста по имени
import requests 

url = "https://api.agify.io/?name=michael"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
print(data)


#2 Определение пола по имени
import requests 

url = "https://api.genderize.io/?name=luc"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
print(data)

#3 Случайная фотография собаки
import requests 

url = "https://dog.ceo/api/breeds/image/random"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
print(data)

