lista_convidados = []
lista_comidas =[]
valor_comida = []

num_convidados = int(input())
passou = 0
for i in range(num_convidados):
    nome = input()
    if nome == "Maicon Kuster":
        comida_inutil = input()
        valor_inutil = int(input())
        print("você é convidado DE GUÊÊ???, sai da minha festa seu FOFOQUEIRO!!")
    else:
        lista_convidados.append(nome)

        comida = input()
        valor_comida.append(int(input()))
        # Conferindo se a comida é repetida
        if len(lista_comidas) >= 1:
            chave = True
            j = 0
            repetida = False
            for palavra in lista_comidas:
                if chave == True:
                    if palavra == comida:
                        repetida = True
                j+=1
                if j == len(lista_comidas):
                    chave = False
            
            if repetida == True:
                print(f"Na Festa do Calabreso não pode comida Repetida SAI FORA {lista_convidados[-1]}")
                lista_convidados.pop()
                valor_comida.pop()
            else:
                lista_comidas.append(comida)
                passou+=1
        else:
            lista_comidas.append(comida)
            passou+=1

if passou == 0 or len(lista_convidados) == 0:
    print("Nenhum convidado marcou presença na festa do calabreso!")
else:

    # Ordenando a lista em ordem crescente (Bubble Sort)
    n = len(valor_comida)
    for s in range(n-1):
        if valor_comida[s] > valor_comida[s+1]:
            valor_comida[s], valor_comida[s+1] = valor_comida[s+1], valor_comida[s]
            lista_convidados[s], lista_convidados[s+1] = lista_convidados[s+1], lista_convidados[s]
            lista_comidas[s], lista_comidas[s+1] = lista_comidas[s+1], lista_comidas[s]
        elif valor_comida[s] == valor_comida[s+1]:
            nomes_iguais = lista_convidados[s:s+2]
            nomes_iguais.sort()
            for k in range(len(nomes_iguais)-1):
                lista_convidados[s], lista_convidados[s+1] = nomes_iguais[k], nomes_iguais[k+1]
                lista_comidas[s], lista_comidas[s+1] = lista_comidas[s+1], lista_comidas[s]

    # Comida mais cara
    valor_comida_cara = valor_comida[-1]
    pessoa_comida_cara = lista_convidados[-1]
    comida_cara = lista_comidas[-1]
    print(f"Obrigado para o(a) {pessoa_comida_cara} pelo(a) excelente {comida_cara}")

    if len(lista_convidados) > 1:
        # Comida mais barata
        valor_comida_barata =valor_comida[0]
        pessoa_comida_barata = lista_convidados[0]
        comida_barata = lista_comidas[0]
        print(f"Rapaz, {pessoa_comida_barata} trouxe o(a) {comida_barata} que estava altamente mais ou menos!!!")

if passou != 0:
    print("Lista de convidados do Calabreso")
    z=0
    for nome in lista_convidados:
        print(f"{z+1}- {nome}")
        z+=1