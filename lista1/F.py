# Recebendo as informações
nome_item = input("O que foi comprado? ").lower()
valor_item = float(input("Custo do item: "))
responsavel = input("Quem fez a compra? ").capitalize()
tipo_evento = input("Qual o tipo de evento? ").lower()

# Regras de Ouro da Angela
if valor_item > 100.00 and responsavel != "Angela":
    status = "Reprovada"
    print("Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!")
elif valor_item > 100.00 and responsavel == "Angela":
    status = "Aprovada"
    print("Apenas eu tenho discernimento para gastos desta magnitude.")
else:
    status = "Aprovada"
    print("Compra feita por mim, obviamente dentro dos padrões de excelência.")

# Regras para Michael Scott
if responsavel == "Michael":
    if nome_item == "mágica" or nome_item == "fantasia":
        status = "Reprovada"
        print("O Comitê não financia frivolidades e palhaçadas, Michael.")
    if valor_item > 60.00:
        status = "Aprovada com ressalvas"
        if tipo_evento == "natal":
            print("O espírito natalino de Michael é... excessivo. A nota será conferida.")
        elif tipo_evento == "aniversário":
            print("Michael nunca gasta tanto nos aniversários dos funcionários, deve ser o dele!")
    else:
        status = "Aprovada"
        print("Uma compra surpreendentemente sensata vinda do Michael. Suspeito.")

# Regras Halloween
if tipo_evento == "halloween":
    if nome_item == "abóbora" and valor_item <= 30.00:
        status = "Aprovada"
        print("Uma abóbora de tamanho e custo razoáveis. Eficiente.")
    elif nome_item == "abóbora" and valor_item > 30.00:
        status = "Aprovada com ressalvas"
        print("Por que uma abóbora precisa ser tão cara? Extravagância.")
    else:
        if valor_item < 100 or responsavel != "Angela":
            status = "Aprovada com ressalvas"
            print("Decoração de Halloween... Tenho certeza que Phyllis exagerou de novo.")

# Regras Aniversário
if tipo_evento == "aniversário":
    if nome_item == "bolo" and valor_item <= 30.00:
        status = "Aprovada"
        print("Um bolo modesto para celebrar mais um ano de produtividade, parabéns!")
    elif nome_item == "sorvete de menta com chocolate":
        status = "Reprovada"
        print("Este sabor de sorvete é uma abominação e não entrará em meu evento.")
    else:
        status = "Aprovada"
        print("Itens de aniversário devem ser práticos, não uma distração do trabalho.")

# Regras gerais
if valor_item > 50.00:
    status = "Aprovada com ressalvas"
    print("Está dentro do orçamento, mas não quer dizer que não vou verificar!")
else:
    status = "Aprovada"
    print("Esta compra não viola nenhum regulamento... por enquanto.")

# Saída do status da compra após os comentários
print(f"Compra {status}!")
