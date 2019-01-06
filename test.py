from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class SeleniumClass:
    def setUp(self):
        # browser = webdriver.get_property("browser")
        # if browser == "firefox":
        #     self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
        #                                    desired_capabilities=DesiredCapabilities.FIREFOX)
        # elif browser == "chrome":
       driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                                       desired_capabilities=DesiredCapabilities.CHROME)

    # def test_(self):
    #     driver = self.driver
       driver.get("http://nlo.welogix.co/scof/shipments")
       driver.get_screenshot_as_file(
            r"/Users/zhaoliang/PycharmProjects/A/1.png")

    # def tearDown(self):
       driver.quit()


# coding=utf-8
# from selenium import webdriver
#
# chrome_capabilities = {
#     "browserName": "chrome",
#     "version": "",
#     "platform": "ANY",
#     "javascriptEnabled": True,
#     # "marionette": True,
# }
# browser = webdriver.Remote(
#     "http://127.0.0.1:4444/wd/hub", desired_capabilities=chrome_capabilities)
# browser.get("http://www.163.com")
# browser.get_screenshot_as_file(r"Users/zhaoliang/PycharmProjects/A/1.png")
# browser.quit()
