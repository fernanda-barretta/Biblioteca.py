class Livro:
    tit=""
    aut=""
    ano=""
    id=""
    st=""
 
def novoitem(acervo):
    ident=input("Identificador do livro: ")
 
    duplicado = False
    for item in acervo:
        if item.id == ident:
            duplicado=True
 
    if duplicado:
        print("Aviso: Este identificador já existe.")
    else:
        obj=Livro()
        obj.id=ident
        obj.tit=input("Título da obra: ")
        obj.aut=input("Nome do autor: ")
        obj.ano=input("Ano de lançamento: ")
        obj.st="disponível"
        acervo.append(obj)
        print("Obra registrada com sucesso!")
 
def buscar(acervo):
    print("1 - Localizar por ID")
    print("2 - Localizar por Autor")
    sel = input("Opção: ")
 
    achou=False
    if sel == "1":
        ident=input("ID: ")
        for item in acervo:
            if item.id == ident:
                print("Obra:", item.tit, "| Autor:", item.aut, "| Status:", item.st)
                achou = True
    else:
        if sel == "2":
            autor=input("Autor: ")
            for item in acervo:
                if item.aut == autor:
                    print("Obra:", item.tit, "| ID:", item.id, "| Status:", item.st)
                    achou = True
 
    if achou == False:
        print("Nenhum registro encontrado")
 
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
 
def excluir(acervo):
    ident=input("ID para remoção: ")
    pos =-1
    for i in range(len(acervo)):
        if acervo[i].id == ident:
            pos = i
 
    if pos != -1:
        acervo.pop(pos)
        print("Registro removido do acervo.")
    else:
        print("Obra não localizada")
 
def exibir(acervo):
    temp = []
    for item in acervo:
        temp.append(item)
 
    tam = len(temp)
    i = 0
    while i < tam - 1:
        j = 0
        while j < tam - 1 - i:
            if temp[j].tit > temp[j+1].tit:
                aux = temp[j]
                temp[j] = temp[j+1]
                temp[j+1] = aux
            j = j + 1
        i = i + 1
 
    print("===== LISTAGEM DE OBRAS (ordem alfabética) =====")
    for item in temp:
        print("Título:", item.tit, "- Lançamento:", item.ano)
 
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
                                        ativo=False
                                    else:
                                        print("Opção inexistente!")
 
if __name__ == "__main__":
    principal()