class Atividade:
    def __init__(self, descricao):
        self.descricao = descricao
        self.acoes = []
    
    def adiciona_acao(self, acao ):
        self.acoes.append (acao)

    def __str__(self):
        retorno = "ATIVIDADE: " + self.descricao + "\n"

        for acao in self.acoes:
            retorno += str(acao) + "\n"
        
        return retorno

class EventoFinal(Atividade):
    def __init__(self, descricao):
        super().__init__(descricao)

class AtividadeGenerica(Atividade):
    def __init__(self, descricao):
        super().__init__(descricao)



        

    