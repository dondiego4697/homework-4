# -*- coding: utf-8 -*-

import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    browser = webdriver.Firefox(executable_path = os.environ['BROWSER_DRIVERS'] + '/geckodriver')

    browser.get('http://www.yahoo.com')
    assert 'Yahoo' in browser.title

    elem = browser.find_element_by_name('p')
    elem.send_keys('seleniumhq' + Keys.RETURN)

    browser.quit()

    # print os.environ['BROWSER_DRIVERS']
    # browser = webdriver.Chrome(os.environ['BROWSER_DRIVERS'] + '/chromedriver')
    # browser.get('http://www.yahoo.com')
    # assert 'Yahoo' in browser.title
    # browser.quit()


if __name__ == '__main__':
    main()
