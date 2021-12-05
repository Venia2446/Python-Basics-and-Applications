'''
def f(родитель):
    for дитя in dict(родитель)
        список += dict(дитя)
        f(дитя)'''





import json
from operator import itemgetter, attrgetter, methodcaller
def find_fathers(parent):
    global All_list

    if parent not in NEW_DICT_2:

        return
    else:
        All_list += NEW_DICT_2[parent]
        for child in NEW_DICT_2[parent]:
            if child in NEW_DICT_2:
                All_list  += NEW_DICT_2[child]
                find_fathers(child)
        return



List = inp_json = [  # тестовый граф наследования в виде json-объекта
    {'name': 'G', 'parents': ['F']},  # сначала отнаследуем от F, потом его объявим: корректный алгоритм все равно правильно обойдёт граф, независимо что было раньше: наследование или объявление
    {'name': 'A', 'parents': []},
    {'name': 'B', 'parents': ['A']},
    {'name': 'C', 'parents': ['A']},
    {'name': 'D', 'parents': ['B', 'C']},
    {'name': 'E', 'parents': ['D']},
    {'name': 'F', 'parents': ['D']},
    # а теперь другая ветка наследования
    {'name': 'X', 'parents': []},
    {'name': 'Y', 'parents': ['X', 'A']},  # свяжем две ветки наследования для проверки, обошла ли рекурсия предков Z и предков Y в поисках A
    {'name': 'Z', 'parents': ['X']},
    {'name': 'V', 'parents': ['Z', 'Y']},
    {'name': 'W', 'parents': ['V']},
]
'''List = (json.loads(List))
print(List)'''
NEW_DICT = {}
Find_list = []
All_list = []
NEW_DICT_2 = {}
ANSWER_LIST = []
for dicts in List:
    NEW_DICT[dicts['name']] = dicts['parents']
    Find_list += [dicts['name']]

print(NEW_DICT)

for key,items in NEW_DICT.items():
    for values in items:

        if values in NEW_DICT_2:
            NEW_DICT_2[values] += [key]
        else:
            NEW_DICT_2[values] = [key]

print(Find_list)
print(NEW_DICT_2)
for parents in Find_list:
    All_list = []
    find_fathers(parents)
    ANSWER_LIST += [[parents,len(set(All_list))+1]]
ANSWER_LIST = sorted((ANSWER_LIST),key = itemgetter(0))
print(ANSWER_LIST)
for answ in ANSWER_LIST:
    print(answ[0],' : ',answ[1])