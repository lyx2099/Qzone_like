# -*- coding: utf-8 -*-
"""
@Time: 2021/1/21 19:41
@Auth: Jase-lee
@File: login.py
@IDE: PyCharm
@Motto: 更多内容：https://github.com/Jase-lee

"""
from appium import webdriver
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
import datetime

desired_caps = dict()
desired_caps['unicodeKeyboard'] = True      #设置编码格式为unicode
desired_caps['resetKeyboard'] = True        #隐藏手机键盘
# 手机参数
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = '000002b5ce6d93ce'
url = 'http://localhost:4723/wd/hub'
#应用参数
desired_caps['appPackage'] = 'com.tencent.mobileqq'
desired_caps['appActivity'] = 'com.tencent.mobileqq.activity.SplashActivity'    #QQ登录界面
driver = webdriver.Remote(url,desired_caps)      #获取driver
driver.implicitly_wait(15)      #隐式等待

#登录界面同意协议
driver.find_element_by_xpath("//*[@text='同意']").click()

#点击登录按钮
driver.find_element_by_xpath("//*[@text='登录']").click()

#点击账号框并输入账号（todo：参数化，由外部文件读取）
ele = driver.find_element_by_xpath("//*[@text='QQ号/手机号/邮箱']")
ele.click()
ele.send_keys("2733840259")

#点击密码框输入密码（todo：参数化，由外部文件读取）
ele = driver.find_element_by_xpath("//*[@text='输入密码']")
ele.click()
ele.send_keys("leeyx349663.!?qq")

#点击登录按钮
driver.find_element_by_id("com.tencent.mobileqq:id/login").click()

# 权限申请点击【去授权】按钮
ele = driver.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn")
ele.click()

#权限请求点击允许（适用于VIVO）
# driver.find_element_by_xpath("//*[@text='允许']").click()

# #点击权限授权确定按钮（适用于华为pad）
driver.find_element_by_id("android:id/button1").click()


def click_like():
    """点赞"""

    #点击头像
    driver.find_element_by_id("com.tencent.mobileqq:id/ws").click()

    # 向右滑动进入头像界面
    driver.swipe(525,1415,1064,1419,500)

    #获取位置信息点击始终允许
    driver.find_element_by_xpath("//*[@text='始终允许']").click()

    #点击背景墙
    driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/nickname']").click()
    sleep(3)

    #点击赞按钮进入赞排行榜界面
    driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/l0l']").click()

    #点赞（todo:下滑点赞更多人，还未开发完毕）
    '''
    elements = driver.find_elements_by_xpath("//*[@content-desc='赞']")
    print(len(elements))
    print(type(elements))
    #因为第一个已经点赞过了，所以从第二个人开始
    for i in elements[1:]:
        for m in range(9):
            i.click()
            sleep(3)
    '''
    return      #函数执行完跳出当前函数
    #调用点赞方法
click_like()

sleep(3)
#点击左上角返回按钮
driver.find_element_by_id("com.tencent.mobileqq:id/ivTitleBtnLeft").click()
sleep(3)

#使用返回键返回头像的侧边栏界面
driver.back()

#点击左上角的X按钮
driver.find_element_by_id("com.tencent.mobileqq:id/a4a").click()
sleep(3)

def search_sonmeone():
    """
    1.点击首页上方搜索框
    2.输入要对话的人的QQ号
    3.发送键盘按键Enter
    :return:
    """
    driver.find_element_by_xpath("//*[@content-desc='搜索']").click()
    #输入要对话的QQ号
    driver.find_element_by_xpath("//*[@text='搜索']").send_keys("178636612")
    #点击搜索出的联系人所在的box,坐标（686,457）
    TouchAction(driver).tap(x=595,y=477).perform()

search_sonmeone()
pass
# 点击联系人
eles = driver.find_elements_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/j_k']")
# for ele in eles:
#     print(ele)
#     print(type(ele))
#下标为1的代表联系人的id,默认是展开的，点击两次关闭显示所有联系人
for i in range(1):
    eles[1].click()
    sleep(1)

# 通过获取resource-id进行遍历
eles = driver.find_elements_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/icon']")
eles[0].click()

# 进入发消息界面
driver.find_element_by_xpath("//*[@text='发消息']").click()

ele = driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/input']")

start_time = '2021-01-21 23:58:00'
end_time = '2021-01-21 23:58:59'


while True:
# 获取当前系统时间，如果时间是XX:XX:XX:XX，发送指定消息
    curr_time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
    if start_time <= time_str <= end_time:
    # 向输入框输入消息
        ele = driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/input']")
        ele.click()
        ele.send_keys("爱你哦！")
    #点击发送按钮
        driver.find_element_by_xpath("//*[@text='发送']").click()
        break
    elif time_str <= '2021-01-21 23:58:00':
        print("时间还没到")
    else:
        print("时间到了")






# sleep(180)
# driver.quit()

