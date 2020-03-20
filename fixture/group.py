from selenium.webdriver.common.by import By

class GroupHelper:
    def __init__(self,app):
        self.app = app

    def return_to_groups_page(self):
        self.app.driver.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        self.open_groups_page()
        # init group creation
        self.app.driver.find_element(By.XPATH, "(//input[@name=\'new\'])[2]").click()
        # fill group form
        self.app.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.app.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.app.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        self.app.driver.find_element(By.NAME, "submit").click()
        # return_to_groups_page
        self.return_to_groups_page()

    def open_groups_page(self):
        self.app.driver.find_element(By.LINK_TEXT, "groups").click()

