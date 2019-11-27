import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com/")
        self.assertIn("Copart", self.driver.title)
        self.driver.find_element(By.ID, "input-search").click()
        self.driver.find_element(By.ID, "input-search").send_keys("exotics")
        self.driver.find_element(By.ID, "input-search").send_keys(Keys.ENTER)

if __name__ == '__main__':
    unittest.main()
