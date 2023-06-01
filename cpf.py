
class CPF:

    def __init__(self, document):
        document = str(document)
        if self.cpf_valido(document):
            self.document = document
        else:
            raise ValueError("CPF INVALIDO")


    def cpf_valido(self, document):
        self.document= document
        if len(self.document) == 11:
            return True
        else:
            return False