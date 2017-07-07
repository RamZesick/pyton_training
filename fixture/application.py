
from selenium.webdriver.firefox.webdriver import WebDriver


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_homepage(self):
        wd = self.wd
        wd.get("https://mail.ru/")

    def login(self, group):
        wd = self.wd
        wd.find_element_by_id("mailbox__login").click()
        wd.find_element_by_id("mailbox__login").clear()
        wd.find_element_by_id("mailbox__login").send_keys(group.username)
        wd.find_element_by_id("mailbox__password").click()
        wd.find_element_by_id("mailbox__password").clear()
        wd.find_element_by_id("mailbox__password").send_keys(group.password)
        wd.find_element_by_id("mailbox__auth__button").click()

    def destroy(self):
        self.wd.quit()