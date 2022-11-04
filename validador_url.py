import re

padrao_url = re.compile("(http(s){0,1}://){0,1}(www.){0,1}bytebank.com(.br){0,1}/cambio")

match = padrao_url.match("https://bytebank.com/cambio")

def checar_url(url_testada: str) -> str:
    global padrao_url
    texto: str = ""
    if padrao_url.match(url_testada):
        texto = f"URL válida: {url_testada}"
    else:
        texto = f"URL inválida: {url_testada}"
    return texto


# testando exemplos de url

exemplos: list[str] = ["bytebank.com/cambio", "bytebank.com.br/cambio",
                       "www.bytebank.com/cambio", "www.bytebank.com.br/cambio",
                       "http://www.bytebank.com/cambio", "http://www.bytebank.com.br/cambio",
                       "https://www.bytebank.com/cambio","https://www.bytebank.com.br/cambio",
                       "https://bytebank/cambio", "http://bytebank.naoexiste/cambio"]

for url in exemplos:
    print(checar_url(url))

