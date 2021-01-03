from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver


class DepartmentPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_department(self, name):
        # 输入部门名称
        self.driver.find_element_by_xpath("//input[@class='qui_inputText ww_inputText']").send_keys(name)
        # 点击部门下路菜单
        self.driver.find_element_by_xpath("//a[@class='qui_btn ww_btn ww_btn_Dropdown js_toggle_party_list']").click()
        # 选择上级部门
        item = self.driver.find_element_by_xpath("//a[@class='jstree-anchor']")
        chain = ActionChains(self.driver)
        chain.move_to_element(item).click(item).perform()
        # 点击确定按钮
        self.driver.find_element_by_xpath("//a[@class='qui_btn ww_btn ww_btn_Blue']").click()
