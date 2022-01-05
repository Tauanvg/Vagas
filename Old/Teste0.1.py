import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException
import time

from selenium.webdriver import Keys
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

import Items


class Crawler:
    def __init__(self, website='', nome=[], data=[], url=[], vrf=[]):
        path = r'C:/chromedriver_win32/chromedriver.exe'

        driver = webdriver.Chrome(path)
        driver.get(website)
        while True:
            try:
                button = driver.find_element('xpath', '//*[@id="dm876A"]')
                break
            except NoSuchElementException:
                time.sleep(0.3)
        button.click()
        pth = '//*[@id="root"]/div/div[1]/main/div[2]/nav/ul/li[sub]/button'
        o = 4
        erros = []

        Nome = './div/div[1]/a/h4'
        Data = './div/div/span'

        def pages(tentativaf):
            while True:
                finds = driver.find_elements(By.TAG_NAME, 'li')
                if len(finds) >= 20 or tentativaf > 6:
                    break
                else:
                    time.sleep(0.2)
                    tentativaf += 1
            for FD in finds:
                try:
                    tdata = FD.find_element(By.XPATH, Data).text
                    tdata = tdata.replace('Vaga publicada em: ', '')
                    tdata = datetime.datetime.strptime(tdata, '%d/%m/%Y')
                    hoje = datetime.datetime.today()
                    dif = hoje - tdata
                    tnome = FD.find_element(By.XPATH, Nome).text
                    turl = FD.find_element(By.TAG_NAME, 'a').get_attribute('href')
                    if dif.days < 3 and Items.itens.Negativo(tnome):
                        vrf.append(Items.itens.VRF(tnome))
                        url.append(turl)
                        nome.append(tnome)
                        data.append(tdata)
                except NoSuchElementException as e:
                    erros.append(e)
            if tentativaf > 6:
                lista = []
                return lista
            return finds


        def buttonA():
            while True:
                try:
                    button = driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/button')
                    break
                except NoSuchElementException:
                    time.sleep(0.1)
            button.click()
        def main(button):
            tentativas = 0
            while True:
                try:
                    button = driver.find_element(By.XPATH, 'button[@aria-label="Next Page"]')
                    break
                except NoSuchElementException:
                    tentativas += 1
                    time.sleep(0.3)
                    if tentativas > 3:
                        break
            pages(0)
            while True:
                try:
                    try:
                        try:
                            button.click()
                        except ElementClickInterceptedException:
                            buttonA()
                    except ElementNotInteractableException as e:
                        erros.append(e)
                except StaleElementReferenceException:
                    break
                tamanho = len(pages(0))

                if tamanho < 3:
                    break

                while True:
                    try:
                        o += 1
                        pthc = pth.replace('sub', str(o))
                        button = driver.find_element('xpath', pthc)
                        break
                    except NoSuchElementException:
                        o = 7
                        time.sleep(0.2)
                        try:
                            pthc = pth.replace('sub', str(o))
                            button = driver.find_element('xpath', pthc)
                            break
                        except NoSuchElementException:
                            o -= 1
                            try:
                                pthc = pth.replace('sub', str(o))
                                button = driver.find_element('xpath', pthc)
                                break
                            except NoSuchElementException:
                                break

        for pesquisa in Items.itens().pesquisa:
            print(pesquisa)
            while True:
                try:
                    preencher = driver.find_element(By.XPATH, '//*[@name="job-search-field"]')
                    ok = driver.find_element(By.XPATH, '//*[@id="job-search-field-button"]')
                    break
                except NoSuchElementException:
                    pass
            i = 0
            while i<30:
                preencher.send_keys(Keys.BACKSPACE)
                i+=1
            preencher.send_keys(pesquisa)
            ok.click()
            ok.click()
            main(button, 4)



        self.nome = nome
        self.data = data
        self.url = url
        self.vrf = vrf
        driver.quit()
