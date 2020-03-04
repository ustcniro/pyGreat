# 1. 查看首页
import requests
from bs4 import BeautifulSoup
import time

testurl = 'https://blog.csdn.net/willow_zhu/article/details/104601533'

def getnum():
    res = requests.get(testurl)
    soup = BeautifulSoup(res.text, 'html.parser')
    numspan = soup.find(name='span', attrs={'class': 'read-count'})
    return int(numspan.text.split()[-1])

ts = time.time()
ns = getnum()
print(ns)
for i in range(100):
    time.sleep(1)
    print('\rthe No.{} test'.format(i+1), end='')
    num = getnum()
    if num != ns:
        print('\n',num)
        te = time.time()
        print('interval time:', te-ts, 's')
        break
