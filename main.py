from selenium import webdriver

from Python_Daily_Work.Traning_Ground_2 import TrainingGroundPage

# Test Setup
browser = webdriver.Chrome()
test_value = "it worked"

# Test
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
# used @property to remove button1().click()
trng_page.button1.click()
