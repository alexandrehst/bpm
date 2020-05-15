# TODO Banco de dados: gravar todas as entidades
# TODO Publicar os serviços
# TODO Log. Logar alterações
# TODO BigData das operações
# TODO Atividades de IF
# TODO Front end
# TODO Resultados dos campos tem que gravar na Instância

# processo inicia, abre, fecha, termina


from core.usuario import Usuario
from core.processo import Processo
from core.bd import BancoDeDados

import processo_teste

#Cria um novo Processo Teste
processo = Processo("Processo Teste")
processo_teste.cria_processo(processo)
usuario = ''

bd = BancoDeDados()

def obtem_instancias():
    for instancia in bd.get_instancias(True):
        print( instancia)

def logar():
    print('Login --------')
    for usu in bd.obtem_usuarios():
        print( usu.id, usu.nome)

    id = int(input('Digite o id do usuário: '))
    usuario = bd.obtem_usuario(id)

    print( "Usuário logado: ")
    print( usuario )
    print( "PROCESSO ATIVO")
    print(processo)

def cria_instancia():    
    # Cria instancia no passo inicial
    bd.cria_instancia(processo)
    
def ver_instancias():
    print( '--------- Instâncias do usuário ---------')
    print( 'Usuário: ' + usuario.nome)

    instancias = bd.get_instancias()

    if ( len( instancias) == 0):
        print("Não existem instâncias")
    else:
        for inst in instancias:
            print(inst)

def pegar():
        print( '--------- Instâncias ---------')
        for inst in bd.get_instancias(true):
            print(inst)
        id = int(input('Digite o id da instância desejada: '))
        instancia = bd.get_instancia(id)

        instancia.atribui(usuario)

        print('---- Suas instâncias -----')
        for inst in bd.get_instancias_usuario(usuario):
            print(inst)

def interagir():
        print('---- Suas instâncias -----')
        for inst in bd.get_instancias_usuario(usuario):
            print(inst)
        id = int(input('Digite o id da instância desejada: '))
        instancia = bd.get_instancia(id)

        instancia.atribui(usuario)



def main():
    while True:
        print('---------- BPM: Command ----------')
        print('1. Logar')
        print('2. Criar nova instância do Processo Teste')
        print('3. Ver instâncias atribuídas')
        print('4. Ver todas as instâncias')
        print('5. Pegar uma instância')
        print('6. Interagir com uma instância')
        print('9. Sair')
        opcao = int(input('Sua opção? '))
        

        if (opcao == 9):
            exit(0)

        if (opcao == 1):
            logar()
        elif (opcao == 2):
            cria_instancia()
        elif (opcao == 3):
            ver_instancias()
        elif (opcao == 4 ):
            obtem_instancias()
        elif (opcao == 5)
            pegar()
        elif (opcao ==6)
            interagir()
        else:
            print( 'Opção inválida.')    


if __name__ == '__main__':
    # execute only if run as the entry point into the program

    bd.adiciona_usuario( 'João' )
    bd.adiciona_usuario( 'Maria' )
    bd.adiciona_usuario( 'José' )
    
    main()

