import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException
import time

from selenium.webdriver.common.by import By

import Items


class Crawler:
    def __init__(self, website, nome):
        path = r'C:/chromedriver_win32/chromedriver.exe'

        driver = webdriver.Chrome(path)
        driver.get(website)
        erros = []

        while True:
            try:
                tdesc = driver.find_element(By.XPATH,'/html/body/div[1]/section[2]/main').text
                break
            except NoSuchElementException as e:
                erros.append(e)
                tdesc.find()

        teste = 0
        print('\n'+nome)
        termos = Items.itens().termos
        for termo in termos:
            if tdesc.find(termo) > 0:
                teste += 1
                print(termo)
        if (teste >= 4):
            verf= True
        else:
            verf = False
        print('\n')
        self.verf = verf
        driver.quit()
