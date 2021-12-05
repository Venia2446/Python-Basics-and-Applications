from xml.etree import ElementTree



def find_answer(child,level):
    global COLOR_DICT
    level +=1
    COLOR_DICT[child.attrib['color']] += level
    for element in child:
        find_answer(element,level)
COLOR_DICT = {'green':0,'red':0,'blue':0}
tree = ElementTree.fromstring(input())
TOP_CUBE = tree.attrib ['color']
COLOR_DICT[TOP_CUBE] +=1

level = 1
for child in tree:
    level = 1
    find_answer(child,level)

print(COLOR_DICT['red'], COLOR_DICT['green'],COLOR_DICT['blue'])