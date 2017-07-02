# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_record(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_homepage(self, wd):
        wd.get("https://mail.ru/")

    def login(self, wd, group):
        wd.find_element_by_id("mailbox__login").click()
        wd.find_element_by_id("mailbox__login").clear()
        wd.find_element_by_id("mailbox__login").send_keys(group.username)
        wd.find_element_by_id("mailbox__password").click()
        wd.find_element_by_id("mailbox__password").clear()
        wd.find_element_by_id("mailbox__password").send_keys(group.password)
        wd.find_element_by_id("mailbox__auth__button").click()

    def test_record(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, Group(username="roman2", password="222"))

    def test_record2(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, Group(username="roman", password="123"))

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
