import os
import os.path

F = []
def findpat(current_dir,dirts, files):
    global F
    for local_files in files:
        if local_files[-2] == 'p':
            print('Ссылка на папку: ', current_dir)
            F.append(current_dir)
            return
with open ('find_py_files.txt','w') as text:
    for current_dir,dirts, files in os.walk('main'):
        z = findpat( current_dir,dirts, files)
    print(sorted(F))
    contest = '\n'.join(F)
    text.write(contest)
