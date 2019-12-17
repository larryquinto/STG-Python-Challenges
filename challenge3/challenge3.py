import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.get("https://www.copart.com/")
        # print(self.driver.title)
        self.assertIn("Copart", self.driver.title)

    def tearDown(self):
        self.driver.close()

    def test_challenge3_forloop(self):
        # datawait = WebDriverWait(self.driver, 10)
        # datawait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='tabTrending']")))
        # makesmodels = self.driver.find_element(By.XPATH, "//*[@id='tabTrending']/div[1]/div[2]")
        # print(makesmodels.text)
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]//a")
        print(len(elements))
        # elements[0].text
        # x = "apple"
        # y = "banana"
        # z = "cherry"
        # fruits = [x, y, z]
        for count in elements:
            print(count.text + " - " + count.get_attribute("href"))

    def test_challenge3_whileloop(self):
        # elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]//a")
        elements = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"tabTrending\"]/div[1]//a")
        print(len(elements))
        i = 0
        while i < len(elements):
            print(elements[i].text + " - " + elements[i].get_attribute("href"))
            i += 1

if __name__ == '__main__':
    unittest.main()
