import json,requests

with open ('Answer.txt','w') as f:

    while True:
        X = input()
        paremeters = {'number':X,'type':'math'}
        URL = 'http://numbersapi.com/'+paremeters['number']+'/'+paremeters['type']
        Request_URL = requests.get(URL,paremeters,json='true')
        Py_Request = Request_URL.json()
        if Py_Request['found'] == True:
            print('Interesting')
            f.write('Interesting\n')
        elif Py_Request['found'] == False:
            print('Boring')
            f.write('Boring\n')
