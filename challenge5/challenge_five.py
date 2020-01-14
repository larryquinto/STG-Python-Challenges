import unittest
from selenium import webdriver
from challenge5.CoPartSearchNav import *

class challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_copart_search(self):
        s = CoPartSearchTopNav(self.driver)
        query = ["porsche"]
        for q in query:
            s.run_search(q)

        model_list = self.driver.find_elements(By.XPATH, "//tbody//span[@data-uname='lotsearchLotmodel']")
        # print(len(model_list))
        # Count of duplicate models; add to dictionary
        model_dictionary = dict()
        for item in model_list:
            model = item.text
            if model:
                if model in model_dictionary:
                    model_dictionary[model] += 1
                else:
                    model_dictionary[model] = 1
        # print("------------------------------------------------")
        print("%s different models in results" % (len(model_dictionary)))
        print("##############################")
        print("Model : Count")
        print("##############################")
        for model, count in model_dictionary.items():
            print(str(model) + " : " + str(count))
        print("##############################")

        damage_list = self.driver.find_elements(By.XPATH, "//*[@data-uname='lotsearchLotdamagedescription']")
        damage_dictionary = {"MINOR DENT/SCRATCHES": 0, "REAR END": 0, "FRONT END": 0, "UNDERCARRIAGE": 0, "MISC": 0}
        for item in damage_list:
            damage = item.text
            if damage:
                if damage in damage_dictionary:
                    damage_dictionary[damage] += 1
                else:
                    damage_dictionary["MISC"] += 1
        print("Damage : Count")
        print("##############################")
        for damage, count in damage_dictionary.items():
            print(str(damage) + " : " + str(count))
        print("##############################")

if __name__ == '__main__':
    unittest.main()