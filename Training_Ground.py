from selenium.webdriver.common.by import By
from .Base_element import BaseElement


class TrainingGroundPage:
    def __init__(self,driver):
        self.driver = driver
        self.url = "https://techstepacademy.com/training-ground"

    def go(self):
        self.driver.get(self.url)

    #treat as a property method treated like a var..get/set, but still treated as var.
    @property
    def button1(self):
        locator = (By.ID, 'b1')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
