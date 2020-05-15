from core.atividade import AtividadeGenerica, AtividadeGenerica,EventoFinal
from core.acao import AcaoTransicao
from core.processo import Processo
from core.controle import ControleSimNao, ControleTexto

def cria_processo(processo):
        ativ1 = AtividadeGenerica( "Abrir uma coisa")
        ativ2 = AtividadeGenerica( "Fechar uma coisa")
        ativ3 = EventoFinal("Fim")

        acao = AcaoTransicao( "Fechar", ativ2)
        ativ1.adiciona_acao( acao )

        acao = AcaoTransicao( "Abrir", ativ1)
        ativ2.adiciona_acao(acao)
        acao = AcaoTransicao("Concluir", ativ3)
        ativ2.adiciona_acao(acao)

        processo.adiciona_atividade( ativ1 )
        processo.adiciona_atividade( ativ2)
        processo.adiciona_atividade( ativ3)

        processo.controles.append(ControleTexto("Coisa que abre e fecha", "Qual o nome da coisa que abre e fecha?"))
        processo.controles.append(ControleSimNao("Porta barulhenta", "A porta faz barulho?")