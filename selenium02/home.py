from selenium.webdriver.remote.webdriver import WebDriver

from selenium02.contacts import ContactsPage


class HomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def go_to_contacts(self):
        # 点击"通讯录"
        self.driver.find_element_by_id("menu_contacts").click()
        return ContactsPage(self.driver)
