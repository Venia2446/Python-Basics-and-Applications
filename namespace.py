
def create(namespace, parent):
    global dict
    dict[namespace] = {'parent':parent,'vars':[]}
    return dict
def add(namespace, var):
    global dict
    dict[namespace]['vars'] += [var]
    return dict
def get (namespace, var):
    global dict
    if var in dict[namespace]['vars']:
        return print(namespace)
    elif dict[namespace]['parent'] == 'None':
        return print('None')
    else:
        get(dict[namespace]['parent'],var)
dict = {'global':{'parent':'None','vars':[]}}
n = int(input())
while n not in range(0, 101):
    n = int(input())
for x in range(0, n):
    command, namespace, some = input().split()
    if command == 'create':
        create(namespace, some)
    if command == 'add':
        add(namespace, some)
    if command == 'get':
        get(namespace, some)
