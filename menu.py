from biblioteca import Biblioteca, Livro, Usuario # Importar as classes: Biblioteca, Livro e Usuario do módulo biblioteca


def menu(): # Função principal do menu de interação com o usuário
    
    biblioteca = Biblioteca() # Cria uma nova instância da biblioteca

    # Laço principal do menu (loop infinito até que o usuário escolha sair)
    while True:
        # Exibe o menu principal
        print("\n===== MENU BIBLIOTECA =====")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Usuário")
        print("3. Realizar Empréstimo")
        print("4. Realizar Devolução")
        print("5. Consultar Livros")
        print("6. Relatórios")
        print("0. Sair")

        # Realiza a leitura da opção digitada pelo usuário
        opcao = input("Escolha uma opção: ")

        # Opção 1 - Cadastro de livro
        if opcao == "1":
            # Solicita os dados do livro
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano = input("Ano de publicação: ")
            copias = int(input("Número de cópias: "))

            # Cria um objeto Livro e adiciona à biblioteca
            livro = Livro(titulo, autor, ano, copias)
            biblioteca.adicionar_livro(livro)

            print("Livro cadastrado com sucesso.")

        # Opção 2 - Cadastro de usuário
        elif opcao == "2":
            # Solicita os dados do usuário
            nome = input("Nome do usuário: ")
            id_usuario = input("ID do usuário: ")
            contato = input("Contato: ")

            # Cria um objeto Usuario e adiciona à biblioteca
            usuario = Usuario(nome, id_usuario, contato)
            biblioteca.adicionar_usuario(usuario)

            print("Usuário cadastrado com sucesso.")

        # Opção 3 - Empréstimo de livro
        elif opcao == "3":
            # Solicita o título do livro e o ID do usuário
            titulo = input("Título do livro para empréstimo: ")
            id_usuario = input("ID do usuário: ")

            # Tenta realizar o empréstimo e exibe o resultado
            print(biblioteca.emprestar_livro(titulo, id_usuario))

        # Opção 4 - Devolução de livro
        elif opcao == "4":
            # Solicita o título do livro e o ID do usuário
            titulo = input("Título do livro para devolução: ")
            id_usuario = input("ID do usuário: ")
