# import requests
# import json
# from pandas import json_normalize


# api_url = "https://randomuser.me/api/"

# response = requests.get(api_url)

# data = response.json()

# user = data['results'][0]

# processed_user = json_normalize({
#         'firstname': user['name']['first'],
#         'lastname': user['name']['last'],
#         'country': user['location']['country'],
#         'username': user['login']['username'],
#         'password': user['login']['password'],
#         'email': user['email']})

# print(response.text)
# print(processed_user)

list1 = [1, 2, 3, 4]
list2 = [6, 7, 8, 9]

def add_lists(list1, list2):
        list = [
                
                ((abs(list1[i]-list2[i])) ** 2) for i in range(0, len(list1))
        ]
        # for i in range(0, len(list1)):
        #         result = ((abs(list1[i]-list2[i])) ** 2)
        #         list.append(result)
                
        result2 = sum(list)/len(list)
        return print(result2)

add_lists(list1, list2)



