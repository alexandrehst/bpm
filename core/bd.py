from core.instancia import Instancia
from core.usuario import Usuario

class BancoDeDados():
    def __init__(self):
        self.usuarios = []
        self.instancias = []
        self.usuario_ultimo_id = 0
        self.instancia_ultimo_id = 0

    def get_ultimo_id(self, classe):
        if (classe == 'usuario'):
            self.usuario_ultimo_id += 1
            return self.usuario_ultimo_id
        
        if (classe == 'instancia'):
            self.instancia_ultimo_id += 1
            return self.instancia_ultimo_id

        return 0

    def adiciona_usuario(self, nome):

        self.usuarios.append( Usuario( self.get_ultimo_id('usuario'),nome))
    
    def obtem_usuarios(self):
        return self.usuarios

    def obtem_usuario(self, id):
        for usu in self.usuarios:
            if (id == usu.id):
                return usu
        
        return None
    
    def cria_instancia(self, processo):
        self.instancias.append(  Instancia(self.get_ultimo_id('instancia'),processo) )

    def get_instancias(self, apenas_nao_atribuidos=False):
        resp = []
        for inst in self.instancias:
            if ( apenas_nao_atribuidos ):
                if (inst.usuario is None ):
                    resp.append( inst)
            else:
                resp.append(inst)
        
        return resp

    def get_instancias_usuario(self, usuario):
        resp = []
        for inst in self.instancias:
            if (inst.usuario.id == usuario.id ):
                resp.append( inst)

        return resp


    
    def get_instancia(self, id):
        for inst in self.instancias:
            if (id == inst.id):
                return inst


