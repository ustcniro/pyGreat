import os
from application.findfile.getallsub import getAllSub

path = r'D:\Anaconda3\envs'
dl, fl = getAllSub(path)
ll = dl+fl
print(len(ll))
for il in ll:
    # print(il)
    fname = il.split('\\')[-1]
    # print(fname)
    if 'pyinstaller' in fname:
        print(il)
