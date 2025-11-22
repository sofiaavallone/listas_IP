print("RECEBA! É hoje que eu me torno o melhor dos melhores.")
goleiros_especiais = ["Rokenedy", "IShowSpeed", "Sérgio Soares", "Neymar Jr", "Gabriel Vasconcelos"]
treino_goleiro = []

quant_treinos = int(input())
habilidade_inicial = int(input())
if habilidade_inicial >= 0 and habilidade_inicial <= 5:
    print("A gente tem que começar de algum lugar, né? RECEBA!")
elif habilidade_inicial >= 6 and habilidade_inicial <= 15:
    print("Não tem jeito, vou ser o melhor do mundo!")
else:
    print("O Pai tá estourado! RECEBA!")

treinos_goleiros = input().split("-")
meta = (100 - habilidade_inicial) / quant_treinos
print(f"Meta por Partida: {meta}")

habilidade_final = habilidade_inicial

# Adicionando os treinos na matriz
for i in range(0, len(treinos_goleiros), 2):
    linha_matriz = []
    linha_matriz.append(treinos_goleiros[i])
    treino_goleiro.append(linha_matriz)

# Adicionando os goleiros na matriz
j = 0
for i in range(1, len(treinos_goleiros), 2):
    treino_goleiro[j].append(treinos_goleiros[i])
    j+=1

chave = True
while habilidade_final < 100 and chave == True:
    # Partidas
    i = 0
    while i < len(treino_goleiro)  and chave == True:
        ponto = 0
        tipo_treino = treino_goleiro[i][0]
        nome_goleiro = treino_goleiro[i][1]

        print(f"TIPO DE PARTIDA: {tipo_treino}")
        print(f"Nome do Goleiro: {nome_goleiro}")
        # Falta
        if tipo_treino == "Batida de Falta":
            if nome_goleiro not in goleiros_especiais:
                habilidade_goleiro = int(input())
            matriz = eval(input())
            # Coordenadas
            x_linha = int(input())
            y_coluna = int(input())

            if matriz[x_linha][y_coluna] == 1:
                if nome_goleiro == "IShowSpeed":
                    ponto = meta*1.5
                    print("REBECA? Is that you?")
                    print("Ispidi mai friand, recieve!")
                elif nome_goleiro == "Sérgio Soares":
                    print("DALE DALE, PROFESSOR! Quero ver se esse tal de Python é bom mesmo…")
                elif nome_goleiro == "Neymar Jr":
                    ponto = meta/2
                    print("Ele nem sabe agarrar! A arma dele é a sua fragilidade…")
                elif nome_goleiro == "Gabriel Vasconcelos":
                    ponto = meta*2
                    print("HAHAHA! Eu pedi um desafio, não uma barra sem goleiro…")
                elif nome_goleiro not in goleiros_especiais:
                    if habilidade_final > habilidade_goleiro:
                        ponto = habilidade_final-habilidade_goleiro
                else: # Rokenedy
                    print("Aí não dá, impossível de fazer gol no maior do mundo.")
                

                if nome_goleiro != "Rokenedy" and nome_goleiro != "Sérgio Soares":       
                    print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")
                else:
                    print("A jornada ainda não acabou!")
            else:
                print("A jornada ainda não acabou!")
        
        # Pênalti
        elif tipo_treino == "Batida de Pênalti":
            if nome_goleiro not in goleiros_especiais:
                habilidade_goleiro = int(input())
            matriz = eval(input())
            # Coordenadas
            x_linha = int(input())
            y_coluna = int(input())

            if matriz[x_linha][y_coluna] == 1:
                if nome_goleiro == "IShowSpeed":
                    ponto = meta*1.5
                    print("REBECA? Is that you?")
                    print("Ispidi mai friand, recieve!")
                elif nome_goleiro == "Sérgio Soares":
                    ponto = meta
                    print("DALE DALE, PROFESSOR! Quero ver se esse tal de Python é bom mesmo…")
                elif nome_goleiro == "Neymar Jr":
                    ponto = meta/2
                    print("Ele nem sabe agarrar! A arma dele é a sua fragilidade…")
                elif nome_goleiro == "Gabriel Vasconcelos":
                    ponto = meta*2
                    print("HAHAHA! Eu pedi um desafio, não uma barra sem goleiro…")
                elif nome_goleiro not in goleiros_especiais:
                    if habilidade_final > habilidade_goleiro:
                        ponto = habilidade_final-habilidade_goleiro
                else: # Rokenedy
                    print("Aí não dá, impossível de fazer gol no maior do mundo.")
                
                if nome_goleiro != "Rokenedy":       
                    print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")
                else:
                    print("A jornada ainda não acabou!")
            else:
                print("A jornada ainda não acabou!")
        # Ataque
        elif tipo_treino == "Batida de Ataque":
            if nome_goleiro not in goleiros_especiais:
                habilidade_goleiro = int(input())
            matriz = eval(input())
            # Coordenadas
            x_linha = int(input())
            y_coluna = int(input())

            if matriz[x_linha][y_coluna] == 1:
                if nome_goleiro == "IShowSpeed":
                    ponto = meta*1.5
                    print("REBECA? Is that you?")
                    print("Ispidi mai friand, recieve!")
                elif nome_goleiro == "Sérgio Soares":
                    print("DALE DALE, PROFESSOR! Quero ver se esse tal de Python é bom mesmo…")
                elif nome_goleiro == "Neymar Jr":
                    ponto = meta/2
                    print("Ele nem sabe agarrar! A arma dele é a sua fragilidade…")
                elif nome_goleiro == "Gabriel Vasconcelos":
                    ponto = meta*2
                    print("HAHAHA! Eu pedi um desafio, não uma barra sem goleiro…")
                elif nome_goleiro not in goleiros_especiais:
                    if habilidade_final > habilidade_goleiro:
                        ponto = habilidade_final-habilidade_goleiro
                else: # Rokenedy
                    print("Aí não dá, impossível de fazer gol no maior do mundo.")
                
                if nome_goleiro != "Rokenedy" and nome_goleiro != "Sérgio Soares":       
                    print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")
                else:
                    print("A jornada ainda não acabou!")
            else:
                print("A jornada ainda não acabou!")
 
        habilidade_final+=ponto 

        if habilidade_final <= 100:
            if ponto >= meta:
                print(f"VAMO! PARTIDA {i+1} DE {len(treino_goleiro)}!")
            else:
                print("Dá pra recuperar depois! Vamo seguindo!")
        else:
            chave = False

        i+=1
    chave = False
    

# Resultado final
if habilidade_final > 100:
    print("NÃO TEM JEITO! EU SEMPRE SOUBE QUE IA SER O MELHOR DO MUNDO! RECEBA!")
elif habilidade_final == 100:
    print("O trono do futebol hoje tem dois reis. Eu e Pelé! Não podia estar com alguém melhor!")
else:
    print("Ano que vem tem InterCIn de novo! É só eu treinar mais…")