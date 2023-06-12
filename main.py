import requests

from acesso_cep import BuscaEndereco

cep = 93804494

cepe = BuscaEndereco(cep)

print(cepe)

r = requests.get("https://viacep.com.br/ws/01001000/json/")
print(r.text)

bairro, cidade, uf = cepe.cep_acessa_viacep()

print(bairro, cidade, uf)