from selenium import webdriver
from selenium.webdriver.common.by import By
from challenge7.check import Check
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings

class GoToLink:
    def __init__(self):
        print("Execute GoToLink")

    def goTo(self, url, verifyText):
        warnings.simplefilter("ignore", ResourceWarning)
        mismatch = 0
        self.driver2 = webdriver.Chrome("../chromedriver.exe")
        self.driver2.get(url)

        element_is_there = EC.presence_of_element_located((By.XPATH, "//*[@id=\"searchResultsHeader\"]/a"))
        WebDriverWait(self.driver2, 30).until(element_is_there)

        c = Check()

        element = self.driver2.find_element(By.XPATH, "//*[@id=\"searchResultsHeader\"]/span[2]")

        newVerifyText = verifyText.replace(' ', '')
        newVerifyText = newVerifyText.replace('-', '')
        targetText = element.text[5:].upper()
        self.driver2.close()
        newTargetText = targetText.replace('-', '')
        newTargetText = newTargetText.replace(' ', '')
        if c.compare(newVerifyText, newTargetText) > 0:
            print("verifyText: " + newVerifyText)
            print("element.text: " + newTargetText)
            mismatch += 1

        if mismatch == 0:
            return True
        else:
            return False