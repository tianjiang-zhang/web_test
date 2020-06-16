import time
import unittest
from time import sleep
from appium import webdriver
from selenium.webdriver.common.keys import Keys

# @unittest.skip('临时跳过MyTests')
class MyTests(unittest.TestCase):
    # 测试开始前执行的方法
    def setUp(self):
        desired_caps = {'platformName': 'Android', # 平台名称
                        'platformVersion': '5.1.1',  # 系统版本号
                        'deviceName': '127.0.0.1:62001',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'appPackage': 'com.tencent.mm',  # apk的包名
                        'appActivity': 'com.tencent.mm.ui.LauncherUI',  # activity 名称
                        'noReset': 'true',                #不重置应用
                        "chromedriverExecutable": ' chromedriverfilepath',     # chromedriverfilepath的版本需要用在inspect中看到的版本
                        "recreateChromeDriverSessions": 'True',       # recreateChromeDriverSessions 用于自动化配置X5内核驱动
                        "chromeOptions": {"androidProcess": "com.tencent.mm:appbrand0"}  # chromeOptions 提前指定小程序webview的context

                        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
        self.driver.implicitly_wait(8)

    def test_appweix(self):
        """登录微信"""
        self.driver.find_element_by_id('com.tencent.mm:id/r9').click()     #点击搜索图标
        sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/m6').send_keys('相册时光机')       #输入小程序名称
        sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/s6').click()  #com.tencent.mm:id/s6
        sleep(10)
        context = self.driver.contexts  # 此时会有两个webview的context
        self.driver.switch_to.context(context[-1])  # 选取最后一个context进行切换
        minp1 = self.driver.contexts
        print(minp1)
        sleep(5)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("制作我的名片")').click()
        sleep(10)

        #self.driver.find_element_by_class_name('android.view.View').send_keys('自动化测试')
        #self.driver.find_element_by_xpath('//*[@class="android.view.View" and @index="2"]').send_keys('zdh')
        #self.driver.find_element_by_xpath('android.view.View[@class="android.view.View"]').send_keys("zsh")
        #zz =("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View/android.view.View"
        #)
        #self.driver.find_element_by_xpath('zz').send_keys('zdh')
        #self.driver.tap([(252, 994), (816, 1040)])
        #self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View/android.view.View").send_keys('zdh')
        zz = ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View[2]")
        #self.driver.find_element_by_xpath('zz').send_keys('zzz')
        #self.driver.find_element('class_name','android.view.View').send_keys('zzz')
        self.driver.tap([(252, 994), (816, 1040)])
        #self.driver.find_element_by_class_name('zz').set_value("登录账号")
        #calss1 = self.driver.find_element_by_class_name("android.view.View")
        #calss2 = calss1[0].find_element_by_class_name("android.view.View")
        #calss2.send_keys('zzz')
        ca = self.driver.find_elements_by_class_name('android.view.View')
        print('ca')




    # 测试结束后执行的方法
    # def tearDown(self):
    #     self.driver.quit()
























        # keyword= self.driver.find_element_by_xpath('//*[text()="制作我的名片"]').text
        # handle = self.driver.window_handles  # 获取当前页面全部的句柄
        # for i in handle:  # 对全部句柄进行遍历
        #     self.driver.switch_to.window(i)  # 切到到每一个句柄上
        #     if keyword in self.driver.page_source:  # 当某个句柄里面有我们要的关键字时就跳出遍历
        #         break




        # minp = self.driver.contexts
        # print(minp)
        # self.driver.switch_to.window(minp[0])
        # context = self.driver.current_context
        # print(context)







    #  @unittest.skip('临时跳过test_calculator')
    # def test_calculator(self, t=500, n=4):
    #     """计算器测试"""
    #     time.sleep(3)
    #     window = self.driver.get_window_size()
    #     x0 = window['width'] * 0.8  # 起始x坐标
    #     x1 = window['width'] * 0.2  # 终止x坐标
    #     y = window['height'] * 0.5  # y坐标
    #     for i in range(n):
    #         self.driver.swipe(x0, y, x1, y, t)
    #         time.sleep(1)
    #     self.driver.find_element_by_id('com.youdao.calculator:id/guide_button').click()
    #     for i in range(6):
    #         self.driver.find_element_by_accessibility_id('Mathbot Editor').click()
    #         time.sleep(1)
    #
    #     btn_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.view.View/android.widget.GridView/android.widget.FrameLayout[{0}]/android.widget.FrameLayout'
    #     self.driver.find_element_by_xpath(btn_xpath.format(7)).click()
    #     self.driver.find_element_by_xpath(btn_xpath.format(10)).click()
    #     self.driver.find_element_by_xpath(btn_xpath.format(8)).click()
    #     time.sleep(3)