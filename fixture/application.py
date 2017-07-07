
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_homepage(self):
        wd = self.wd
        wd.get("https://mail.ru/")



    def destroy(self):
        self.wd.quit()