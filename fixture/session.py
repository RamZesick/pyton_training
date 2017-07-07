
class SessionHelper:
    def __init__(self, app):
        self.app=app

    def login(self, group):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_element_by_id("mailbox__login").click()
        wd.find_element_by_id("mailbox__login").clear()
        wd.find_element_by_id("mailbox__login").send_keys(group.username)
        wd.find_element_by_id("mailbox__password").click()
        wd.find_element_by_id("mailbox__password").clear()
        wd.find_element_by_id("mailbox__password").send_keys(group.password)
        wd.find_element_by_id("mailbox__auth__button").click()