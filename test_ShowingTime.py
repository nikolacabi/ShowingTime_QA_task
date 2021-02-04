# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 22:26:54 2021

@author: Nikola
"""

import pytest
from selenium import webdriver
import page
import Elements
#import time


def test_Gmail():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.Gmail)
    assert main_page.element_text(Elements.MainPageElement.Gmail) == "Gmail"

    driver.close()    
    
    
def test_Images():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.Images)
    assert main_page.element_text(Elements.MainPageElement.Images) == "Images"

    driver.close()  
    
    
def test_More():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.More)

    driver.close()  
        
    
def test_Menu():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)
    main_page.click_element(Elements.MainPageElement.More)

    assert main_page.element_displayed(Elements.MainPageElement.Menu)

    driver.close()  


def test_Sign_In():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.Sign_In)
    assert main_page.element_text(Elements.MainPageElement.Sign_In) == "Sign in"
    
    driver.close()  


def test_Google():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.Google)
    assert main_page.element_alt(Elements.MainPageElement.Google) == "Google"
    
    driver.close()  


def test_Search():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.Search)
    
    driver.close()  


def test_Google_Search():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.Google_Search)
    assert main_page.element_value(Elements.MainPageElement.Google_Search) == "Google Search"
    
    driver.close()  


def test_Im_feeling_lucky():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.Im_feeling_lucky)
    assert main_page.element_value(Elements.MainPageElement.Im_feeling_lucky) == "I'm Feeling Lucky"
    
    driver.close()  


def test_Google_offer():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.Google_offer)
    assert main_page.element_text(Elements.MainPageElement.Google_offer) == "Google offered in: српски srpski"
    
    driver.close()  


def test_Script1():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.Script1)
    assert main_page.element_text(Elements.MainPageElement.Script1) == "српски"
    
    driver.close()  


def test_Script2():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.Script2)
    assert main_page.element_text(Elements.MainPageElement.Script2) == "srpski"
    
    driver.close()  


def test_Country():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.Country)
    assert main_page.element_text(Elements.MainPageElement.Country) == "Serbia"
    
    driver.close()  


def test_Advertising():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.Advertising)
    assert main_page.element_text(Elements.MainPageElement.Advertising) == "Advertising"
    
    driver.close()  
    
    
def test_Business():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.Business)
    assert main_page.element_text(Elements.MainPageElement.Business) == "Business"
    
    driver.close()     
    
    
def test_About():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.About)
    assert main_page.element_text(Elements.MainPageElement.About) == "About"
    
    driver.close()         
               
    
def test_How():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.How)
    assert main_page.element_text(Elements.MainPageElement.How) == "How Search works"
    
    driver.close()         
        
    
def test_Privacy():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.Privacy)
    assert main_page.element_text(Elements.MainPageElement.Privacy) == "Privacy"
    
    driver.close()        
    
    
def test_Terms():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.Terms)
    assert main_page.element_text(Elements.MainPageElement.Terms) == "Terms"
    
    driver.close()         
    

def test_Settings():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)

    assert main_page.element_displayed(Elements.MainPageElement.Settings)
    assert main_page.element_text(Elements.MainPageElement.Settings) == "Settings"
    
    driver.close()   
    
    
def test_Settings_Menu():

    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)
    main_page.click_element(Elements.MainPageElement.Settings)

    assert main_page.element_displayed(Elements.MainPageElement.Settings_Menu)

    driver.close()  


def test_Search_ShowingTime():
    
    driver = webdriver.Firefox()
    driver.get("http://www.google.com/en")

    main_page = page.MainPage(driver)
    search_page = page.SearchPage(driver)

    main_page.input_text_to_element(Elements.MainPageElement.Search, "ShowingTime")
    main_page.press_ENTER(Elements.MainPageElement.Search)
    
    assert (search_page.element_text(Elements.ResultPageElement.first_result)).find('ShowingTime')!=-1
    assert (search_page.element_destination(Elements.ResultPageElement.first_result)).find('www.showingtime.com')!=-1
    
    driver.close()  
    




