import requests
import json
from rcviz import CallGraph,viz
cg = CallGraph(filename="fibo.png")



with open ('Answer2.txt','w') as TEXT:
    client_id = '03edc5dff51bc6ec568f'
    client_secret = 'a5be55e822b981e4a752fbbd02858fb7'
    # инициируем запрос на получение токена
    r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                      data={
                          "client_id": client_id,
                          "client_secret": client_secret
                      })

    # разбираем ответ сервера
    j = json.loads(r.text)

    # достаем токен
    token = j["token"]
    # создаем заголовок, содержащий наш токен
    headers = {"X-Xapp-Token" : token}
    # инициируем запрос с заголовком

    #имени художника и годе рождения.
    AUTORS_LIST = []
    try:
        while True:
            ID = input()
            r = requests.get("https://api.artsy.net/api/artists/"+ID, headers=headers)

            # разбираем ответ сервера
            j = json.loads(r.text)
            print(j)
            AUTORS_LIST += [[j['sortable_name'],j['birthday']]]
    except:
        print(AUTORS_LIST)


from PIL import Image
Image.open('./fibo.png').show()