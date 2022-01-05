import datetime

import datetime as datetime
import pandas as pd
import Items
from Procura import Linkedin, Teste, Vgas, Google
from Verifica import VgasV, LKDL, Teste2

def leitura(link, vrf, nome):
    if vrf:
        return True
    elif link.find('gupy') > 0:
        Info2 = Teste2.Crawler(link, nome)
        return Info2.verf
    elif link.find('link') > 0:
        Info2 = LKDL.Crawler(link, nome)
        return Info2.verf
    elif link.find('vagas') > 0:
        Info2 = VgasV.Crawler(link, nome)
        return Info2.verf




for linkI in Items.itens().url:
    print(linkI)
    if linkI.find('gupy') > 0:
        try:
            Info = Teste.Crawler(linkI, Info.nome, Info.data, Info.url, Info.vrf, Info.empresa)
        except NameError:
            Info = Teste.Crawler(linkI)
    elif linkI.find('link') > 0:
        try:
            Info = Linkedin.Crawler(linkI, Info.nome, Info.data, Info.url, Info.vrf, Info.empresa)
        except NameError:
            Info = Linkedin.Crawler(linkI)
    elif linkI.find('vagas') > 0:
        try:
            Info = Vgas.Crawler(linkI, Info.nome, Info.data, Info.url, Info.vrf, Info.empresa)
        except NameError:
            Info = Vgas.Crawler(linkI)
    elif linkI.find('google') > 0:
        try:
            Info = Google.Crawler(linkI, Info.nome, Info.data, Info.url, Info.vrf, Info.empresa)
        except NameError:
            Info = Google.Crawler(linkI)



nome = Info.nome
url = Info.url
data = Info.data
vrf = Info.vrf
empresa = Info.empresa
df = pd.DataFrame({'Nome': nome, 'Empresa':empresa, 'Data': data, 'Link': url, 'Verificado': vrf})
df.drop_duplicates(subset=['Nome', 'Empresa'], keep='first', inplace=True)
df.drop_duplicates('Link', inplace=True)
lista = []
cont = 0
def limite(tdata):
    hoje = datetime.datetime.today()
    if hoje.isoweekday() == 1:
        limite = 3
    else:
        limite = 1
    dif = hoje - tdata
    if dif.days > limite:
        return True
    return False

#df.reset_index(drop=True, inplace=True)
hoje = datetime.datetime.today()

dfe = df


for index, row in df.iterrows():
    try:
        dif = hoje - row['Data']
        if dif.days > 1:
            print(row['Nome'], '---------->', dif.days, ' dias')
            df.drop(index, inplace=True)
        elif Items.itens.Negativo(row['Nome']):
            df.drop(index, inplace=True)
        elif Items.itens.NegativoS(row['Empresa'], row['Nome']):
            df.drop(index, inplace=True)
        elif not leitura(row['Link'], row['Verificado'], row['Nome']) and not row['Verificado']:
            df.drop(index, inplace=True)
    except KeyError as e:
        print(e)

df.drop('Verificado', axis=1, inplace=True)

hoje = datetime.datetime.today().strftime('%d-%m-%Y')
df.to_csv('Resultado/teste.csv', index=False)
df.to_xml('Resultado/teste.xml', index=False)
df.to_excel(f'Resultado/{hoje}.xlsx', index=False)
dfe.to_excel(f'Resultado/E:{hoje}.xlsx', index=False)
