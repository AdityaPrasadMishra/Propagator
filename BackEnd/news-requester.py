import requests
import json


def save_batch_news(file_name):
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=ac945d7f66d049008e75d39077a32673')
    response = requests.get(url)
    with open(file_name, 'a') as outfile:
        json.dump(response.json(), outfile)

    print(response.json())


# file_name =

with open(file_name, 'r') as my_file:
    print(my_file)



