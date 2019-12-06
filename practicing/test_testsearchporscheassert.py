# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestsearchporscheassert():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testsearchporscheassert(self):
    self.driver.get("https://www.copart.com/")
    self.driver.set_window_size(1256, 784)
    self.driver.execute_script("window.scrollTo(0,0.800000011920929)")
    self.driver.find_element(By.ID, "input-search").click()
    self.driver.find_element(By.ID, "input-search").send_keys("exotics")
    self.driver.find_element(By.ID, "input-search").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(5) > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(5) > span").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(5) > span")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(3) > td:nth-child(5) > span").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(3) > td:nth-child(5) > span").text == "PORSCHE"
    self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(5)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(5) > td:nth-child(5) > span").text == "PORSCHE"
    self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(6)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(6) > td:nth-child(5) > span").text == "PORSCHE"
    assert self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(5) > span").text == "PORSCHE"
  