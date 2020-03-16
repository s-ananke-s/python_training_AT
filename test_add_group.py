# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTestaddgroup():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_add_group(self):
    self.open_home_page()
    self.login(username="admin", password="secret")
    self.open_groups_page()
    self.create_group(group_name="new2", group_header="new2", group_footer="new2")
    self.return_to_groups_page()
    self.logout()
    self.driver.close()


  def test_add_empty_group(self):
    self.open_home_page()
    self.login(username="admin", password="secret")
    self.open_groups_page()
    self.create_group(group_name="", group_header="", group_footer="")
    self.return_to_groups_page()
    self.logout()
    self.driver.close()

  def logout(self):
    self.driver.find_element(By.LINK_TEXT, "Logout").click()

  def return_to_groups_page(self):
    self.driver.find_element(By.LINK_TEXT, "groups").click()

  def create_group(self, group_name, group_header, group_footer):
    # init group creation
    self.driver.find_element(By.XPATH, "(//input[@name=\'new\'])[2]").click()
    # fill group form
    self.driver.find_element(By.NAME, "group_name").send_keys(group_name)
    self.driver.find_element(By.NAME, "group_header").send_keys(group_header)
    self.driver.find_element(By.NAME, "group_footer").send_keys(group_footer)
    # submit group creation
    self.driver.find_element(By.NAME, "submit").click()

  def open_groups_page(self):
    self.driver.find_element(By.LINK_TEXT, "groups").click()

  def login(self, username, password):
    self.driver.find_element(By.NAME, "user").send_keys(username)
    self.driver.find_element(By.NAME, "pass").send_keys(password)
    self.driver.find_element(By.XPATH, "//input[@value=\'Login\']").click()

  def open_home_page(self):
    self.driver.get("http://localhost/addressbook/")
    self.driver.set_window_size(1936, 1056)