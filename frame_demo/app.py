from appium import webdriver

from frame.base_page import BasePage
from frame.main import Main


# class App(BasePage):
#     def start(self):
#         if self.driver is None:
#             # 第一次调用start（）方法的时候driver 为None
#             caps = {}
#             caps["platformName"] = "android"
#             caps["appPackage"] = "com.xueqiu.android"
#             caps["appActivity"] = ".view.WelcomeActivityAlias"
#             caps["noReset"] = "true"
#             self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
#         else:
#             self.driver.launch_app()
#         self.driver.implicitly_wait(20)
#         return self
#
#     def goto_main(self):
#         return Main(self.driver)
