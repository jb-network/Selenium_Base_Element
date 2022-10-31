class BasePage(object):
    # Things you want or know every page will need to do
    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)
