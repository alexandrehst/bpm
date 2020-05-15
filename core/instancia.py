import copy
from core.render import Re

class Instancia:

    def __init__(self, id, processo):
        self.id = id
        self.processo = processo
        self.atividade_atual = processo.inicia()
        self.usuario = None
        self.controles = copy.deepcopy(processo.controles)

    def atribui(self, usuario):
        self.usuario = usuario

    def executa(self, render):
        render.executa(self.controles)
        
    def __str__(self):
        return f"ID: {self.id}  PROCESSO: {self.processo.descricao} ATIVIDADE: {self.atividade_atual.descricao}"

