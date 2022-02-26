#Imports necessários
from requests import get
from time import sleep

#Funções necessárias
def NumeroMoedaParaString(numeroMoeda):
    stringMoeda = ''
    if(numeroMoeda == 1):
        stringMoeda = 'BRL'
        simboloMoeda = 'R$'
    elif(numeroMoeda == 2):
        stringMoeda = 'USD'
        simboloMoeda = 'US$'
    elif(numeroMoeda == 3):
        stringMoeda = 'EUR'
        simboloMoeda = '€'
    else:
        stringMoeda = 'GBP'
        simboloMoeda = '£'
    return [stringMoeda,simboloMoeda]

def Conversor(primeiraConversao=0):
    #Apresentar o aplicativo
    if(primeiraConversao):
        stringApresentacao = "O aplicativo serve para converter o valor de uma moeda para a outra" + "\n"
        stringApresentacao += "Para indicar a moeda, utilizamos um sistema de número" + "\n"
        stringApresentacao += "Real Brasileiro = 1" + "\n"
        stringApresentacao += "Dólar Americano = 2" + "\n"
        stringApresentacao += "Euro = 3" + "\n"
        stringApresentacao += "Libra Esterlina = 4"
        print(stringApresentacao)

    #Receber moeda origem
    moedaOrigem = 2
    try:
        moedaOrigem = int(input("Digite a moeda origem: "))
    except:
        moedaOrigem = 2
    if(moedaOrigem < 1 or moedaOrigem > 4):
        moedaOrigem = 2

    #Receber moeda destino
    moedaDestino = 1
    try:
        moedaDestino = int(input("Digite a moeda destino: "))
    except:
        moedaDestino = 1
    if(moedaDestino < 1 or moedaDestino > 4):
        moedaDestino = 1

    #Receber valor que vai ser convertido
    valorParaConversao = 1.00
    try:
        valorParaConversao = input("Digite o valor a ser convertido: ")
        valorParaConversao = valorParaConversao.replace(",", ".")
        valorParaConversao = float(valorParaConversao)
    except:
        valorParaConversao = 1.00
    if(valorParaConversao <= 0):
        valorParaConversao = 1.00

    #Converter o número passado para a string correspondente a moeda
    arrayOrigem = NumeroMoedaParaString(moedaOrigem)
    moedaOrigem = arrayOrigem[0]
    simboloMoedaOrigem = arrayOrigem[1]
    arrayDestino = NumeroMoedaParaString(moedaDestino)
    moedaDestino = arrayDestino[0]
    simboloMoedaDestino = arrayDestino[1]

    #Realizar a conversão
    sleep(1)
    if(primeiraConversao):
        print('Será usado o "." como separador decimal')
    sleep(1)
    print(f'Conversão de {simboloMoedaOrigem}{valorParaConversao} para {simboloMoedaDestino}')
    conversao = get(f'http://economia.awesomeapi.com.br/json/last/{moedaOrigem}-{moedaDestino}').json()
    precoCompra = float(conversao[moedaOrigem+moedaDestino]['ask'])
    precoVenda = float(conversao[moedaOrigem+moedaDestino]['bid'])
    sleep(1)
    print('Usando preço de compra: {}{} * {} = {}{:.3f}'.format(simboloMoedaOrigem,valorParaConversao,precoCompra,simboloMoedaDestino,valorParaConversao*precoCompra))
    sleep(1)
    print('Usando preço de venda: {}{} * {} = {}{:.3f}'.format(simboloMoedaOrigem,valorParaConversao,precoVenda,simboloMoedaDestino,valorParaConversao*precoVenda))
Conversor(1)
while(True):
    sleep(60)
    continuar = input("Deseja continuar? (Sim ou Não): ").upper()[0]
    if(continuar == 'S'):
        Conversor()
    else:
        break
