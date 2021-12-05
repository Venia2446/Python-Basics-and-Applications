def Find_Error(errors):
    global glob_Errors
    glob_Errors+=Error_list[errors]
    for err in Error_list[errors]:
        Find_Error(err)
    return glob_Errors
glob_Errors = [] # список родителей
Error_list = {} # граф
Find_List = [] #весь список поиска
Answers = [] # список для ответов
N = int(input())
for numbers in range(0,N):
    Error_1,*Error_2 = input().replace(':',' ').split()
    Error_list[Error_1] = [*Error_2]
X = int(input())
for numbers2 in range(0,X):
    Errors_find = input()
    Find_List+=[Errors_find]
Find_listV2 = [Find_List[0]] #список проверки
for errors in Find_List[1:]:
    glob_Errors = []
    if errors in Find_listV2:
        Answers.append(errors)
    else:
        Find_listV2 += [errors]
        Find_Error(errors)
        for check_errors in Find_listV2:
            if check_errors in glob_Errors:
                Answers.append(errors)
                break
for x in Answers:
    print(x)
