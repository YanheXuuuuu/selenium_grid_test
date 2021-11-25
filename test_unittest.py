# -*- coding: utf-8 -*-

#https://testdriven.io/blog/distributed-testing-with-selenium-grid/
import time, os
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class HackerNewsSearchTest(unittest.TestCase):
    def set_chrome_options(self):
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

    def setUp(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        print(time.time(),caps)
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            #command_executor="http://0.0.0.0:4444/wd/hub",
            desired_capabilities=caps,
            options=self.set_chrome_options()
    )

    def test_hackernews_search_for_testdrivenio(self):
        browser = self.browser
        browser.get('https://news.ycombinator.com')
        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven.io')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # simulate long running test
        self.assertIn('testdriven.io', browser.page_source)

    def test_hackernews_search_for_selenium(self):
        browser = self.browser
        browser.get('https://news.ycombinator.com')
        search_box = browser.find_element_by_name('q')
        search_box.send_keys('selenium')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # simulate long running test
        self.assertIn('selenium', browser.page_source)

    def test_hackernews_search_for_testdriven(self):
        browser = self.browser
        browser.get('https://news.ycombinator.com')
        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # simulate long running test
        self.assertIn('testdriven', browser.page_source)

    def test_hackernews_search_with_no_results(self):
        browser = self.browser
        browser.get('https://news.ycombinator.com')
        search_box = browser.find_element_by_name('q')
        search_box.send_keys('?*^^%')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # simulate long running test
        self.assertNotIn('<em>', browser.page_source)

    def tearDown(self):
        self.browser.quit()  # quit vs close?
        #self.brower.close()


if __name__ == '__main__':
    unittest.main(warnings='ignore')

        #    breakß
            
        #except:
        #    print("fail!")
    