import yfinance as yf
from datetime import datetime as dt
from datetime import timedelta
from openpyxl import *
import os
import time

#Bem vindo
print("Seja bem-vindo ao GET Bolsa de Valores.\n")
time.sleep(5)
print("Esse é um código simples. Será solicitado no terminal algumas interações com o usuário. Basta escolher o ticker (ação), a data de início da busca, e a data final, ao final um arquivo em formato .XLSX será salvo no mesmo diretório em que esse projeto está salvo.\n")
time.sleep(12)
print("Esse sistema é baseada na biblioteca 'YahooFinance' e está configurada para receber entradas e fornecer saídas todas em padrão americano (ticker, data e etc).\n")
time.sleep(7)
print("Além disso, no momento apenas ações com tickers dos Estados Unidos estão operantes.\n")
time.sleep(4)
print("Em futuras versões será incluída algumas funções e melhorias no código, como: Janela interativa,  data em formato brasileiro, lista suspensa com todos os tickers, possibilidade de outras bolsas e etc.\n")
time.sleep(13)
print("Dúvidas e sugestões entre em contato pelo GitHub =)\n")
time.sleep(3)
print("Iniciando GET Bolsa")
time.sleep(5)

#Definindo ticker
ticker = input('\nPara pesquisar um ativo digite o ticker.\nPara pesquisar por "AAPL" (Apple) pressione a tecla "Enter".\n')
if not ticker:
    ticker =  "AAPL"

#Definindo data de início
data_inicio = input('\nDigite a data de início da busca. (aaaa-mm-dd)\nPara usar a data 30 dias antes pressione a tecla"Enter".\n')
if not data_inicio:
    data_inicio_30d = dt.now() - timedelta(days=30)
    data_inicio = data_inicio_30d.strftime('%Y-%m-%d') 
    
print('\nData de início definida para '+data_inicio)

#Definindo data de fim
data_fim = input('\nDigite a data de fim da busca. (aaaa-mm-dd)\nPara usar a data de hoje pressione a tecla "Enter".\n')
if not data_fim:
    data_fim = dt.now().strftime('%Y-%m-%d')

print('\nData fim definida para '+data_fim+'\n')

#Pesquisando ticker
print("Fazendo download do histórico de "+ticker+".")
pesquisa_ticker = yf.download(ticker, start=data_inicio, end=data_fim)

#Salvando resultados em um XLSX
pesquisa_ticker.to_excel(ticker+".xlsx", index=True)
cd = os.getcwd()
print("Dados salvos em "+cd+"\n")