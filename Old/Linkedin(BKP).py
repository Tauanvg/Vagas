import datetime

import items as items
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException
import time

from selenium.webdriver.common.by import By

import Items


class Crawler:
    def __init__(self, website='', nome=[], data=[], url=[], vrf=[]):
        path = r'C:/chromedriver_win32/chromedriver.exe'

        driver = webdriver.Chrome(path)
        driver.get(website)
        while True:
            try:
                entrar = driver.find_element(By.CLASS_NAME, 'nav__button-secondary')
                entrar.click()
                break
            except NoSuchElementException:
                print('Aqui')
                time.sleep(0.2)
        while True:
            try:
                email = driver.find_element(By.XPATH, '//*[@id="username"]')
                email.send_keys('tauanvg@hotmail.com')
                senha = driver.find_element(By.XPATH, '//*[@id="password"]')
                senha.send_keys('talles15')
                entrar = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
                entrar.click()
                break
            except StaleElementReferenceException:
                print('Aqui')
                time.sleep(0.2)

        while True:
            while True:
                try:
                    try:
                        button = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[2]/button')
                        button.click()
                        button.click()
                        time.sleep(1)
                    except BaseException as e:
                        pass
                    finds = driver.find_elements_by_tag_name('li')
                    print(len(finds))
                    break
                except NoSuchElementException:
                    pass
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            if Ant == len(finds):
                break
            else:
                time.sleep(1.7)
                Ant = len(finds)

        erros = []

        for FD in finds:
            try:
                tnome = FD.find_element(By.CLASS_NAME, 'base-search-card__title').text
                tdata = FD.find_element(By.TAG_NAME, 'time').get_attribute('datetime')
                turl = FD.find_element(By.TAG_NAME, 'a').get_attribute('href')
                tdata = datetime.datetime.strptime(tdata, '%Y-%m-%d')
                hoje = datetime.datetime.today()
                dif = hoje - tdata
                if dif.days < 3 and Items.itens.Negativo(tnome):
                    vrf.append(Items.itens.VRF(tnome))
                    nome.append(tnome)
                    url.append(turl)
                    data.append(tdata)
            except NoSuchElementException as e:
                erros.append(e)
        self.nome = nome
        self.data = data
        self.url = url
        self.vrf = vrf
        driver.quit()
