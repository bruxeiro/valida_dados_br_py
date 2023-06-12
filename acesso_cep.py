import requests


class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP INVÁLIDO")

    def __str__(self):
        return self.cep_format()

    def cep_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def cep_format(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def cep_acessa_viacep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()

        return(
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )