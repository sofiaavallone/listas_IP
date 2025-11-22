nome1 = input("Digite o nome 1: ")
nome2 = input("Digite o nome 2: ")
nome3 = input("Digite o nome 3: ")

cont_achados1 = 0
cont_achados2 = 0
cont_achados3 = 0

print("Vai começar o esconde-esconde UFPE 2025!")
for i in range(3):
    print()
    # Inicialização para cada buscador
    if i == 0:
        print(f"Prontos ou não, lá vai {nome1}.")
        print(f"Agora {nome1} procurará no CFCH.")
    elif i == 1:
        print(f"Prontos ou não, lá vai {nome2}.")
        print(f"Agora {nome2} procurará no CFCH.")
    elif i == 2:
        print(f"Prontos ou não, lá vai {nome3}.")
        print(f"Agora {nome3} procurará no CFCH.")

    # Contagem de pontos
    resposta = "Achou uma pessoa!"
    while resposta != "Fim da busca nesse prédio.": #CFCH
        if i == 0:
            resposta = input("Digite se achou alguém: ")
            if resposta == "Achou uma pessoa!":
                print(f"{nome1} achou uma pessoa!")
                cont_achados1+=1
        elif i == 1:
            resposta = input("Digite se achou alguém: ")
            if resposta == "Achou uma pessoa!":
                print(f"{nome2} achou uma pessoa!")
                cont_achados2+=1
        else:
            resposta = input("Digite se achou alguém: ")
            if resposta == "Achou uma pessoa!":
                print(f"{nome3} achou uma pessoa!")
                cont_achados3+=1
    
    # Início CTG
    if i == 0:
        print(f"Agora {nome1} procurará no CTG.")
    elif i == 1:
        print(f"Agora {nome2} procurará no CTG.")
    elif i == 2:
        print(f"Agora {nome3} procurará no CTG.")

    resposta = "Achou uma pessoa!"
    while resposta != "Fim da busca nesse prédio.": #CTG
        if i == 0:
            resposta = input("Digite se achou alguém: ")
            if resposta == "Achou uma pessoa!":
                print(f"{nome1} achou uma pessoa!")
                cont_achados1+=1
        elif i == 1:
            resposta = input("Digite se achou alguém: ")
            if resposta == "Achou uma pessoa!":
                print(f"{nome2} achou uma pessoa!")
                cont_achados2+=1
        else:
            resposta = input("Digite se achou alguém: ")
            if resposta == "Achou uma pessoa!":
                print(f"{nome3} achou uma pessoa!")
                cont_achados3+=1
    
    # Início CIN
    if i == 0:
        print(f"Agora {nome1} procurará no CIN.")
    elif i == 1:
        print(f"Agora {nome2} procurará no CIN.")
    elif i == 2:
        print(f"Agora {nome3} procurará no CIN.")

    resposta = "Achou uma pessoa!"
    while resposta != "Fim da busca nesse prédio.": #CIN
        if i == 0:
            resposta = input("Digite se achou alguém: ")
            if resposta == "Achou uma pessoa!":
                print(f"{nome1} achou uma pessoa!")
                cont_achados1+=1
        elif i == 1:
            resposta = input("Digite se achou alguém: ")
            if resposta == "Achou uma pessoa!":
                print(f"{nome2} achou uma pessoa!")
                cont_achados2+=1
        else:
            resposta = input("Digite se achou alguém: ")
            if resposta == "Achou uma pessoa!":
                print(f"{nome3} achou uma pessoa!")
                cont_achados3+=1

print()
if cont_achados1 == 0 and cont_achados2 == 0 and cont_achados3 == 0:
    print("Ninguém foi encontrado, nenhum dos buscadores ganhou a disputa.")
else:
    vencedor = max(cont_achados1, cont_achados2, cont_achados3)
    if vencedor == cont_achados1:
        print(f"{nome1} é o(a) melhor no esconde-esconde da UFPE!")
    elif vencedor == cont_achados2:
        print(f"{nome2} é o(a) melhor no esconde-esconde da UFPE!")
    else:
        print(f"{nome3} é o(a) melhor no esconde-esconde da UFPE!")