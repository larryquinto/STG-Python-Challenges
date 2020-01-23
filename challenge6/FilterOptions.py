from selenium.webdriver.common.by import By

class FilterOptions:
    def __init__(self, driver):
        self.driver = driver

    def filter_selection(self, filter_name):
        elements = self.driver.find_elements(By.XPATH, "//*[@id='filters-collapse-1']//li//h4//a")
        count = 0
        for e in elements[::2]:
            count = count + 1
            if e.text == filter_name:
                e.click()
                break
        return self.driver.find_element(By.XPATH, "//*[@id='collapseinside" + str(count) + "']/form/div/input"), count