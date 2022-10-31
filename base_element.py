from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):
    # Driver = Driver, value is the target, by is the path via CSS or XPATH
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        # Hold Selenium web element class when an element is found
        self.web_element = None
        self.find()

    def find(self):
        # Example: Do not hardcode CSS, XPATH..etc, but this is not good enough
        # self.driver.find_element(by=self.by, value=self.locator)
        # locator is a tuple
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def input_text(self, text):
        self.web_element.send_keys(text)
        return None

    def click(self):
        # element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator=self.locator))
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator))
        element.click()
        return None

    def text(self):
        # Web element is already captured from find
        text = self.web_element.text
        return text
