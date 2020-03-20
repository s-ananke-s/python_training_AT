from selenium.webdriver.common.by import By

class ContactHelper:
    def __init__(self,app):
        self.app = app

    def return_to_home_page(self):
        self.app.driver.find_element(By.LINK_TEXT, "home").click()

    def create(self, contact):
        self.open_contact_page()

        # fill contract form
        self.app.driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.app.driver.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        self.app.driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.app.driver.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        self.app.driver.find_element(By.NAME, "title").send_keys(contact.title)
        self.app.driver.find_element(By.NAME, "company").send_keys(contact.company)
        self.app.driver.find_element(By.NAME, "address").send_keys(contact.address)
        self.app.driver.find_element(By.NAME, "home").send_keys(contact.home)
        self.app.driver.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        self.app.driver.find_element(By.NAME, "work").send_keys(contact.work)
        self.app.driver.find_element(By.NAME, "fax").send_keys(contact.fax)
        self.app.driver.find_element(By.NAME, "email").send_keys(contact.email)
        self.app.driver.find_element(By.NAME, "email2").send_keys(contact.email2)
        self.app.driver.find_element(By.NAME, "email3").send_keys(contact.email3)
        self.app.driver.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        self.app.driver.find_element(By.NAME, "address2").send_keys(contact.address2)
        self.app.driver.find_element(By.NAME, "phone2").send_keys(contact.phone2)
        self.app.driver.find_element(By.NAME, "notes").send_keys(contact.notes)



        #self.app.driver.find_element(By.NAME, "bday").click()
        ##dropdown.find_element(By.XPATH, "//option[. = '14']").click()

        self.app.driver.find_element(By.XPATH, "(// select[@name=\'bday\']\option[text()=" + contact.bday + "]").click()

        #self.app.driver.find_element(By.NAME, "bmonth").click()
        #dropdown = self.app.driver.find_element(By.NAME, "bmonth")
        #dropdown.find_element(By.XPATH, "//option[. = 'June']").click()

        self.app.driver.find_element(By.XPATH, "// select[@name=\'bmonth\']\option[text()=" + contact.bmonth + "]").click()

        # submit contact creation
        self.app.driver.find_element(By.XPATH, "(//input[@name=\'submit\'])[2]").click()
        self.return_to_home_page()

    def open_contact_page(self):
        self.app.driver.find_element(By.LINK_TEXT, "add new").click()
