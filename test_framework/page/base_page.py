import logging

import yaml
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:

    _driver: WebDriver = None
    _current_element: WebElement = None

    def start(self):
        caps = {
            'platformName': 'android',
            'deviceName': 'ceshiren.com',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'noRest': True
        }
        self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self._driver.implicitly_wait(20)
        return self

    def stop(self):
        self._driver.quit()

    def find(self, by):
        self._current_element = self._driver.find_element(*by)
        return self

    def click(self):
        self._current_element.click()

    def send_keys(self, text):
        self._current_element.send_keys(text)

    def back(self):
        self._driver.back()

    def po_run(self, po_method, **kwargs):
        # 读取YAML
        with open("page_demo.yaml") as f:
            yaml_data = yaml.safe_load(f)
            # 查找
            for step in yaml_data[po_method]:
                # find by click send_keys
                if isinstance(step, dict):
                    # id click send_keys
                    for key in step.keys():
                        if key == 'id':
                            locator = (By.ID, step[key])
                            self.find(locator)
                        elif key == 'click':
                            self.click()
                        elif key == 'send_keys':
                            text = str(step[key])
                            for k, v in step.items():
                                text = text.replace('${' + key + '}', v)
                            self.send_keys(text)

                        # 更多关键词
                        else:
                            logging.error(f"Unknown step: {step}")
