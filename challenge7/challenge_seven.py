import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from challenge7.GoToLink import GoToLink


class challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

    def tearDown(self):
        self.driver.close()

    def test_challenge7(self):
        elements = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]//a")
        dictionary = dict()

        for model in elements:
            try:
                go = GoToLink()
                txt = model.text
                dictionary[txt] = model.get_attribute("href")
                print(txt + " - " + dictionary[txt])

                if go.goTo(dictionary[txt], txt):
                    print("Successful navigation to " + txt + "'s link")
                else:
                    print("Failed navigation to " + txt + "'s link")

            except:
                print("An error occurred.")


if __name__ == '__main__':
    unittest.main()