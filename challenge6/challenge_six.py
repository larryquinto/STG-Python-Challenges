import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from challenge6.TopNavSearch import TopNavSearch
from challenge6.FilterOptions import FilterOptions
from challenge6.CaptureScreen import CaptureScreen

class ChallengeSix(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge6(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        self.driver.maximize_window()
        tns = TopNavSearch(self.driver)
        fo = FilterOptions(self.driver)
        cs = CaptureScreen(self.driver)

        try:
            filter_name = "Model"
            modelvalue = "Skylarry"
            query = "Nissan"
            self.assertIn(query.upper(), tns.runSearch(query).text)
            txtelement, count = fo.filter_selection(filter_name)
            txtelement.send_keys(modelvalue)
            checkElement = self.driver.find_element(By.XPATH,
                "//*[@id='collapseinside" + str(count) + "']//abbr[@value='" + modelvalue + "']")
            checkElement.click()

        except:
            print("An exception occurred")
            # capture an image
            print("You looked for " + modelvalue)
            timestr = time.strftime("%Y%m%d-%H%M%S")
            element = self.driver.find_element(By.XPATH, "//*[@id='filters-collapse-1']")
            path = "../challenge6/screen_grab_" + timestr + ".png"
            cs.capture(element, path)
            checkboxelements = self.driver.find_elements(By.XPATH, "//*[@id='collapseinside" + str(count) +
                                                         "']//input[@type='checkbox']")
            print("This is not an available selection")
            for e in checkboxelements:
                print(e.get_attribute('value'))