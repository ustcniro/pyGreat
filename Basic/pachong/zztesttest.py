# 1. 查看首页
import requests
from bs4 import BeautifulSoup

# r1 = requests.get(  # 返回r1一个非授权的cookie
#     url='https://passport.csdn.net/login',
# )
#
# soup1 = BeautifulSoup(r1.text, 'html.parser')
# form = soup1.find(name='input')

r2 = requests.get('https://imgconvert.csdnimg.cn/aHR0cHM6Ly96eWRzdG9yZS0xMjU4NDc3NzE0LmNvcy5hcC1iZWlqaW5nLm15cWNsb3VkLmNvbS90eXBvcmEvMjAyMDAyMjMxNTE2MDctMTE5ODQ0LnBuZw?x-oss-process=image/format,png')
savepath = r'data/pictures/test01.png'
with open(savepath, 'wb') as f:  # 因为下载的是图片，所以是wb，以二进制流写入
    f.write(r2.content)
    # ret.text 将结果ret转换成字符串，ret.content直接是二进制文件

