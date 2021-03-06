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

class TestRokuSearchSling():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_rokuSearchSling(self):
    self.driver.get("https://www.sling.com/")
    self.driver.set_window_size(1256, 785)
    self.driver.find_element(By.LINK_TEXT, "Help Center").click()
    self.driver.find_element(By.ID, "support-search-input").click()
    self.driver.find_element(By.ID, "support-search-input").send_keys("roku")
    self.driver.find_element(By.CSS_SELECTOR, ".hide-in-mobile").click()
  
