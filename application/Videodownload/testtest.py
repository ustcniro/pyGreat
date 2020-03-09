from application.Videodownload.getVideo import *

if __name__ == '__main__':
    url = 'https://www.bilibili.com/video/av39240017?from=search&seid=13275619882014314126'
    path = r'E:\Test\others2'

    checkenv()
    download(url, path)

