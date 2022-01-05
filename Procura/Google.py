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
    def __init__(self, website='', nome=[], data=[], url=[], vrf=[], empresa=[]):
        path = r'C:/chromedriver_win32/chromedriver.exe'
        teste = []

        driver = webdriver.Chrome(path)
        driver.get(website)
        def pages():
            tentativas = 0
            while True:
                try:
                    ul = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/div/div[3]/div[1]/div[1]/div[4]/div[6]/div/ul')
                    break
                except NoSuchElementException:
                    tentativas += 1
                    time.sleep(0.3)
                    if tentativas > 10:
                        return []
            finds = ul.find_elements(By.XPATH, './li')
            for FD in finds:
                try:
                    tdata = FD.find_element(By.CLASS_NAME, 'SuWscb').text
                    print(tdata)
                    tdata = tdata.replace('Vaga publicada em: ', '')
                    tdata = datetime.datetime.strptime(tdata, '%d/%m/%Y')
                    tnome = FD.find_element(By.CLASS_NAME, 'BjJfJf PUpOsf').text
                    nome_e = FD.find_element(By.CLASS_NAME, 'vNEEBe').text
                    button = FD.find_element(By.CLASS_NAME, 'BjJfJf PUpOsf')
                    button.click()
                    turl = FD.find_element(By.XPATH, '//div/div/span/a').get_attribute('href')
                    if Items.itens.Positivo():
                        empresa.append(nome_e)
                        vrf.append(True)
                        url.append(turl)
                        nome.append(tnome)
                        data.append(tdata)
                except NoSuchElementException:
                    pass
            return finds

        for pesquisa in Items.itens().pesquisa:
            #driver.execute_script(f'document.body.style.zoom="{100}%"')
            print('\n------------------', pesquisa, '----------------------')
            while True:
                try:
                    preencher = driver.find_element(By.XPATH, '//*[@id="hs-qsb"]')
                    preencher.clear()
                    break
                except NoSuchElementException:
                    pass
            preencher.send_keys(pesquisa)
            preencher.send_keys(Keys.ENTER)
            pages()


        self.nome = nome
        self.data = data
        self.url = url
        self.vrf = vrf
        self.test = teste
        self.empresa = empresa
        driver.quit()
