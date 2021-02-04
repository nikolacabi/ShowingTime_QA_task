# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 22:39:13 2021

@author: Nikola
"""

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    
class MainPage(BasePage):

    def all_elements(self):
        return self.driver.find_elements_by_xpath('//*')
    
    def element_displayed(self, element_xpath):
        self.wait.until(EC.presence_of_element_located((By.XPATH, element_xpath)))
        return self.driver.find_element_by_xpath(element_xpath).is_displayed()

    def element_text(self, element_xpath):
        return self.driver.find_element_by_xpath(element_xpath).text
        
    def element_value(self, element_xpath):
        return self.driver.find_element_by_xpath(element_xpath).get_attribute("value")
    
    def element_alt(self, element_xpath):
        return self.driver.find_element_by_xpath(element_xpath).get_attribute("alt")
    
    def click_element(self, element_xpath):
        self.driver.find_element_by_xpath(element_xpath).click()

    def input_text_to_element(self, element_xpath, text):
        self.driver.find_element_by_xpath(element_xpath).send_keys(text)
        
    def press_ENTER(self, element_xpath):
        self.driver.find_element_by_xpath(element_xpath).send_keys(Keys.RETURN)


class SearchPage(BasePage):
    
    def element_text(self, element_xpath):
        self.wait.until(EC.presence_of_element_located((By.XPATH, element_xpath)))
        return self.driver.find_element_by_xpath(element_xpath).text
    
    def element_destination(self, element_xpath):
        self.wait.until(EC.presence_of_element_located((By.XPATH, element_xpath)))
        return self.driver.find_element_by_xpath(element_xpath).get_attribute("href")




