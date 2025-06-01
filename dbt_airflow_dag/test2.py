import requests
import json
from pandas import json_normalize


api_url = "https://randomuser.me/api/"

response = requests.get(api_url)

data = response.json()

user = data['results'][0]

processed_user = json_normalize({
        'firstname': user['name']['first'],
        'lastname': user['name']['last'],
        'country': user['location']['country'],
        'username': user['login']['username'],
        'password': user['login']['password'],
        'email': user['email']})

print(response.text)
print(processed_user)



