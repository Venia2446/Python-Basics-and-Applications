import requests,re
List = []
X = input()
A = requests.get(X)
print(A.content)
print()
print(A.text)
A_url = re.findall(r'<a\s.*href=[\'\"]?(?:[\w\-]*(?:://))?(\w[\w\.\-_]*)',A.text)
print(A_url)
for x in A_url:
    if x in List:
        None
    else:
        List.append(x)
for m in sorted(List):
    print(m)


