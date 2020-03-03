# 将某用户的CSDN所有博客访问一遍
import requests
from bs4 import BeautifulSoup  # 解析html网页的


def vistapagearticle(link):
    res = requests.get(
        url=link,
    )

    soup = BeautifulSoup(res.text, 'html.parser')

    div = soup.find(name='div', attrs={'class': 'article-list'})
    # find：找到阈值相匹配的第一个标签
    # 案例说通过class进行find是不太好的，因为不同的标签的class值可能是相同，这里我通过查看源码确认了该class值只在这个div才有
    # 通过id寻找是一种比较准确的方式，因为通过id匹配是唯一的

    h4_list = div.find_all(name='h4')
    # find_all：找对与之相匹配的所有标签
    a_list = [h4.find(name='a') for h4 in h4_list]

    for a in a_list:
        link = a.attrs.get('href')

        res2 = requests.get(
            url=link
        )

        # 打印一下进度
        print('\r[', str(a_list.index(a) + 1).rjust(2, ' '), '/', len(a_list), ' ]', end='')
    print()


if __name__ == '__main__':
    for epoch in range(10):
        print('epoch:', epoch, '-------------------------')
        base = 'https://blog.csdn.net/BBJG_001/article/list/'
        pageend = 4     # 博客列表的最终页
        for i in range(1, pageend+1):
            print( str(i), '/', pageend, 'processing . . .')
            url = base + str(i)
            vistapagearticle(url)
