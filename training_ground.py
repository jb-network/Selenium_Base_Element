from selenium.webdriver.common.by import By
from base_element import BaseElement
from base_page import BasePage
from locator import Locator


class TrainingGroundPage(BasePage):
    # init happens in parent class
    url = "https://techstepacademy.com/training-ground"

    # treat as a property method treated like a var..get/set, but still treated as var.
    @property
    def button1(self):
        locator = Locator(by=By.ID, value='b1')
        return BaseElement(driver=self.driver, locator=locator)
