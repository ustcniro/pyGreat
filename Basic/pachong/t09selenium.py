from selenium import webdriver
import time

options = webdriver.ChromeOptions()
# 一些网站能够识别selenium并进行针对性拒绝访问，这里设置options为开发者模式，防止被网站识别出来使用了Selenium
# 我实际用了几次（比如在淘宝和CSDN的登录上）已经没有效果了，应该是反爬机制又升级了
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(
    executable_path=r'D:\Anaconda3\envs\others\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe',
    options=options
)
# 其中executable_path传入的是驱动程序的路径，需要下载，谷歌浏览器可以参见https://blog.csdn.net/weixin_43746433/article/details/95237254
# driver = webdriver.Firefox()

def login(uname, pwd):
    driver.get("http://www.jd.com")
    driver.find_element_by_link_text("你好，请登录").click()
    time.sleep(3)
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_name("loginname").send_keys(uname)
    driver.find_element_by_name("nloginpwd").send_keys(pwd)
    driver.find_element_by_id("loginsubmit").click()
    time.sleep(5)
    driver.get("https://cart.jd.com/cart.action")
    time.sleep(3)
    driver.find_element_by_link_text("去结算").click()
    now = datetime.datetime.now()
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    print('login success')


# buytime = '2016-12-27 22:31:00'
def buy_on_time(buytime):
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            driver.find_element_by_id('order-submit').click()
            time.sleep(3)
            print(now.strftime('%Y-%m-%d %H:%M:%S'))
            print('purchase success')
        time.sleep(0.5)


# entrance
login('178', 'z19')
buy_on_time('2017-01-01 14:00:00')