import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class slingsearchbonus(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.get("https://help.sling.com/")
        # print(self.driver.title)
        self.assertIn("Help", self.driver.title)

    def tearDown(self):
        self.driver.close()

    def test_slingsearchrokubonus(self):
        self.driver.find_element(By.ID, "support-search-input").click()
        self.driver.find_element(By.ID, "support-search-input").send_keys("roku")
        pageinfo = self.driver.page_source
        # print(pageinfo)
        self.assertIn("Roku", pageinfo)

if __name__ == '__main__':
    unittest.main()