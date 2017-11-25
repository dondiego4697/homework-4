# -*- coding: utf-8 -*-

import os
from selenium import webdriver


def main():
    browser = webdriver.Firefox(executable_path=os.environ['BROWSER_DRIVERS'] + '/geckodriver')

    browser.get('https://yandex.ru/')
    assert u'Яндекс' in browser.title
    browser.quit()


if __name__ == '__main__':
    main()
