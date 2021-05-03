"""Agora que conseguimos extrair valores da nossa URL como moeda de origem, moeda de destino e quantidade de moeda,
proponho a você o desafio de realizar essa conversão.
Modifique o nosso projeto, levando em conta o valor do dólar em real (por exemplo: DOLAR = 5.50), para, sabendo o valor
do dólar em real (por exemplo: DOLAR = 5.50), ler da URL os 3 parâmetros (origem, destino e quantidade)
e imprimir na tela o valor da conversão.
Observação: pode assumir que a moeda de origem e destino será sempre “real” ou “dolar”, ou seja,
só faremos a conversão de dólar para real e vice-versa.
"""

from extrator_url import ExtratorUrl

url_de_teste = "www.bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
valor_dolar = 5.50  # $1.00 = R$5.50

url = ExtratorUrl(url_de_teste)
origem = url.get_valor_parametro("moedaOrigem")
destino = url.get_valor_parametro("moedaDestino")
quantidade = int(url.get_valor_parametro("quantidade"))

if origem == 'dolar':
    valor_convertido = quantidade*valor_dolar
else:
    valor_convertido = quantidade/valor_dolar

print("o valor para conversão é: " + str(quantidade))
print("a moeda de origem é: " + origem)
print("a moeda de destino é: " + destino)
print("O valor total da conversão é de: " + str(valor_convertido))


