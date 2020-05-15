class RenderFactory:
    @staticmethod
    def funcname(render):
        if (render == 'linha_de_comando')
            return RenderLinhaDeComando()

class Render:
    pass

class RenderLinhaDeComando(Render):

    def exec(self, controles):
        for controle in controles:
            if (controle is ControleTexto):
                self.controle_texto(controle)
            elsif (controle is ControleSimNao):
                self.controle_sim_nao()
    
    def controle_texto(self, controle):
        controle.conteudo = input(controle.pergunta)

        return controle
    
    def controle_sim_nao(self, controle):
        resposta = input( controle.pergunta + '(S)im ou (N)ão')

        if (resposta.upper() == 'S'):
            controle.conteudo = 1
        else:
            controle.conteudo = 0 


