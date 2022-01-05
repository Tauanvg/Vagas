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
        driver.set_window_size(2000,3000)
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
                    ul = driver.find_element(By.XPATH, '//ul[@itemtype="http://schema.org/ItemList"]')
                    finds = ul.find_elements(By.XPATH, './li')
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
                        hoje = datetime.datetime.today()
                        if hoje.isoweekday() == 1:
                            limite = 3
                        else:
                            limite = 1
                        dif = hoje - tdata
                        #and Items.itens.Negativo(tnome) and Items.itens.NegativoS(site)
                        if dif.days <= limite:
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
        def local(filtro):
            while True:
                local = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/ul/li[8]/fieldset/div/ul')
                while True:
                    try:
                        local = local.find_element(By.XPATH, '//*[text()[contains(.,"Rio de Janeiro, RJ")]]')
                        break
                    except StaleElementReferenceException:
                        local = driver.find_element(By.XPATH,
                                                    '/html/body/div[3]/div/div/div[2]/ul/li[8]/fieldset/div/ul')
                break
            while True:
                try:
                    if not local.is_selected():
                        local.click()
                        break
                    elif filtro:
                        local.click()
                        break
                    else:
                        break
                except StaleElementReferenceException:
                    local = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/ul/li[8]/fieldset/div/ul')
                    while True:
                        try:
                            local = local.find_element(By.XPATH, '//*[text()[contains(.,"Rio de Janeiro, RJ")]]')
                            break
                        except StaleElementReferenceException:
                            local = driver.find_element(By.XPATH,
                                                        '/html/body/div[3]/div/div/div[2]/ul/li[8]/fieldset/div/ul')
                except ElementClickInterceptedException:
                    time.sleep(0.05)
        def remote(filtro):
            while True:
                try:
                    if not remote.is_selected() :
                        remote.click()
                        break
                    elif filtro:
                        remote.click()
                        break
                    else:
                        break
                except StaleElementReferenceException:
                    pass
                    remote = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/ul/li[6]/fieldset/div/ul')
                    while True:
                        try:
                            remote = remote.find_element(By.XPATH, '//*[text()[contains(.,"Remoto")]]')
                            break
                        except StaleElementReferenceException:
                            remote = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/ul/li[6]/fieldset/div/ul')

        def main(Ant, c, C):
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
        for pesquisa in Items.itens().pesquisa:
            print('\n------------------', pesquisa, '----------------------')
            while True:
                try:
                    preencher = driver.find_element(By.XPATH, '//*[@aria-label="Pesquisar cargo, competência ou empresa"]')
                    break
                except NoSuchElementException:
                    pass
            driver.execute_script(f'document.querySelector("header[tabindex]").style.zoom="{100}%"')
            driver.execute_script(f'document.getElementById("global-nav").style.zoom="{100}%"')
            driver.execute_script(f'document.querySelector("section[aria-label]").style.zoom="{100}%"')
            time.sleep(0.5)
            preencher.clear()
            preencher.send_keys(pesquisa)
            preencher.send_keys(Keys.ENTER)
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
                    #time.sleep(0.4)
                    break
                except StaleElementReferenceException :
                    ok = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[3]/section/div/div/div/div/div/button')
            #time.sleep(1.2)
            tenta = 0
            while True:
                try:
                    ok = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]')
                    ok = ok.find_element(By.XPATH, '//div/button[2]')
                    break
                except NoSuchElementException:
                    time.sleep(0.05)
                    tenta += 1
                    if tenta>15:
                        break
                except StaleElementReferenceException:
                    remote = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/ul/li[6]/fieldset/div/ul')

            while True:
                try:
                    ok.click()
                    break
                except StaleElementReferenceException :
                    ok = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]')
                    ok = ok.find_element(By.XPATH, '//div/button[2]')
            main(0, 0, 2)
        for pesquisa in Items.itens().pesquisa:
            print('\n------------------', pesquisa, '----------------------')
            while True:
                try:
                    preencher = driver.find_element(By.XPATH, '//*[@aria-label="Pesquisar cargo, competência ou empresa"]')
                    break
                except NoSuchElementException:
                    pass
            driver.execute_script(f'document.querySelector("header[tabindex]").style.zoom="{100}%"')
            driver.execute_script(f'document.getElementById("global-nav").style.zoom="{100}%"')
            driver.execute_script(f'document.querySelector("section[aria-label]").style.zoom="{100}%"')
            time.sleep(0.5)
            preencher.clear()
            preencher.send_keys(pesquisa)
            preencher.send_keys(Keys.ENTER)
            while True:
                try:
                    menu = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[3]/section/div/div/div/div/div/button')
                    break
                except NoSuchElementException:
                    time.sleep(0.05)
            while True:
                try:
                    menu.click()
                    break
                except StaleElementReferenceException :
                    ok = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[3]/section/div/div/div/div/div/button')
            local(False)
            remote(True)
            while True:
                try:
                    ok = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[3]/section/div/div/div/div/div/button')
                    ok.click()
                    break
                except StaleElementReferenceException or ElementNotInteractableException or StaleElementReferenceException:
                    ok = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]')
                    ok = ok.find_element(By.XPATH, './div/button[2]')
            main(0, 0, 2)



        self.nome = nome
        self.data = data
        self.url = url
        self.vrf = vrf
        self.empresa = empresa
        driver.quit()
