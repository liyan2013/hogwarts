from selenium.webdriver.remote.webdriver import WebDriver

from selenium02.department import DepartmentPage


class ContactsPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_department(self):
        # 点击添加子部门
        self.driver.find_element_by_class_name("js_add_sub_party").click()
        return DepartmentPage(self.driver)
