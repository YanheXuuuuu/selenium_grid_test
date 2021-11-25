# -*- coding: utf-8 -*-

#https://testdriven.io/blog/distributed-testing-with-selenium-grid/
import time, os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    def set_chrome_options():
        """Sets chrome options for Selenium.
        Chrome options for headless browser is enabled.
        """
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--verbose")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_prefs = {}
        chrome_options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        return chrome_options
    
    caps = {'browserName': os.getenv('BROWSER', 'chrome')}
    print("start",time.time(),caps)
    browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            #command_executor="http://0.0.0.0:4444/wd/hub",
            desired_capabilities=caps,
            options=set_chrome_options()
    )
    browser.get('https://news.ycombinator.com')
    browser.quit()
    print("end",time.time(),caps)
            
        #except:
        #    print("fail!")
    