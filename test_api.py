from http.client import responses

import requests
import pytest

# сначала нужно установить pip install requests
import json


# def test_api_get_posts():
#     response = requests.get('https://jsonplaceholder.typicode.com/posts')
#     # print(response.text)
#     # print(response.status_code)
#     print(response.headers['Content-Type'])
#     print(response.json()[12]['userId'])
#
#     # Вывод всего header из response из пары ключ:значение
#     # for key, value in response.headers.items():
#     #     print(key, ' => ',  value)
#
#     # проверяем статус код
#     assert response.status_code == 200
#     # Проверяем assert тип одного из полей ззголовка
#     assert type(response.headers['Pragma']) is str, 'Тип не строка'

# _________________________________________________________________________________

# ЭТО ПРО ЗАПРОС С ПАРАМЕТРАМИ

# обычно пишется функция по получению какого-то поля
# def get_user_name():
#     return 'Leanne Graham'
#
#
# n = get_user_name()
# querry = {
#     "id": 1,
#     "name": n,
#     "username": "Bret",
#     "email": "Sincere@april.biz"
# }
#
#
# def test_get_user_for_id():
#     r = requests.get('https://jsonplaceholder.typicode.com/users?', params=querry)
#     print(r.json())

# _________________________________________________________________________________

# АВТОРИЗАЦИЯ
# , cert='path/to/cer.pem
# def test_auth():
#     response = requests.get('https://httpbin.org//basic-auth/user/password', auth=('user', 'password'))
#     print(response.json())
# response test_api.py {'authenticated': True, 'user': 'user'}

# _________________________________________________________________________________

# АВТОРИЗАЦИЯ ПО API KEY
# headers = {'apiKey' : 'special-key'}
#
# json = {
#     "name": 'doggie',
#     "photoUrls": [
#         "https:// cdn2.thedogapi.com"
#     ]
# }
# r = requests.post(url='https://test_swagger/pet', headers=headers,
#                   json=json)
# print(r.json())

# _________________________________________________________________________________
# работа с файлом

# # загружаем через менеджер контекста with открываем в формате rb
# with open(DOG_FILE_PATH, 'rb') as f:
#     files = { 'file': f,
#               'type': 'image/jpeg'}
#
#     file_headers = {'api_key': 'special-key'}
#
#     r_upload = requests.post(url='ddddddd'.format(dog_id),
#                              headers=file_headers,
#                              files=files)
#     print(r_upload.json())

# @pytest.mark.parametrize('lang, id_', [('rus', 12), ('urd', 1)])
# два метода параметризации
# @pytest.mark.parametrize('lang', ['rus', 'urd'])
# @pytest.mark.parametrize('id_', [ 12, 1])
# def test_meow_api (lang, id_):
#     query = {'lang': lang, 'id': id_}
#     r = requests.get('https://meowfacts.herokuapp.com/', params=query)
#     print (r.json())
#     assert r.status_code == 200
#     assert r.json()['data']
# ________________________________________________________________________

# еще пример post запроса

# def test_pos_new_post():
#     headers = {
#         'Content-type': 'application/json; charset = UTF-8'
#     }
#     body = json.dumps({
#         'title': 'foo',
#         "body": 'bar',
#         "userId": 1
#     })
#     response = requests.post('https://jsonplaceholder.typicode.com/posts',
#                              data=body, headers=headers)
#     print(response.json())
#     print(response.headers.items())

# ________________________________________________________________________

# PUT запрос
# def test_update_post():
#     headers = {
#         'Content-type': 'application/json; charset = UTF-8'
#     }
#     body = json.dumps({
#         'title': 'Vladimir',
#         "body": 'bar',
#         "userId": 1
#     })
#     response = requests.put('https://jsonplaceholder.typicode.com/posts/21',
#                              data=body, headers=headers)
#     print(response.json())
# # если нужно обновить какие-то поля, то используем PATCH
# # _______________________________________________________________
#
# #  DELETE запрос
# def test_delete_post():
#     response = requests.delete('https://jsonplaceholder.typicode.com/posts/21')
#     print(response.text)
#     print(response.status_code)