from selenium import webdriver

from selenium02.home import HomePage

option = webdriver.ChromeOptions()
option.debugger_address = "localhost:9222"

driver = webdriver.Chrome(options=option)
driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
driver.maximize_window()
driver.implicitly_wait(5)

home = HomePage(driver)

contacts = home.go_to_contacts()

department = contacts.add_department()

department.add_department("test")
