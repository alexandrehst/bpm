class Acao:
    def __init__(self, descricao):
        self.descricao = descricao
    def __str__(self):
        return self.descricao

class AcaoTransicao(Acao):
    def __init__(self, descricao, atividade_destino):
        super().__init__(descricao)
        self.atividade_destino = atividade_destino

    def executa(self):
        return self.atividade_destino

class AcaoCancelamento(Acao):
    pass

class AcaoTransferencia(Acao):
    pass