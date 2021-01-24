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
desired_caps['deviceName'] = 'anyone'
url = 'http://localhost:4723/wd/hub'
#应用参数
desired_caps['appPackage'] = 'com.tencent.mobileqq'
desired_caps['appActivity'] = 'com.tencent.mobileqq.activity.SplashActivity'    #QQ登录界面
driver = webdriver.Remote(url,desired_caps)      #获取driver
driver.implicitly_wait(15)      #隐式等待

# 登录账号密码
datas={}
datas['login_usr'] = "登录的QQ号"
datas['passwd'] = "登录的密码"
datas['searched_qq_number'] = {
    'first':'在此输入想要查找的QQ号',
    'second':'在此输入想要查找的QQ号',
    'third':'在此输入想要查找的QQ号',
    'forth':'在此输入想要查找的QQ号',
    'fifth':'在此输入想要查找的QQ号'
    ''
}
chat_mesage = {}
chat_mesage["问候语"]="你好！"
chat_mesage["段子"]= {
    "段子0":"有的女孩真的很讲道理的，只要你道歉态度诚恳，哪怕你根本就没错，她们也会原谅你的。",
    "段子1":"所有人都关心你飞的高不高 累不累 只有我不一样 我不关心你。"
}


def login():
    """
    1.登录
    :return:
    """
    # 登录界面同意协议
    driver.find_element_by_xpath("//*[@text='同意']").click()

    # 点击登录按钮
    driver.find_element_by_xpath("//*[@text='登录']").click()

    # 点击账号框并输入账号（todo：参数化，由外部文件读取）
    ele = driver.find_element_by_xpath("//*[@text='QQ号/手机号/邮箱']")
    ele.click()
    ele.send_keys(datas['login_usr'])
    sleep(2)

    # 点击密码框输入密码（todo：参数化，由外部文件读取）
    ele = driver.find_element_by_xpath("//*[@text='输入密码']")
    ele.click()
    ele.send_keys(datas['passwd'])

    # 点击登录按钮
    driver.find_element_by_id("com.tencent.mobileqq:id/login").click()

    # 权限申请点击【去授权】按钮
    driver.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn").click()

    # 权限请求点击允许（适用于VIVO）
    # driver.find_element_by_xpath("//*[@text='允许']").click()
    # #点击权限授权确定按钮（适用于华为pad）
    driver.find_element_by_id("android:id/button1").click()
    return

login()

class EnterIntoChatPage():

    """
    1.进入聊天界面
    2.发送消息
    3.定时发送消息
    """
    def __init__(self, searched_qq_number, message, start_time='', end_time='', ontime_message=''):
        """
        :param searched_qq_number: 被查找的QQ号码
        :param message: 要发送的消息
        :param start_time: 定时发送消息模式开始时间，默认为空
        :param end_time: 定时发送消息模式截止时间，默认为空
        :param ontime_message: 定时发送消息内容，默认为空
        """
        self.searched_qq_number = searched_qq_number
        self.message = message
        self.start_time = start_time
        self.end_time = end_time
        self.ontime_message = ontime_message

    def enter_chat_page(self):
        """
        1.进入聊天界面
        :return:
        """
        # 1.找到搜索框并进行点击
        driver.find_element_by_xpath("//*[@content-desc='搜索']").click()

        # 2.向搜索框中输入要查找的QQ号(todo:datas['searched_qq_number']['first']first需要修改)
        # driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/et_search_keyword']").send_keys(self.searched_qq_number)
        driver.find_element_by_id("com.tencent.mobileqq:id/et_search_keyword").send_keys(self.searched_qq_number)
        sleep(2)
        # 3.点击搜索出联系人进入聊天界面
        driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/image']").click()

    def send_message(self):
        """
        1.发送信息
        """
        # 1.点击聊天界面消息输入框并将消息输入输入框
        ele = driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/input']")
        ele.click()
        # TODO:交互实现实时对话
        for i in range(1):  #range(1)默认为1，小黑屋模式可指定对应数字
            ele.send_keys(message)

            # 2.点击发送消息按钮
            driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/fun_btn']").click()

    def send_message_on_time(self):
        """
        用于定时发送消息
        """
        while True:
            # 获取当前系统时间，如果时间是2021-01-23 13:00:00，发送指定消息
            curr_time = datetime.datetime.now()
            time_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
            if self.start_time <= time_str <= self.end_time:
                # 向输入框输入消息
                ele = driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/input']")
                ele.click()
                ele.send_keys("定时发送消息测试，当前时间是 "+ time_str + "要发送的消息是：" + self.ontime_message)
                # 点击发送按钮
                driver.find_element_by_xpath("//*[@text='发送']").click()
                break
            elif time_str <= self.start_time:
                pass
            else:
                pass

