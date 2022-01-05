import datetime

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import Items


class Crawler:
    def __init__(self, website='', nome=None, data=None, url=None, vrf=None, empresa=None):
        if empresa is None:
            empresa = []
        if vrf is None:
            vrf = []
        if url is None:
            url = []
        if data is None:
            data = []
        if nome is None:
            nome = []

        path = r'C:/chromedriver_win32/chromedriver.exe'

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")

        driver = webdriver.Chrome(path, chrome_options=chrome_options)
        driver.get(website)

        def pages(finds):
            for FD in finds:
                teste = False
                try:
                    tnome = FD.find_element(By.CLASS_NAME, 'link-detalhes-vaga').get_attribute('title')
                    tdata = FD.find_element(By.CLASS_NAME, 'data-publicacao').text
                    turl = FD.find_element(By.CLASS_NAME, 'link-detalhes-vaga').get_attribute('href')
                    nome_e = FD.find_element(By.XPATH, './header/div[2]/span').text
                    hoje = datetime.datetime.today()
                    if tdata.find('Há') >= 0:
                        tdata = tdata.replace('Há ', '')
                        tdata = tdata.replace(' dias', '')
                        teste = True
                    elif tdata.find('Ontem') >= 0:
                        tdata = tdata.replace('Ontem', '2')
                        teste = True
                    elif tdata.find('Hoje') >= 0:
                        tdata = tdata.replace('Hoje', '1')
                        teste = True
                    if teste:
                        idata = int(tdata) - 1
                        tdata = hoje - datetime.timedelta(days=idata)
                    else:
                        tdata = datetime.datetime.strptime(tdata, '%d/%m/%Y')
                    vrf.append(Items.itens.VRF(tnome))
                    nome.append(tnome)
                    empresa.append(nome_e)
                    url.append(turl)
                    data.append(tdata)
                except NoSuchElementException:
                    pass

        def main(ant):
            tentativa = 0
            while True:
                tenta = 0
                while True:
                    try:
                        button = driver.find_element(By.XPATH, '//*[@id="maisVagas"]')
                        button.click()
                        break
                    except NoSuchElementException:
                        tenta += 1
                        if tenta > 10:
                            break
                        time.sleep(0.05)
                    except StaleElementReferenceException:
                        try:
                            button = driver.find_element(By.XPATH, '//*[@id="maisVagas"]')
                        except NoSuchElementException:
                            break
                        button.click()
                        break
                try:
                    div = driver.find_element(By.XPATH, '//*[@id="todasVagas"]')
                    finds = div.find_elements(By.TAG_NAME, 'li')
                    print(ant)
                    if ant == len(finds):
                        pages(finds)
                        break
                    else:
                        time.sleep(0.2)
                        ant = len(finds)
                except NoSuchElementException:
                    tentativa += 1
                    if tentativa > 1:
                        break

        def remoto():
            while True:
                try:
                    remote = driver.find_element(By.XPATH, '//*[@id="pesquisaFiltros"]/div[2]/div[1]/ul')
                    remote = remote.find_element(By.XPATH, '//*[text()[contains(.,"100% Home Office")]]')
                    while True:
                        try:
                            remote.click()
                            time.sleep(0.3)
                            break
                        except StaleElementReferenceException:
                            pass
                    break
                except NoSuchElementException:
                    pass

        def local():
            tentativa = 0
            while True:
                try:
                    local = driver.find_element(By.XPATH, '//*[@id="pesquisaFiltros"]/div[2]/div[2]/ul')
                    local = local.find_element(By.XPATH, '//*[text()[contains(.,"Rio de Janeiro")]]')
                    while True:
                        try:
                            local.click()
                            time.sleep(0.3)
                            break
                        except StaleElementReferenceException:
                            pass
                    break
                except NoSuchElementException:
                    tentativa += 1
                    if tentativa > 3:
                        break

        '''
        for pesquisa in Items.itens().pesquisa:
            print('\n------------------', pesquisa, '----------------------')

            while True:
                try:
                    preencher = driver.find_element(By.XPATH, '//*[@id="search-input-header"]')
                    break
                except NoSuchElementException:
                    pass
            time.sleep(0.1)
            preencher.clear()
            preencher.send_keys(pesquisa)
            preencher.send_keys(Keys.ENTER)
            ver = driver.find_elements(By.XPATH, '//*[@id="pesquisaFiltros"]/div[2]/div[1]/ul')
            for li in ver:
                try:
                    li.find_element(By.XPATH, '//li[@class="aplicado"]')
                except NoSuchElementException:
                    remoto()
            #time.sleep(0.4)
            main(0)
        remoto()
        '''
        for pesquisa in Items.itens().pesquisa:
            print('\n------------------', pesquisa, '----------------------')
            while True:
                try:
                    preencher = driver.find_element(By.XPATH, '//*[@id="search-input-header"]')
                    break
                except NoSuchElementException:
                    pass
            time.sleep(0.1)
            preencher.clear()
            preencher.send_keys(pesquisa)
            preencher.send_keys(Keys.ENTER)
            ver = driver.find_elements(By.XPATH, '//*[@id="pesquisaFiltros"]/div[2]/div[2]/ul')
            for li in ver:
                try:
                    li.find_element(By.XPATH, '//li[@class="aplicado"]')
                    break
                except NoSuchElementException:
                    local()
                    break
            #time.sleep(0.4)
            main(0)

        self.nome = nome
        self.data = data
        self.url = url
        self.vrf = vrf
        self.empresa = empresa
        driver.quit()
