from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CoPartSearchTopNav:
    def __init__(self, driver):
        self.driver = driver

    # Code to search for cars by variable passed in from another script
    def run_search(self, query):
        self.driver.get("https://www.copart.com/")
        searchfield = self.driver.find_element(By.ID, "input-search")
        searchfield.send_keys(query)
        searchbutton = self.driver.find_element(By.XPATH, "//button[@data-uname=\"homepageHeadersearchsubmit\"]")
        searchbutton.click()
        datawait = WebDriverWait(self.driver, 30)
        datawait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='serverSideDataTable']")))
        dropdown = self.driver.find_element(By.NAME, "serverSideDataTable_length")
        # Change results from 20 to 100
        dropdown.find_element(By.XPATH, "//option[. = '100']").click()
        # datawait2 = WebDriverWait(self.driver, 20)
        # datawait2.until(EC.visibility_of_element_located((By.XPATH,
        #                                                   "//*[@id='serverSideDataTable_wrapper']/div[3]/div[1]")))
        time.sleep(2)
        # showing = self.driver.find_element(By.XPATH, "//*[@id='serverSideDataTable_wrapper']/div[3]/div[1]")
        # print(showing.text)
        # self.assertIn("100", showing.text)