#---------------以下是对EnterIntoChatPage()类的测试---------------
searched_qq_number = datas['searched_qq_number']['second']
message = chat_mesage["段子"]["段子0"]
start_time='2021-01-23 13:33:00'
end_time='2021-01-23 13:33:59'
ontime_message='你好'

# action = EnterIntoChatPage(searched_qq_number, message,start_time,end_time,ontime_message)
# action.enter_chat_page()
# action.send_message()
# action.send_message_on_time()
# action.enter_personal_data_page()

#---------------------------------------------------------------

class EnetrQzone():
    """
    用于进入个人信息展示页面进行点赞和进入QQ空间
    1.首先进入个人信息展示页面
    2.点赞
    3.进入QQ空间
    """
    def __int__(self):
        """"""

    def enter_personal_data_page(self):
        """
        1.在聊天界面点击右上角【聊天设置】按钮
        2.点击个人头像和昵称一栏进入个人信息展示界面
        3.进入个人信息展示页面
        """
        #1.调用EnterIntoChatPage()类的enter_chat_page()方法进入聊天界面
        EnterIntoChatPage(searched_qq_number, message,start_time,end_time,ontime_message).enter_chat_page()

        #2.点击在聊天界面点击右上角【聊天设置】按钮
        driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/ivTitleBtnRightImage']").click()

        #3.点击个人头像和昵称一栏进入个人信息展示界面
        driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/clv']").click()
        sleep(5)

    def give_like(self):
        """
        点赞
        TODO:赞显示为花样赞时，无法进行点赞
        """
        pass

    def qzone_like(self):
        """
        1.对个人QQ空间进行点赞
        2.通过对话框界面进入，调用send_message函数
        :return:
        """
        # 1.点击进入空间的按钮(进行判断，若已经开通了小世界，则第二个入口为QQ空间，否则为第一个)
        elements = driver.find_elements_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/dkv']")
        elements[0].click()

        #2.判断空间是否是禁止访问的状态
        '''
        if driver.find_element_by_xpath("//*[@text='主人设置了权限']"):
            print("主人设置了权限")
            # 发送返回键模拟手机返回按钮
            driver.press_keycode(4)
        else:
            pass
        '''

        # 首次进入空间需要滑动一段距离，以防点赞按钮加赞不处理来
        # sleep(3)
        origin_ele = driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/c53']")
        destination_ele = driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/hto']")
        driver.drag_and_drop(origin_ele, destination_ele)

        # 先找昵称和说说发表时间所在的方框，进行遍历
        while True:
            elements = driver.find_elements_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/c7p']")
            print("Current page click_like_button number is：" + str(len(elements)))

            # if current page click_lkie_button number is one,click it one times
            if len(elements) == 1:
                elements[0].click()
                # pass

            # if current page click_like_button number >=2，the button is iterated over
            elif len(elements) >= 2:
                elements[1].click()
                    # pass

            print("------------点赞一轮结束---------------")
            origin_eles = driver.find_elements_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/c7y']")
            destination_eles = driver.find_elements_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/c4r']")
            print("Current page origin_eles numbers：" + str(len(origin_eles)))
            print("Current page destination_eles numbers：" + str(len(destination_eles)))

            # if current page only have one origin_eles and one destination_eles,direct use of
            if len(origin_eles) == 1 and len(destination_eles) == 1:
                    driver.drag_and_drop(origin_eles[0],destination_eles[0])

            # if current page have two desttination_eles and one origin_eles,than Slide from the destination_eles[1] to the destination_eles[1]
            elif len(destination_eles) == 2 and len(origin_eles) == 1:
                driver.drag_and_drop(destination_eles[1],destination_eles[0])

            # if current page have two desttination_eles and one origin_eles,than Slide from the origin_eles[1] to the origin_eles[0]
            elif len(origin_eles) == 2 and len(destination_eles) == 1:
                driver.drag_and_drop(origin_eles[1],origin_eles[0])

            # 如果当前页面有2个滑动起点和2个滑动终点，那么从第2个滑动终点滑动到第1个滑动终点
            elif len(origin_eles) == 2 and len(destination_eles) == 2:
                driver.drag_and_drop(destination_eles[1],destination_eles[0])

            # 如果当前界面有1个滑动起点和0个滑动终点
            elif len(origin_eles) == 1 and len(destination_eles) == 0:
                origin_ele = driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/c4r']")
                destination_ele = driver.find_element_by_xpath("//*[@resource-id='com.tencent.mobileqq:id/c7y']")
                driver.drag_and_drop(origin_ele, destination_ele)

            # 如果当前界面有1个滑动终点和0个滑动起点
            elif len(destination_eles) == 1 and len(origin_eles) == 0:
                pass

#---------------以下是对EnetrQzone(EnterIntoChatPage)类的测试---------------

action = EnetrQzone()
action.enter_personal_data_page()
action.qzone_like()
#---------------------------------------------------------------


