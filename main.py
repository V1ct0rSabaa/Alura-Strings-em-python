from extrator_url import Extrator_url
url: str = "bytbank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

url_formatada = Extrator_url(url)

print(url_formatada)
print(url_formatada.base_url)