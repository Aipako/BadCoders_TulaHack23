import requests
import json
ё
BASE_PORT = "7122"
BASE_URL = "https://localhost:" + BASE_PORT + "/"


def add_good(user_id, url, price):
    answer = requests.post(BASE_URL + 'Bot/addgood',
                           data={'packedGood': json.dump({'UserId': user_id, 'Url': url, 'Price': price})})
    if answer.status_code == 200:
        return True
    else:
        return False


def delete_good(user_id, url):
    answer = requests.delete(BASE_URL + 'Bot/deletegood',
                           data={'packedGood': json.dump({'UserId': user_id, 'Url': url})})
    if answer.status_code == 200:
        return True
    else:
        return False


def update_good(user_id, url, new_price):
    answer = requests.post(BASE_URL + 'Bot/updategood',
                             data={'userId': user_id, 'url': url, 'newPrice': new_price})
    if answer.status_code == 200:
        return answer.json()
    else:
        return False
    pass


def get_good(user_id):
    answer = requests.get(BASE_URL + 'Bot/getgoods',
                             data={'userId': user_id})
    if answer.status_code == 200:
        return answer.json()
    else:
        return False
    pass

