import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge3_forloop(self):
        self.driver.get("https://www.copart.com/")
        # print(self.driver.title)
        self.assertIn("Copart", self.driver.title)
        datawait = WebDriverWait(self.driver, 10)
        datawait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='tabTrending']")))
        makesmodels = self.driver.find_element(By.XPATH, "//*[@id='tabTrending']/div[1]/div[2]")
        print(makesmodels.text)
        elements = self.driver.find_elements(By.XPATH, "//*[@id='tabTrending']/div[1]/div[2]//a")
        # fruits = ["apple", "banana", "cherry"]
        elements[0].text
        for x in elements:
            print(x)
        # html = self.driver.page_source
        # print(html)

    # def test_challenge3_whileloop(self):
    #     self.driver.get("https://www.copart.com/")
    #     print(self.driver.title)
    #     self.assertIn("Copart", self.driver.title)
    #     # self.driver.find_element(By.ID, "input-search").click()
    #     # self.driver.find_element(By.ID, "input-search").send_keys("exotics")
    #     # self.driver.find_element(By.ID, "input-search").send_keys(Keys.ENTER)
    #     # html = self.driver.page_source
    #     # print(html)
    #     # element = self.driver.find_element(By.XPATH, "//*[@name=\"q\"]")
    #     element = self.driver.find_element(By.ID, "input-search")
    #     element.send_keys("exotics")
    #     searchBtn = self.driver.find_element(By.XPATH, "//button[@data-uname='homepageHeadersearchsubmit']")
    #     searchBtn.click()
    #     html = self.driver.page_source
    #     print(html)
    #     datawait = WebDriverWait(self.driver, 10)
    #     datawait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]//td")))
    #     datatable = self.driver.find_element(By.XPATH, "//*[@id=\"serverSideDataTable\"]")
    #     print(datatable.text)
    #     self.assertIn("PORSCHE", datatable.text)

if __name__ == '__main__':
    unittest.main()
