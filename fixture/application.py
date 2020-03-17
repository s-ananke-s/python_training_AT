from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper

class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.session = SessionHelper(self)
        # нужно добавтьб что-то чтобы не вызывать from selenium.webdriver.common.by import By в session.py


    def return_to_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        self.open_groups_page()
        # init group creation
        self.driver.find_element(By.XPATH, "(//input[@name=\'new\'])[2]").click()
        # fill group form
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        self.driver.find_element(By.NAME, "submit").click()
        # return_to_groups_page
        self.return_to_groups_page()

    def open_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "groups").click()


    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")
        self.driver.set_window_size(1936, 1056)

    def destroy(self):
        self.driver.quit()