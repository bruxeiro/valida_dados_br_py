from validate_docbr import CPF, CNPJ


class Document:

    @staticmethod
    def cria_documento(document):

        if len(document) == 11:
            return DocCpf(document)

        elif len(document) == 14:
            return DocCnpj(document)

        else:
            raise ValueError("Quantidade de digitos está incorreta")


class DocCpf:

    def __init__(self, document):
        document = str(document)
        if self.cpf_valido(document):
            self.document = document
        else:
            raise ValueError("CPF INVALIDO")

    def cpf_valido(self, document):
        validador = CPF()
        return validador.validate(document)

    def cpf_formata(self):
        mascara = CPF()
        return mascara.mask(self.document)

    def __str__(self):
        return self.cpf_formata()


class DocCnpj:

    def __init__(self, document):
        document = str(document)
        if self.cnpj_valido(document):
            self.document = document
        else:
            raise ValueError("CPF INVALIDO")

    def cnpj_valido(self, document):
        validador = CNPJ()
        return validador.validate(document)

    def cnpj_formata(self):
        mascara = CPF()
        return mascara.mask(self.document)
