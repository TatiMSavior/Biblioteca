# biblioteca.py

# Classe que representa um livro na biblioteca
class Livro:
    def __init__(self, titulo, autor, ano, copias):
        # Atributos principais do livro
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.copias = copias  # Número de cópias disponíveis
        self.emprestados = 0  # Número de cópias atualmente emprestadas

    # Método para realizar o empréstimo do livro
    def emprestar(self):
        if self.copias > 0:
            self.copias -= 1         # Diminui o número de cópias disponíveis
            self.emprestados += 1    # Aumenta o número de cópias emprestadas
            return True              # Empréstimo bem-sucedido
        return False                 # Empréstimo não realizado (sem cópias)

    # Método para devolver um livro emprestado
    def devolver(self):
        if self.emprestados > 0:
            self.copias += 1         # Aumenta o número de cópias disponíveis
            self.emprestados -= 1    # Diminui o número de cópias emprestadas
            return True              # Devolução bem-sucedida
        return False                 # Não há cópias emprestadas para devolver

    # Representação textual do objeto Livro
    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano}) | Disponíveis: {self.copias} | Emprestados: {self.emprestados}"


# Classe que representa um usuário da biblioteca
class Usuario:
    def __init__(self, nome, id_usuario, contato):
        # Atributos principais do usuário
        self.nome = nome
        self.id_usuario = id_usuario
        self.contato = contato
        self.livros_emprestados = []  # Lista de livros que o usuário possui em empréstimo

    # Representação textual do objeto Usuario
    def __str__(self):
        return f"{self.nome} (ID: {self.id_usuario}) - Contato: {self.contato}"


# Classe principal da biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = []   # Lista de livros cadastrados na biblioteca
        self.usuarios = [] # Lista de usuários cadastrados

    # Adiciona um novo livro à biblioteca
    def adicionar_livro(self, livro):
        self.livros.append(livro)

    # Adiciona um novo usuário à biblioteca
    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    # Busca livros por título, autor ou ano
    def buscar_livros(self, termo):
        resultados = [
            livro for livro in self.livros
            if termo.lower() in livro.titulo.lower()
            or termo.lower() in livro.autor.lower()
            or termo == str(livro.ano)
        ]
        return resultados

    # Encontra um usuário pelo seu ID
    def encontrar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    # Realiza o empréstimo de um livro para um usuário
    def emprestar_livro(self, titulo, id_usuario):
        usuario = self.encontrar_usuario(id_usuario)
        if not usuario:
            return "Usuário não encontrado."

        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if livro.emprestar():
                    usuario.livros_emprestados.append(livro)
                    return f"Livro '{livro.titulo}' emprestado com sucesso para {usuario.nome}."
                else:
                    return "Livro indisponível para empréstimo."
        return "Livro não encontrado."

    # Realiza a devolução de um livro por um usuário
    def devolver_livro(self, titulo, id_usuario):
        usuario = self.encontrar_usuario(id_usuario)
        if not usuario:
            return "Usuário não encontrado."

        for livro in usuario.livros_emprestados:
            if livro.titulo.lower() == titulo.lower():
                if livro.devolver():
                    usuario.livros_emprestados.remove(livro)
                    return f"Livro '{livro.titulo}' devolvido com sucesso."
        return "Livro não encontrado na lista de empréstimos do usuário."

    # Lista todos os livros cadastrados
    def listar_livros(self):
        return self.livros

    # Lista todos os usuários cadastrados
    def listar_usuarios(self):
        return self.usuarios

    # Lista apenas os livros que estão com pelo menos uma cópia emprestada
    def listar_livros_emprestados(self):
        return [livro for livro in self.livros if livro.emprestados > 0]
