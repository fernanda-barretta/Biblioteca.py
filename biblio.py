class Livro:
    tit="" # Atributo para guardar o título da obra
    aut="" # Atributo para guardar o nome do autor
    ano="" # Atributo para guardar o ano de lançamento
    id=""  # Atributo para guardar o código identificador único
    st=""  # Atributo para guardar o status (disponível ou emprestado)

# Função para cadastrar uma nova obra no sistema
def novoitem(acervo):
    ident=input("Identificador do livro: ")
 
    duplicado = False  # Variável de controle para verificar se o ID já existe
    for item in acervo: #Percorre cada livro já cadastrado na lista 
        if item.id == ident:
            duplicado=True
 
    if duplicado:
        print("Aviso: Este identificador já existe.")

    # Caso o ID seja inédito
    else:
        obj=Livro()  #Cria um novo objeto vazio da classe Livro
        obj.id=ident # Define o ID do novo livro
        obj.tit=input("Título da obra: ")
        obj.aut=input("Nome do autor: ")
        obj.ano=input("Ano de lançamento: ")
        obj.st="disponível"
        acervo.append(obj) # Adiciona o livro completo à lista do acervo
        print("Obra registrada com sucesso!")

# Função para buscar livros por identificador ou por autor
def buscar(acervo):
    print("1 - Localizar por ID")
    print("2 - Localizar por Autor")
    sel = input("Opção: ")
 
    achou=False # Variável para controlar se algum resultado foi exibido
    if sel == "1":
        ident=input("ID: ")
        for item in acervo:
            if item.id == ident:
                print("Obra:", item.tit, "| Autor:", item.aut, "| Status:", item.st)
                achou = True # Marca que encontrou o resultado
    else:
        if sel == "2":
            autor=input("Autor: ")
            for item in acervo:
                if item.aut == autor:
                    print("Obra:", item.tit, "| ID:", item.id, "| Status:", item.st)
                    achou = True # Marca que encontrou pelo menos um resultado
 
    if achou == False:
        print("Nenhum registro encontrado")
 
 # Função para atualizar os dados de uma obra que já existe
def editar(acervo):
    ident=input("ID da obra para atualizar: ")
    achou=False
    for item in acervo:
        if item.id == ident:
            item.tit = input("Novo título: ")
            item.aut = input("Novo autor: ")
            item.ano = input("Novo ano: ")
            print("Informações atualizadas!")
            achou=True
 
    if achou==False:
        print("Obra não localizada")

 # Função para excluir permanentemente uma obra do sistema 
def excluir(acervo):
    ident=input("ID para remoção: ")
    pos =-1 # Variável para guardar o índice da posição na lista
    for i in range(len(acervo)): # Percorre a lista usando os índices numéricos
        if acervo[i].id == ident:
            pos = i # Salva o número da posição na variável pos
    if pos != -1: # Se a posição foi alterada (ou seja, o livro foi achado)
        acervo.pop(pos) # Remove o item da lista usando a posição encontrada
        print("Registro removido do acervo.") 
    else: 
        print("Obra não localizada")
 
# Função para listar as obras em ordem alfabética pelo título
def exibir(acervo):
    temp = [] # Cria uma lista temporária para não alterar a ordem original
    for item in acervo: # Copia cada livro para a lista temporária
        temp.append(item)
 
    tam = len(temp) # Obtém o total de livros
    i = 0
    while i < tam - 1: # Laço externo do Bubble Sort
        j = 0
        while j < tam - 1 - i: # Laço interno compara pares adjacentes
            if temp[j].tit > temp[j+1].tit: # Compara títulos em ordem alfabética
                aux = temp[j] # Guarda o item atual na variável auxiliar
                temp[j] = temp[j+1] # Coloca o próximo no lugar do atual
                temp[j+1] = aux # Coloca o auxiliar na posição seguinte
            j = j + 1
        i = i + 1
 
    print("===== LISTAGEM DE OBRAS (ordem alfabética) =====")
    for item in temp:
        print("Título:", item.tit, "- Lançamento:", item.ano)

# Função para registrar que um livro foi emprestado 
def saida(acervo):
    ident=input("ID para empréstimo: ")
    achou=False
    for item in acervo:
        if item.id == ident:
            achou=True
            if item.st == "disponível":
                item.st = "emprestado"
                print("Saída registrada!")
            else:
                print("Atenção: Obra já se encontra emprestada")
 
    if achou==False:
        print("Obra não localizada")

# Função para registrar que um livro foi devolvido à biblioteca 
def retorno(acervo):
    ident=input("ID para devolução: ")
    achou=False
    for item in acervo:
        if item.id == ident:
            achou = True
            item.st = "disponível"
            print("Retorno confirmado!")
 
    if achou == False:
        print("Obra não localizada")

# Função principal que organiza a execução do programa e o menu
def principal():
    dados=[]
    ativo=True
 
    while ativo:
        print("\n============================")
        print("   GERENCIADOR DE ACERVO")
        print("============================")
        print("1. Registrar Obra")
        print("2. Pesquisar Obra")
        print("3. Editar Informações")
        print("4. Remover Registro")
        print("5. Listar Tudo (ordem alfabética)")
        print("6. Registrar Empréstimo")
        print("7. Registrar Devolução")
        print("8. Encerrar")
 
        escolha=input("Selecione: ")
 
        if escolha == "1":
            novoitem(dados)
        else:
            if escolha == "2":
                buscar(dados)
            else:
                if escolha == "3":
                    editar(dados)
                else:
                    if escolha == "4":
                        excluir(dados)
                    else:
                        if escolha == "5":
                            exibir(dados)
                        else:
                            if escolha == "6":
                                saida(dados)
                            else:
                                if escolha == "7":
                                    retorno(dados)
                                else:
                                    if escolha == "8":
                                        print("Finalizando sistema...")
                                        ativo=False # Muda para falso para sair do loop while
                                    else: # Se digitou qualquer outra coisa inválida
                                        print("Opção inexistente!")

 #Esse trecho garante que a função principal só é chamada quando o arquivo é executado diretamente. Se o arquivo fosse importado por outro código, essa parte não rodaria automaticamente.
if __name__ == "__main__":
    principal()
