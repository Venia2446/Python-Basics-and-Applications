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
List = input()
List = (json.loads(List))
NEW_DICT = {}
Find_list = []
All_list = []
NEW_DICT_2 = {}
ANSWER_LIST = []
for dicts in List:
    NEW_DICT[dicts['name']] = dicts['parents']
    Find_list += [dicts['name']]
for key,items in NEW_DICT.items():
    for values in items:

        if values in NEW_DICT_2:
            NEW_DICT_2[values] += [key]
        else:
            NEW_DICT_2[values] = [key]
for parents in Find_list:
    All_list = []
    find_fathers(parents)
    ANSWER_LIST += [[parents,len(set(All_list))+1]]
ANSWER_LIST = sorted((ANSWER_LIST),key = itemgetter(0))
for answ in ANSWER_LIST:
    print(answ[0],':',answ[1])