import requests

response = requests.get('https://randomuser.me/api')

gender = response.json()['results'][0]['gender']

first_name = response.json()['results'][0]['name']['first']

title = response.json()['results'][0]['name']['title']

last_name = response.json()['results'][0]['name']['last']

age = response.json()['results'][0]['dob']['age']

phoneNum = response.json()['results'][0]['phone']

pic = response.json()['results'][0]['picture']['large']

nat = response.json()['results'][0]['nat']

time = response.json()['results'][0]['location']['offset']['description']
print(nat)
print(f'{title}. {first_name} {last_name}')
print(f'Photo: {pic}')
print(f'Phone number: {phoneNum}')
print(f'Age: {age}')
print(f'Gender: {gender}')
print(f'time: {time}')