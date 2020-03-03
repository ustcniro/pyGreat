import requests
from bs4 import BeautifulSoup
import time

# 1. 查看首页
r1 = requests.get(  # 返回r1一个非授权的cookie
    url='https://passport.csdn.net/login',
)

print(time.time())
print(str(time.time()*1000)[5:13])

# 2. 提交用户名和密码
r2 = requests.post(
    url='https://passport.csdn.net/v1/register/pc/login/doLogin',
    data={
        'loginType': '1',
        'luserIdentification': 'BBJG_001',
        'pwdOrVerifyCode': 'asd123456789',
        # 'uaToken': "122#sMmgs4xpEEJx/EpZMEpJEJponDJE7SNEEP7rEJ+/f9t/2oQLpo7iEDpWnDEeK51HpyGZp9hBuDEEJFOPpC76EJponDJL7gNpEPXZpJRgu4Ep+FQLpoGUEJLWn4yP7SQEEyuLpEMmEyfU1DnHwStW7kLNxQIZjeaQfPr8nBKHViOewbad40auK39qIw3bRC92e/Etnk/EV2dYNVfZdGe9s2xTaIK0F/Krso9vnc8YFmXrqflIJ0n25M66VOH9rZ/lH5GEc8zcDuiodvFq0LAGYoeLKsygMLoQc7NXfTGEG9VT3wd6ttuYwjEx2hbBb2wVR2boYHVHxw5MiWEhWdKAAtsHVnPEq+71DEPQkSp1uOL9D5aYn5ZkMzEEyBFHqsgPk9Tu8gplul5EELXrGCpik9cAWo3mqWfWEJpanS+ituaHDtVZ85G6JDEERFtDqMfbDEpxnSp1uOIEEL7Z8CLUJ4bEyF3mqW32D5pangL4ul0EDLIL8oL6xNyEyB3maMV5x4bWy+51Z5nPpqPWhwZeugR81PCoo0NJuYeLGP/QfxvYRcpI3HF9Na0iEVfdjmF50H0yfPYI1ut9UFE5KlnCqblQv6RI+w9Z/rjupMsu5Kk9IcWBn4jVYka4LNX1jNXoDlBMCozE8nN459jTxIOUsn1MJQN+IpNhNC6huFcMEu68z30CAxwOiuoZwgmTs0E9nR9inQuBUfhxJySCgnd2+NBSymb8KgQIhWhkkOQAxtChdpojYt7jdG7IUw/5jIt3is3VFaMvytFnSoEAmRj5LxbKYgsSi766OdBCfb8yShV2SeQzx4/WzVL3RN0eNAPd9PXQB8rvEBMLrRnSRFYmZpB0riySBycst5nibTmYd6kwTT9plQERKdCihzJDB1e3eHF1TeC9IGxKdnYW60PcIcarTRb01Ksp+EdAwhpl7RcYcGxsB6N8vb2JuGUE+5Etyxo9pGRPqrv/3mXe08ViceEnEQovIZVfFy3iLty2Az7BB5kQe292FewCostLVgyc2Yc6/s2pFF5DHrkz48JqrogDLi58B5w8avYCrYdPqWRPGCxk7RjonYq2DFvZqEjxEte49i77E6pY4ORkHYvTXLBAyw74prDGEEdXsEKhNxoeye5AYQFeCo7HVRdPfHil6nlrvDuf3Q4WLUpNGFSQkiAYmKHgncgbENiayDuM7fCLMk3BwOFJbO5imP6cmgBj04NgU6PsYZpjmXSHeoqu5vhjtV52WQ3fHGRZ2Vmz9xKD2H8ftBBK++k1XA/9w+E4iF2nCreEQAFz6QfZHuoRjWDx+JlCteNKnDDIlcSoQOZxqA/PIySXaJ7Tp6cxYcAgLJovRNhkOU8ohimpFHDIirw7ZA+hIEHp4jD5Roo9lEepL3O3AsKbUnsd+N/IR0Fp63hVltqfB/spMvsF3Q4sz+HZEEu2ExTmeD2QIFGFpWa9dMSvPM7ziIjdiCA3bYIaiiCTFEjULqgymM/8ZDWi0Y5Mh7CpIC3lU4jb2A2ADGBuU1W1M+xFdKJcuj8sdzJq05JDxccvMOntp1FoKadtnpWXbuZp/MekbCdRgpLOGkILSmZS0Fb2/1HzhTkGfr3eihb6lSEkXZPw4SKgAkhRxx9DLWvutv/2PY9b8F0=",
        # 'webUmidToken': "T65BAEC54ED9AF4D57A83D0578225C3CF450ECA9AE7C35489C7E0055C83"
    },
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
        'origin': 'https://passport.csdn.net',
        'referer': 'https://passport.csdn.net/login',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en;q=0.9,zh-GB;q=0.8,zh;q=0.7,en-US;q=0.6,zh-CN;q=0.5',
        # 'content-length': '1791',
        'content-type': 'application/json;charset=UTF-8',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'x-requested-with': 'XMLHttpRequest',
        # 'x-tingyun-id': 'im-pGljNfnc;r=35872847',
        'x-tingyun-id': 'im-pGljNfnc;r='+str(time.time()*1000)[5:13]
    },
    cookies=r1.cookies.get_dict()  # 带着从r1那里带的cookie去
)
print(r2.text)

# 3. 点赞
# r3 = requests.get(
#     url='https://blog.csdn.net/devil_2009/phoenix/article/digg?ArticleId=38796533',
#     headers={
#         'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
#     },
#     # cookies=r1.cookies.get_dict()
#     cookies=r2.cookies.get_dict()  # 带着从r1那里带的cookie去
# )
# r3.encoding = 'unicode_escape'
# print(r3.text)
