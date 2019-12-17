import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class slingchannelimages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.get("https://www.sling.com/")
        # print(self.driver.title)
        # self.assertIn("Sling", self.driver.title)

    def tearDown(self):
        self.driver.close()

    def test_slingchannelimages_forloop(self):
        self.driver.find_element(By.CSS_SELECTOR, "#planThree > .dyn-grid_package-title").click()
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"channelList\"]//img")
        print(len(elements))
        for count in elements:
            print(count.text + " - " + count.get_attribute("title"))

if __name__ == '__main__':
    unittest.main()
