from selenium.webdriver.common.by import By
from .base import Page
from time import sleep


class login(Page):
    @property
    def username_text_field(self):
        return self.by_id('kw')

    @property
    def login_btn(self):
        return self.by_id('su')

    def login(self, username):
        self.open()
        self.username_text_field.send_keys(username)
        self.login_btn.click()
