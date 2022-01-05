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
        while True:
            try:
                button = driver.find_element('xpath', '//*[@id="dm876A"]')
                break
            except NoSuchElementException:
                time.sleep(0.3)
        button.click()

        def pages():
            tentativas = 0
            while True:
                try:
                    ul = driver.find_element(By.XPATH, '//ul[@aria-label="job-list"]')
                    teste.append(ul.text)
                    break
                except NoSuchElementException:
                    tentativas += 1
                    time.sleep(0.3)
                    if tentativas > 3:
                        return []
            finds = ul.find_elements(By.XPATH, './li')
            for FD in finds:
                try:
                    tdata = FD.find_element(By.XPATH, './div/div[1]/span').text
                    tdata = tdata.replace('Vaga publicada em: ', '')
                    tdata = datetime.datetime.strptime(tdata, '%d/%m/%Y')
                    tnome = FD.find_element(By.XPATH, './div/div[1]/a/h4').text
                    nome_e = FD.find_element(By.XPATH, './div/div[1]/div').text
                    turl = FD.find_element(By.TAG_NAME, 'a').get_attribute('href')
                    empresa.append(nome_e)
                    vrf.append(Items.itens.VRF(tnome))
                    url.append(turl)
                    nome.append(tnome)
                    data.append(tdata)
                except NoSuchElementException:
                    pass
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
                    button = driver.find_element(By.XPATH, '//button[@aria-label="Next Page"]')
                    break
                except NoSuchElementException:
                    tentativas += 1
                    time.sleep(0.3)
                    if tentativas > 3:
                        print('Não achou')
                        break

            tenta = 0
            tamanho = 0
            while True:
                if tamanho > 0:
                    try:
                        try:
                            try:
                                button.click()
                                tamanho = len(pages())
                                print('\nVagas na pagina: ', tamanho)
                            except ElementClickInterceptedException:
                                buttonA()
                                tenta += 1
                                if tenta >= 3:
                                    break
                        except ElementNotInteractableException:
                            tenta += 1
                            if tenta >= 3:
                                break
                    except StaleElementReferenceException:
                        button = driver.find_element(By.XPATH, '//button[@aria-label="Next Page"]')
                if tamanho < 1:
                    tamanho = len(pages())
                    print('\nVagas na pagina: ', tamanho)
                    if tamanho < 15:
                        break
                vrf = driver.find_element(By.XPATH, '//button[@aria-label="Next Page"]').get_attribute(
                    'aria-disabled')
                #print(vrf)
                if vrf == 'true':
                    break


        for pesquisa in Items.itens().pesquisa:
            #driver.execute_script(f'document.body.style.zoom="{100}%"')
            print('\n------------------', pesquisa, '----------------------')
            while True:
                try:
                    preencher = driver.find_element(By.XPATH, '//*[@name="job-search-field"]')
                    ok = driver.find_element(By.XPATH, '//*[@aria-label="Pesquisar vagas"]')
                    break
                except NoSuchElementException:
                    pass
            i = 0
            while i<30:
                preencher.send_keys(Keys.BACKSPACE)
                i+=1
            preencher.send_keys(pesquisa)
            while True:
                try:
                    ok.click()
                    ok.click()
                    break
                except ElementClickInterceptedException:
                    buttonA()
            main(button)


        self.nome = nome
        self.data = data
        self.url = url
        self.vrf = vrf
        self.test = teste
        self.empresa = empresa
        driver.quit()
