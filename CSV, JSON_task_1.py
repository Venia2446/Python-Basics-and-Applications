import csv
from operator import itemgetter, attrgetter, methodcaller
Type = []
Dict = {}
Q = []
with open ('Crimes.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        if '2015' in row[2]:
            Type +=[row[5]]
        for crimes in Type:
            if crimes in Dict:
                Dict[crimes] +=1
            else:
                Dict[crimes] = 0
    for key in Dict:
        Q += [[key,Dict[key]]]
    Q = sorted(Q,key = itemgetter(1))
    print(Dict)
    print(Q)



    print('Ответ: ',Q[len(Q)-1][0])
