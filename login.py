# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import re


class UntitledTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://nlo.welogix.co/login")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='数字化跨境供应链'])[1]/following::input[1]").send_keys(
            "admin")

        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='数字化跨境供应链'])[1]/following::input[2]").send_keys(
            "123456")

        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='记住我'])[1]/following::button[1]").click()

        driver.find_element_by_xpath(
            "//*[@id=\"mount\"]/div/div[2]/div[2]/div[1]/div/div[3]/a/div/div/div").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='特殊区保税物流'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='选择仓库'])[1]/following::div[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='大陆仓库'])[1]/following::li[1]").click()
        sleep(3)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='修改'])[4]/following::button[4]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='账册表头'])[1]/following::div[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='新 建'])[1]/following::button[1]").click()
        # driver.find_element_by_xpath(
        # u"(.//*[normalize-space(text()) and
        # normalize-space(.)='重复覆盖'])[1]/preceding::input[1]").click()
        # driver.find_element_by_xpath(
        #     u"(.//*[normalize-space(text()) and normalize-space(.)='上传文件'])[1]/following::p[1]").click()
        driver.find_element_by_css_selector("input[type=\"file\"]").send_keys(
        u"/Users/zhaoliang/Downloads/账册KS4923830100全部明细.xlsx")
        sleep(3)
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
