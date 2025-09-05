from config import db

class Usuarios(db.Model):
    __tablename__ = 'cadastroUsuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "cpf": self.cpf,
            "telefone": self.telefone
        }

class UsuarioNaoEncontrado(Exception):
    pass

def criar_cadastro(dados):
    novo_usuario = Usuarios (
        nome= dados['nome'],
        email= dados['email'],
        senha= dados['senha'],
        cpf= dados['cpf'],
        telefone= dados['telefone']
    )
    db.session.add(novo_usuario)
    db.session.commit()
    return{"mensagem": "Cadastro feito com sucesso!", "usuario": novo_usuario.to_dict()}, 201


def exibir_usuarios():
    usuarios = Usuarios.query.all()
    return [usuario.to_dict() for usuario in usuarios]


def exibir_idusuario(id_usuario):
    usuario = Usuarios.query.get(id_usuario)
    if not usuario:
            raise UsuarioNaoEncontrado("Usuario não Encontrado!")
    return usuario.to_dict()


def atualizar_usuario(id_usuario, dadoNovo):
    usuario = Usuarios.query.get(id_usuario)
    if not usuario:
        raise UsuarioNaoEncontrado("Usuario não Encontrado!")

    usuario.nome = dadoNovo.get("nome", usuario.nome)
    usuario.email = dadoNovo.get("email", usuario.email)
    usuario.senha = dadoNovo.get("senha", usuario.senha)
    usuario.cpf = dadoNovo.get("cpf", usuario.cpf)
    usuario.telefone = dadoNovo.get("telefone", usuario.telefone)

    db.session.commit()
    return usuario.to_dict(), 200



def deletar_usuario(id_usuario):
    usuario = Usuarios.query.get(id_usuario)
    if not usuario:
        raise UsuarioNaoEncontrado('Usuario não Encontrado!')
    
    db.session.delete(usuario)
    db.session.commit()
    return {"mensagem": "Usuario deletado com sucesso!"}, 200
