from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest




def test_1(launch_browser):
    browser = launch_browser
    browser.get("https://www.google.com")
    p = search_page(browser)
    p.search("test")
    

def test_2(launch_browser):
    browser = launch_browser
    browser.get("https://www.facebook.com")
    browser.close()

def test_3(launch_browser):
    browser = launch_browser
    browser.get("https://www.facebook.com")
    browser.close()

def test_4(launch_browser):
    browser = launch_browser
    browser.get("https://www.facebook.com")
    browser.close()

def test_5(launch_browser):
    browser = launch_browser
    browser.get("https://www.facebook.com")
    browser.close()


def test_6(launch_browser):
    browser = launch_browser
    browser.get("https://www.facebook.com")
    browser.close()



class search_page:

    def __init__(self,browser):
        self.a = "//input[@name='q']"
        self.browser  = browser      

    def search(self, x):
        wait_for(self.browser,self.a,2)
        e=self.browser.find_element_by_xpath(self.a) 
        e.send_keys("test")
        
    def go_to():
        pass   




def wait_for(b,x,t):
    e = WebDriverWait(b,t).until(EC.presence_of_element_located((By.XPATH,x)))
     
    



