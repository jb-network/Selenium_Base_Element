from selenium import webdriver
from traning_ground import TrainingGroundPage
from trial_page import TrialPage

# Test Setup
browser = webdriver.Chrome()

# Trial_Page
trial_page = TrialPage(driver=browser)
trial_page.go()
trial_page.stone_input.input_text("rock")
trial_page.stone_button.click()
# Just for this test, this should not be in a real test
input()

# Training Grounds
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
# used @property to remove button1().click()
assert trng_page.button1.text() == "Button1", "Unexpected button1 text"
print("Passed")
input()
browser.quit()
# trng_page.button1.click()
