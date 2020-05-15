class Processo:
    def __init__(self, descricao):
        self.descricao = descricao
        self.atividades=[]
        self.campos = []
        self.controles=[]
    
    def adiciona_atividade(self, atividade):
        self.atividades.append(atividade)

    def inicia(self):s
        return self.atividades[0]

    def __str__(self):
        retorno = 'PROCESSO: ' + self.descricao + '\n'
        for atv in self.atividades:
            retorno += str(atv) + '\n'
        return retorno


