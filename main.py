

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

# Sanitização da URL
# poderia ser usado também-> url = url.replace(" ", "")
# substituindo os espaços vazio por nenhum espaço
url = url.strip()

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia")

# Seapração da URL base dos parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]

parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1

indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)

