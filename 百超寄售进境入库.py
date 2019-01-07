# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import warnings


# def ignore_warnings(test_func):
#     def do_test(self, *args, **kwargs):
#         with warnings.catch_warnings():
#             warnings.simplefilter("ignore", ResourceWarning)
#             test_func(self, *args, **kwargs)
#     return do_test


class Costmn_I(unittest.TestCase):

    def setUp(self):
        warnings.filterwarnings("ignore", category=ResourceWarning)
        # self.driver = webdriver.Chrome()
        # chrome_capabilities = {
        #     "browserName": "chrome",
        #     "version": "",
        #     "platform": "ANY",
        #     "javascriptEnabled": True,
        #     # "marionette": True,
        # }
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        # self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_(self):
        driver = self.driver
        driver.get("http://nlo.welogix.co/login")
        sleep(2)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='数字化跨境供应链云平台'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='数字化跨境供应链云平台'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='数字化跨境供应链云平台'])[1]/following::input[1]").send_keys(
            "welogix2")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='数字化跨境供应链云平台'])[1]/following::input[2]").clear()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='数字化跨境供应链云平台'])[1]/following::input[2]").send_keys(
            "123456")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='忘记密码?'])[1]/following::button[1]").click()
        driver.find_element_by_link_text(u"订单中心").click()

        driver.find_element_by_xpath(
            "//body/div[@id='mount']/div[@class='welo-layout-wrapper ant-layout']/div[@class='ant-layout-wrapper ant-layout ant-layout-has-sider']/div[@class='ant-layout']/div[@class='ant-layout']/div[@class='welo-page-header ant-layout-header']/div[@class='welo-page-header-actions']/button[1]").click()
        # driver.find_element_by_xpath(
        #     "//*[@id=\"mount\"]/div/div[2]/div[2]/div/div[1]/div[2]/button[1]").click()
        # driver.find_element_by_css_selector(
        #     ".ant-select-selection--single > div.ant-select-selection__rendered").click()
        driver.find_element_by_xpath(
            "//div[@style='display: block; opacity: 1;' and text()='TY | 上海恩诺物流有限公司']").click()
        driver.find_element_by_xpath(
            "//div//div[contains(@class,'ant-col-6')]//div[contains(@class,'ant-select-selection__rendered')]//div[3]//div[1]//input[1]").send_keys(u"百超")
        driver.find_element_by_xpath(
            "//div//div[contains(@class,'ant-col-6')]//div[contains(@class,'ant-select-selection__rendered')]//div[3]//div[1]//input[1]").send_keys(Keys.ENTER)
        driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/div[1]").click()
        driver.find_element_by_xpath("//li[text()='进口货运']").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='运输方式'])[1]/following::div[5]").click()
        driver.find_element_by_xpath("//li[text()='海运']").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='货运流程'])[1]/following::div[5]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='寄售出库集报'])[1]/following::li[1]").click()
        sleep(3)
        driver.find_element_by_xpath(
            "//div[@class='welo-page-header-actions']//button[1]").click()
        sleep(2)
        driver.find_element_by_xpath(
            "//span/input[@placeholder='提单号*分提单号']").send_keys("zhu_fen")
        driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[6]/div[3]/div[1]/div[2]/div[1]/span[1]/span[1]/span[1]/input[1]").send_keys(
            "33")
        driver.find_element_by_xpath(
            "//div[@class='welo-page-header-actions']//button[1]").click()
        sleep(3)
        driver.find_element_by_xpath(
            "//div[@class='ant-table-fixed-right']/div[@class='ant-table-body-outer']/div/table/tbody/tr[1]/td[1]/span[1]//button[1]").click()
        driver.find_element_by_link_text(u"关务管理").click()
        sleep(3)
        driver.find_element_by_xpath(
            "//div[contains(@class,'ant-table-fixed-right')]//tbody[contains(@class,'ant-table-tbody')]//tr[1]//td[1]//span[1]//button[1]").click()
        driver.find_element_by_xpath(
            "//div[@id='trader_ciqcode']//input[@type='text']").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='/'])[9]/following::li[1]").click()
        driver.find_element_by_xpath(
            "//div[@id='owner_ciqcode']//input[@type='text']").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='/'])[9]/following::li[2]").click()
        driver.find_element_by_xpath(
            "//div[@id='agent_ciqcode']//input[@type='text']").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='/'])[9]/following::li[5]").click()
        driver.find_element_by_id("traf_name").click()
        driver.find_element_by_id("traf_name").clear()
        driver.find_element_by_id("traf_name").send_keys(u"船")
        driver.find_element_by_id("voyage_no").click()
        driver.find_element_by_id("voyage_no").clear()
        driver.find_element_by_id("voyage_no").send_keys("03891")
        driver.find_element_by_id("bl_wb_no").click()
        driver.find_element_by_id("bl_wb_no").clear()
        driver.find_element_by_id("bl_wb_no").send_keys("zhu_fen")
        driver.find_element_by_id("gross_wt").click()
        driver.find_element_by_id("gross_wt").clear()
        driver.find_element_by_id("gross_wt").send_keys("33")
        driver.find_element_by_id("net_wt").click()
        driver.find_element_by_id("net_wt").clear()
        driver.find_element_by_id("net_wt").send_keys("30")
        driver.find_element_by_xpath(
            "//div[@id='wrap_type']//div[@class='ant-select-selection__rendered']").click()
        driver.find_element_by_xpath(
            "//li[contains(text(),'纸制或纤维板制桶')]").click()
        driver.find_element_by_id("pack_count").click()
        driver.find_element_by_id("pack_count").clear()
        driver.find_element_by_id("pack_count").send_keys("30")
        driver.find_element_by_xpath("//input[@id='fee_rate']").send_keys("30")
        driver.find_element_by_xpath(
            "//input[@id='insur_rate']").send_keys("30")
        driver.find_element_by_xpath(
            "//input[@id='other_rate']").send_keys("30")
        driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/button[2]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='报关清单表头'])[1]/following::div[1]").click()
        mouse = driver.find_element_by_xpath("//span//button[2]")
        ActionChains(driver).move_to_element(mouse).perform()

        driver.find_element_by_xpath(
            "//li[contains(text(),'关联账册归并关系导入')]").click()
        # driver.find_element_by_xpath(
        #     u"(.//*[normalize-space(text()) and normalize-space(.)='上传文件'])[1]/following::p[1]").click()
        driver.find_element_by_css_selector("input[type=\"file\"]").send_keys(
            "/Users/zhaoliang/Downloads/百超关联账册导入.xlsx")
        sleep(3)
        # ActionChains(driver).move_to_element(mouse).perform()
        # driver.find_element_by_css_selector(
        #     "div:nth-child(9) div:nth-child(1) div.ant-dropdown.ant-dropdown-placement-bottomLeft ul.ant-dropdown-menu.ant-dropdown-menu-light.ant-dropdown-menu-root.ant-dropdown-menu-vertical > li.ant-dropdown-menu-item.ant-dropdown-menu-item-active:nth-child(5)").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::button[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='检验检疫编码'])[5]/following::div[5]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='sentinelEnd'])[1]/following::li[1]").click()
        driver.find_element_by_id("qty_1").click()
        driver.find_element_by_id("qty_1").clear()
        driver.find_element_by_id("qty_1").send_keys("30")
        driver.find_element_by_id("dec_price").click()
        driver.find_element_by_id("dec_price").clear()
        driver.find_element_by_id("dec_price").send_keys("30")
        driver.find_element_by_id("qty_2").click()
        driver.find_element_by_id("qty_2").clear()
        driver.find_element_by_id("qty_2").send_keys("30")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='毛重'])[3]/following::input[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='毛重'])[3]/following::input[1]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='毛重'])[3]/following::input[1]").send_keys("33")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='取 消'])[1]/following::button[1]").click()
        sleep(2)
        # 生成报关建议书
        driver.find_element_by_xpath(
            "//*[@id=\"mount\"]/div/div[2]/div[2]/div/div/div[1]/div[2]/button[1]").click()
        # 检务项报文
        driver.find_element_by_xpath(
            "//div[@class='ant-select-selection__rendered']/div[@title='全部发送']").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='sentinelEnd'])[1]/following::li[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='取 消'])[1]/following::button[1]").click()
        sleep(2)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='/'])[3]/following::button[1]").click()
        sleep(2)
        ActionChains(driver).send_keys(Keys.SHIFT+'a').perform()
        # driver.find_element_by_xpath("//input[@type='checkbox']").send_keys(Keys.SHIFT, 'a')
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='取 消'])[2]/following::button[1]").click()
        sleep(2)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='/'])[3]/following::button[1]").click()
        sleep(2)
        driver.find_element_by_xpath(
            "//tr[contains(@class,'ant-table-row ant-table-row-level-0')]//td[2]//div[1]//div[1]//span[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='有纸进口报关单'])[1]/following::li[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='有纸进境备案清单'])[1]/following::div[3]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='恩诺茂鸿-EP2121'])[1]/following::li[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='取 消'])[2]/following::button[1]").click()
        # mouseover = driver.find_element_by_xpath(
        #     "//span[contains(@class,'ant-breadcrumb-link')]//a[contains(@role,'presentation')]")
        # ActionChains(driver).move_to_element(mouseover).perform()
        # sleep(2)
        # driver.find_element_by_xpath(
        #     "//span[contains(@class,'ant-tree-node-content-wrapper ant-tree-node-content-wrapper-normal')]//span[contains(@class,'ant-tree-title')]").click()
        sleep(2)
        driver.find_element_by_xpath(
            "//ul[contains(@class,'ant-menu ant-menu-dark ant-menu-inline-collapsed ant-menu-root ant-menu-vertical')]//li[1]").click()
        driver.find_element_by_xpath(u"//a[contains(text(),'保税仓储')]").click()
        driver.find_element_by_xpath(
            "//ul[contains(@class,'ant-menu ant-menu-dark ant-menu-inline-collapsed ant-menu-root ant-menu-vertical')]//li[2]//ul[1]//li[1]").click()
        driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/div[1]/div[1]/div[1]/div[2]").click()
        driver.find_element_by_xpath("//li[contains(text(),'寄售维修仓')]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='全部供货商'])[1]/following::div[6]").click()
        driver.find_element_by_xpath("//li[contains(text(),'全部执行人员')]").click()
        sleep(2)
        # driver.find_element_by_xpath(
        # u"(.//*[normalize-space(text()) and normalize-space(.)='入库单'])[1]/following::li[1]").click()
        # 入库操作
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[2]/following::button[1]").click()
        sleep(2)
        driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/button[1]").click()
        sleep(2)
        # driver.find_element_by_xpath(
        #     "//tr[contains(@class,'ant-table-row ant-table-row-level-0')]//input[contains(@placeholder,'SKU件数')]").click()
        # driver.find_element_by_xpath(
        #      "//tr[contains(@class,'ant-table-row ant-table-row-level-0')]//input[contains(@placeholder,'SKU件数')]").clear()
        driver.find_element_by_xpath(
            "//tr[contains(@class,'ant-table-row ant-table-row-level-0')]//input[contains(@placeholder,'SKU件数')]").send_keys("30")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='操作'])[3]/following::input[4]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='取 消'])[1]/following::button[1]").click()
        sleep(3)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='收货明细'])[1]/following::div[1]").click()
        sleep(2)
        driver.find_element_by_xpath(
            "//div[contains(@class,'ant-tabs-tabpane ant-tabs-tabpane-active')]//div[contains(@class,'ant-table-fixed-right')]//td[contains(@class,'table-col-ops')]//button[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='上架库位'])[2]/following::div[5]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='sentinelEnd'])[1]/following::li[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='取 消'])[1]/following::button[1]").click()
        CostmnMouseover = driver.find_element_by_xpath(
            "//span[@class='ant-breadcrumb-link']//a[@role='presentation']")
        ActionChains(driver).move_to_element(CostmnMouseover).perform()
        driver.find_element_by_xpath(
            "//span[@class='ant-tree-node-content-wrapper ant-tree-node-content-wrapper-normal']//span[@class='ant-tree-title']").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='核注清单表头'])[1]/following::div[1]").click()
        driver.find_element_by_xpath(
            "//ul[@class='ant-menu-item-group-list']//li[@class='ant-menu-item ant-menu-item-selected']").click()
        driver.find_element_by_link_text(u"寄售入库核注清单").click()
        sleep(5)

    # def is_element_present(self, how, what):
    #     try:
    #         self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException as e:
    #         return False
    #     return True
    #
    # def is_alert_present(self):
    #     try:
    #         self.driver.switch.to.alert()
    #     except NoAlertPresentException as e:
    #         return False
    #     return True
    #
    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.driver.switch.to.alert()
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally:
    #         self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
