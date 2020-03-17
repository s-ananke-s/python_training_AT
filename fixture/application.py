from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        # нужно добавтьб что-то чтобы не вызывать from selenium.webdriver.common.by import By в session.py


    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")
        self.driver.set_window_size(1936, 1056)

    def destroy(self):
        self.driver.quit()