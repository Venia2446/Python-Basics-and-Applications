import requests,re
A = input()
B = input()
def request(A,B):
    A0 = requests.get(A)
    B0 = requests.get(B)
    print('Url 1: ', A)
    print('Url 2:', B)

    #if A0 != '<Response [200]>' or B0 != '<Response [200]>':
        #return 'No'
    A_re = re.findall(r'https://.*html', A0.text)
    B_re = re.findall(r'https://.*html', B0.text)
    print('ссылкa в Url1: ', A_re[0])
    print('ссылкa в Url2: ', B_re[0])

    if A_re[0] == B_re[0]:
        return 'Yes'
    if A_re[0] == B:
        return 'No'
    else:
        return request(*A_re,*B_re)
print(request(A,B))

