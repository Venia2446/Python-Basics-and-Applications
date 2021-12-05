import sys, re

for line in sys.stdin:
    line = line.rstrip()
    find_lis = re.findall(r'\b(\w{1})(\w{1})(\w*)\b', line)
    find_lis_2 = re.sub(r'\b(\w{1})(\w{1})(\w*)\b',r'\2\1\3',line)
    print(find_lis_2)