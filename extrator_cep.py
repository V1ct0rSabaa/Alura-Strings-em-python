import re

endereco: str = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 233440-120"
# [valores possiveis] {quantidade de vezes que aparece em seguida}
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereco) # Match, função que busca o padrão de string no texto, retorna None se não achar substring

if busca:
    cep: str = busca.group()
    print(f"o cep extraido é {cep}")
else:
    raise ValueError("essa string não contém um CEP")
