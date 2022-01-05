import datetime
import items as items
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException, JavascriptException
import time

from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By

import Items


class Crawler:
    def __init__(self, website='', nome=[], data=[], url=[], vrf=[], empresa=[]):
        global remote, ok, local
        path = r'C:/chromedriver_win32/chromedriver.exe'
        driver = webdriver.Chrome(path)
        driver.set_window_size(2000, 3000)
        driver.get(website)

        while True:
            try:
                entrar = driver.find_element(By.CLASS_NAME, 'nav__button-secondary')
                entrar.click()
                time.sleep(0.4)
                break
            except NoSuchElementException:
                time.sleep(0.2)
        while True:
            try:
                email = driver.find_element(By.XPATH, '//*[@id="username"]')
                email.send_keys('tauanvg@hotmail.com')
                senha = driver.find_element(By.XPATH, '//*[@id="password"]')
                senha.send_keys('talles15')
                entrar = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
                entrar.click()
                time.sleep(0.4)
                break
            except StaleElementReferenceException:
                time.sleep(0.2)
        C = 2
        xp = '//button[@aria-label="Página sub"]'

        def Linhas(tenta):
            while True:
                try:
                    block = driver.find_element(By.XPATH, '//ul[@itemtype="http://schema.org/ItemList"]')
                    driver.execute_script(f'document.querySelector("ul[itemtype]").style.zoom="{22}%"')
                    driver.execute_script(f'document.querySelector("header[tabindex]").style.zoom="{1}%"')
                    driver.execute_script(f'document.getElementById("global-nav").style.zoom="{1}%"')
                    driver.execute_script(f'document.querySelector("section[aria-label]").style.zoom="{1}%"')
                    time.sleep(0.1)
                    while True:
                        ul = driver.find_element(By.XPATH, '//ul[@itemtype="http://schema.org/ItemList"]')
                        try:
                            finds = ul.find_elements(By.XPATH, './li')
                            break
                        except StaleElementReferenceException:
                            pass
                    if len(finds) >= 24 or tenta >= 3:
                        break
                    else:
                        time.sleep(0.1)
                        tenta += 1
                except NoSuchElementException:
                    pass
                except JavascriptException:
                    driver.refresh()
            return finds

        def vaga(Achados, c):
            for FD in Achados:
                while True:
                    try:
                        tnome = FD.find_element(By.XPATH, './div/div/div[1]/div[2]/div[1]/a').text
                        tdata = FD.find_element(By.TAG_NAME, 'time').get_attribute('datetime')
                        turl = FD.find_element(By.XPATH, './div/div/div[1]/div[2]/div[1]/a').get_attribute('href')
                        site = FD.find_element(By.XPATH, './div/div/div[1]/div[2]/div[2]').text
                        c += 1
                        tdata = datetime.datetime.strptime(tdata, '%Y-%m-%d')
                        vrf.append(Items.itens.VRF(tnome))
                        empresa.append(site)
                        nome.append(tnome)
                        url.append(turl)
                        data.append(tdata)
                        break
                    except NoSuchElementException:
                        break
                    except StaleElementReferenceException:
                        break

            return c

        def Button(C):
            numero = xp.replace('sub', str(C))
            tenta = 0
            driver.execute_script(f'document.body.style.zoom="{100}%"')
            while True:
                try:
                    button = driver.find_element(By.XPATH, numero)
                    try:
                        button.click()
                        time.sleep(0.1)
                        C += 1
                        break
                    except StaleElementReferenceException:
                        button = driver.find_element(By.XPATH, numero)
                        button.click()
                        time.sleep(0.1)
                        C += 1
                        break
                except NoSuchElementException:
                    tenta += 1
                    time.sleep(0.1)
                    if tenta > 5:
                        break
            return C

        def Local():
            Menu()
            while True:
                try:
                    local = driver.find_element(By.XPATH,
                                                '/html/body/div[3]/div/div/div[2]/ul/li[8]/fieldset/div/ul')
                    local = local.find_element(By.XPATH, '//*[text()[contains(.,"Rio de Janeiro, RJ")]]')
                    break
                except StaleElementReferenceException:
                    time.sleep(0.05)
                except NoSuchElementException:
                    print('Abrir')
                    Menu()
            while True:
                try:
                    find = driver.find_element(By.XPATH,
                                               '/html/body/div[6]/div[3]/div[3]/section/div/div/div/ul/li['
                                               '4]/div/span/button').get_attribute(
                        'aria-label')
                    while find.find('aplicado') >= 0:
                        try:
                            local.click()
                        except ElementNotInteractableException:
                            Menu()
                        except ElementClickInterceptedException:
                            pass
                        Ok()

                        if find.find('aplicado') >= 0:
                            break
                    break
                except StaleElementReferenceException:
                    try:
                        local = driver.find_element(By.XPATH,
                                                    '/html/body/div[3]/div/div/div[2]/ul/li[8]/fieldset/div/ul')
                        local = local.find_element(By.XPATH, '//*[text()[contains(.,"Rio de Janeiro, RJ")]]')
                    except NoSuchElementException:
                        Menu()

        def Remote():
            Menu()
            while True:
                try:
                    remote = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/ul/li[6]/fieldset/div/ul')
                    remote = remote.find_element(By.XPATH, '//*[text()[contains(.,"Remoto")]]')
                    break
                except StaleElementReferenceException:
                    pass
                except NoSuchElementException:
                    Menu()
            while True:
                try:
                    while True:
                        try:
                            remote.click()
                        except ElementNotInteractableException:
                            Menu()
                        except ElementClickInterceptedException:
                            pass
                        Ok()
                        find = driver.find_element(By.XPATH,
                                                   '/html/body/div[6]/div[3]/div[3]/section/div/div/div/ul/li[4]/div/span/button').get_attribute(
                            'aria-label')
                        if find.find('aplicado') >= 0:
                            break
                        break
                    break
                except StaleElementReferenceException:
                    try:
                        remote = driver.find_element(By.XPATH,
                                                     '/html/body/div[3]/div/div/div[2]/ul/li[6]/fieldset/div/ul')
                        remote = remote.find_element(By.XPATH, '//*[text()[contains(.,"Remoto")]]')
                    except NoSuchElementException:
                        Menu()

        def Main(Ant, c, C):
            while True:
                finds = Linhas(0)
                linha = 0
                for f in finds:
                    try:
                        print(linha, '-', f.text)
                    except StaleElementReferenceException:
                        pass
                    linha += 1

                c = vaga(finds, c)
                C = Button(C)
                if C == Ant:
                    break
                else:
                    Ant = C
                if len(finds) < 3:
                    break
            print('Total de vagas: ', c)

        def Menu():
            while True:
                try:
                    menu = driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/div/div')
                    menu = menu.find_element(By.XPATH, '//button[@aria-label="Todos os filtros"]')
                    break
                except NoSuchElementException:
                    time.sleep(0.05)
            while True:
                try:
                    menu.click()
                    break
                except StaleElementReferenceException:
                    pass

        def Ok():
            while True:
                try:
                    ok = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]')
                    ok = ok.find_element(By.XPATH, '//div/button[2]')
                    break
                except NoSuchElementException or StaleElementReferenceException:
                    time.sleep(0.05)
            while True:
                try:
                    ok.click()
                    break
                except StaleElementReferenceException:
                    ok = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]')
                    ok = ok.find_element(By.XPATH, '//div/button[2]')
                except ElementNotInteractableException:
                    break

        def Preencher(pesquisa):
            while True:
                try:
                    preencher = driver.find_element(By.XPATH,
                                                    '//*[@aria-label="Pesquisar cargo, competência ou empresa"]')
                    break
                except NoSuchElementException:
                    pass
            driver.execute_script(f'document.querySelector("header[tabindex]").style.zoom="{100}%"')
            driver.execute_script(f'document.getElementById("global-nav").style.zoom="{100}%"')
            driver.execute_script(f'document.querySelector("section[aria-label]").style.zoom="{100}%"')
            time.sleep(0.3)
            preencher.clear()
            preencher.send_keys(pesquisa)
            preencher.send_keys(Keys.ENTER)

        for pesquisa in Items.itens().pesquisa:
            for pesquisaA in Items.itens().pesquisaavancada:
                pesquisaalt = pesquisa + pesquisaA
                print('\n------------------', pesquisaalt, '----------------------')
                Preencher(pesquisaalt)
                Main(0, 0, 2)

        self.nome = nome
        self.data = data
        self.url = url
        self.vrf = vrf
        self.empresa = empresa
        driver.quit()
