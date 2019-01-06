# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://nlo.welogix.co/login")
        sleep(2)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='数字化跨境供应链'])[1]/following::input[1]").send_keys(
            "admin")

        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='数字化跨境供应链'])[1]/following::input[2]").send_keys(
            "123456")

        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='记住我'])[1]/following::button[1]").click()
        # 登录
        # driver.find_element_by_xpath(
        #     "//*[@id=\"mount\"]/div/div[2]/div[2]/div[1]/div/div[3]/a/div/div/div").click()
        # 工作台
        driver.find_element_by_xpath(
            "//*[@id=\"mount\"]/div/div[2]/div[2]/div[1]/div/div[1]/a/div/span").click()
        sleep(5)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='全部订单'])[1]/following::button[1]").click()
        sleep(3)
        driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[3]/div[2]/form/div[1]/div[2]/div/span/div/div/div/div[1]").click()
        driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[3]/div[2]/form/div[1]/div[2]/div/span/div/div/div/div[2]/div/input").clear()
        driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[3]/div[2]/form/div[1]/div[2]/div/span/div/div/div/div[2]/div/input").send_keys(
            "356")
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[1]").click()
        driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[3]/div[2]/form/div[2]/div[2]/div/span/div/div/div").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='进境清关'])[1]/following::li[1]").click()
        # driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[3]/div[2]/div/span/div/span").click()
        sleep(2)
        driver.find_element_by_css_selector("input[type=\"file\"]").send_keys(u"/Users/zhaoliang/PycharmProjects/A/订单.xlsx")
        sleep(3)
        driver.find_element_by_css_selector(
            "i.anticon.anticon-close.ant-notification-close-icon > svg > path").click()
        sleep(2)
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
