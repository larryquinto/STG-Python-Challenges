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

class TestSearchforPorsche():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_searchforPorsche(self):
    self.driver.get("https://www.copart.com/")
    self.driver.set_window_size(1254, 784)
    self.driver.find_element(By.ID, "input-search").click()
    self.driver.find_element(By.ID, "input-search").send_keys("porsche")
    self.driver.find_element(By.ID, "input-search").send_keys(Keys.ENTER)
    self.driver.find_element(By.ID, "input-search").send_keys("porsche")
    self.driver.execute_script("window.scrollTo(0,0)")
    assert self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(6) > span").text == "CAYENNE S"
    assert self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(6) > span").text == "CAYENNE S"
    self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(6) > span").text == "CAYENNE S"
  
