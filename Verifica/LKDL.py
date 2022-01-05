import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException
import time

import Items


class Crawler:
    def __init__(self, website, nome):
        path = r'C:/chromedriver_win32/chromedriver.exe'

        driver = webdriver.Chrome(path)
        driver.get(website)


        def ler():
            tenta = 0
            while True:
                try:
                    return driver.find_element_by_class_name('details').text
                except NoSuchElementException:
                    tenta += 1
                    time.sleep(0.1)
                    if tenta > 15:
                        return ''

        teste = 0
        print('\n'+nome)
        termos = Items.itens().termos
        tdesc = ler()
        for termo in termos:
                try:
                    if tdesc.find(termo) > 0:
                        teste += 1
                        print(termo)
                except NameError:
                    tdesc = ler()
        print('\n')
        if (teste >= 4):
            verf= True
        else:
            verf = False
        self.verf = verf
        driver.quit()
