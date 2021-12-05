
def findeparent(parent,child):
    global Found_args
    if child not in graph:
        return Found_args
    if parent == child:
        Found_args+=[parent]
        return Found_args
    Found_args += graph[child]
    for func in graph[child]:
        findeparent(parent,func)# он добаввяет в одни список - надо под каждый новый
    return Found_args
n = int(input())
tree = []
arg_found = []
graph = {}

for z in range(0, n):
    a, *b = input().replace(":", " ").split()
    tree += b
    graph[a] = tree
    tree = []
print(graph)
q = int(input())
for z in range(0, q):
    parent, child = input().split()
    arg_found  += [[parent, child]]
for args in arg_found :
    Found_args = []
    print('Предок_Ребёнок:',args[0],args[1])
    findeparent( parent=args[0], child=args[1])
    print('Список по которому ищем Предка:',Found_args)

    if args[0] in Found_args:
        print('Yes')
    else:
        print('No')
