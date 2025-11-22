print("Sam: Mas que lugar é esse aqui?")
print("Dollman: WASD... Num exclusivo de PS5? Ah, fala sério!")
print()

matriz = []

hp_sam = 100
hp_neil = 100

def distancia (linha_s, coluna_s, linha2, coluna2): # Calculando a distância de Chebyshev
    coordenadas_s = [linha_s, coluna_s]
    coordenadas2 = [linha2, coluna2]

    dist = 0
    for i in range(len(coordenadas_s)):
        diff = abs(coordenadas_s[i] - coordenadas2[i])
        if diff > dist:
            dist = diff

    return dist

def ataque_sam (dist, arma_sam, hp_neil):
    if arma_sam == "Espingarda" and dist <= 2:
        hp_neil-=25
    elif arma_sam == "Rifle" and dist == 3:
        hp_neil-=15
    elif arma_sam == "Rifle":
        hp_neil-=5
    elif arma_sam == "Metralhadora" and dist >= 4:
        hp_neil-=15

    return hp_neil

def teletransporte_neil (linha_s, coluna_s, matriz):
    dist = 0
    maior_dist = 0
    melhor_posicao = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != "I":
                dist = distancia(linha_s, coluna_s, i, j)
            if dist >= maior_dist:
                maior_dist = dist
                melhor_posicao = [i, j]

    return melhor_posicao
    

for i in range(6):
    linha = input().split()
    matriz.append(linha)

# Encontrando as coordenadas de Neil e Sam
i = 0
for linha in matriz:
    j = 0
    for elemento in linha:
        if elemento == "S":
            linha_s = i
            coluna_s = j
        elif elemento == "N":
            linha_n = i
            coluna_n = j
        j+=1
    i+=1

acoes_sam = 0
cont_teletr = 0
dano_neil = 0
hits_fogo = 0
arma_sam = "Rifle" # Inicia com essa
tipo_posicao_s_atual = "P"
chave = False
chave2 = False
rodadas = 0
calculo_do_like = 0
while hp_sam > 0 and hp_neil > 0:
    entrada = input()
    if entrada == "W":
        if linha_s-1 <= 5 and matriz[linha_s-1][coluna_s] != "I": # Se não for I, pode fazer o movimento
            tipo_posicao_s_anterior = tipo_posicao_s_atual
            tipo_posicao_s_atual = matriz[linha_s-1][coluna_s]
            # Trocando Sam de lugar
            if rodadas != 0:
                matriz[linha_s][coluna_s], matriz[linha_s-1][coluna_s] = tipo_posicao_s_anterior, matriz[linha_s][coluna_s]
            else: # Primeira rodada (onde ele tava era P)
                matriz[linha_s-1][coluna_s] = matriz[linha_s][coluna_s]
                matriz[linha_s][coluna_s] = "P"
            linha_s-=1
        acoes_sam+=1
    elif entrada == "A":
        if coluna_s-1 >= 0 and matriz[linha_s][coluna_s-1] != "I":
            tipo_posicao_s_anterior = tipo_posicao_s_atual
            tipo_posicao_s_atual = matriz[linha_s][coluna_s-1]
            if rodadas != 0:
                matriz[linha_s][coluna_s], matriz[linha_s][coluna_s-1] = tipo_posicao_s_anterior, matriz[linha_s][coluna_s]
            else:
                matriz[linha_s][coluna_s-1] = matriz[linha_s][coluna_s]
                matriz[linha_s][coluna_s] = "P"
            coluna_s-=1
        acoes_sam+=1
    elif entrada == "S":
        if linha_s+1 >= 0 and matriz[linha_s+1][coluna_s] != "I":
            tipo_posicao_s_anterior = tipo_posicao_s_atual
            tipo_posicao_s_atual = matriz[linha_s+1][coluna_s]
            if rodadas != 0:
                matriz[linha_s][coluna_s], matriz[linha_s+1][coluna_s] = tipo_posicao_s_anterior, matriz[linha_s][coluna_s]
            else:
                matriz[linha_s+1][coluna_s] = matriz[linha_s][coluna_s]
                matriz[linha_s][coluna_s] = "P"
            linha_s+=1
        acoes_sam+=1
    elif entrada == "D":
        if coluna_s+1 <= 5 and matriz[linha_s][coluna_s+1] != "I":
            tipo_posicao_s_anterior = tipo_posicao_s_atual
            tipo_posicao_s_atual = matriz[linha_s][coluna_s+1]
            if rodadas != 0:
                matriz[linha_s][coluna_s], matriz[linha_s][coluna_s+1] = tipo_posicao_s_anterior, matriz[linha_s][coluna_s]
            else:
                matriz[linha_s][coluna_s+1] = matriz[linha_s][coluna_s]
                matriz[linha_s][coluna_s] = "P"
            coluna_s+=1
        acoes_sam+=1
    # Troca de arma
    elif entrada == "Espingarda":
        arma_sam = "Espingarda"
        print(f"Arma trocada para {arma_sam}.")
        acoes_sam+=1
    elif entrada == "Rifle":
        arma_sam = "Rifle"
        print(f"Arma trocada para {arma_sam}.")
        acoes_sam+=1
    elif entrada == "Metralhadora":
        arma_sam = "Metralhadora"
        print(f"Arma trocada para {arma_sam}.")
        acoes_sam+=1
    else: # Atacar
        dist = distancia(linha_s, coluna_s, linha_n, coluna_n)
        hp_neil = ataque_sam(dist, arma_sam, hp_neil)
        dano_neil+=1
        acoes_sam+=1
        chave = True

    if tipo_posicao_s_atual == "F":
        hp_sam-=5
        hits_fogo+=1

    if acoes_sam % 4 == 0 and acoes_sam != 0 and hp_sam>0 and hp_neil>0: # Ataque de Neil
        hp_sam-=15
        calculo_do_like +=15
        print(">>> Você recebe um disparo de Neil! <<<")


    if dano_neil % 3 == 0 and dano_neil != 0 and chave == True and hp_neil >0 and hp_sam >0: # Teletransporte Neil
        nova_posicao = teletransporte_neil(linha_s, coluna_s, matriz)
        tipo_posicao_n = matriz[nova_posicao[0]][nova_posicao[1]]
        if cont_teletr != 0:
            matriz[linha_n][coluna_n] = tipo_posicao_n
            matriz[nova_posicao[0]][nova_posicao[1]] = "N"
        else:
            matriz[linha_n][coluna_n] = "P"
            matriz[nova_posicao[0]][nova_posicao[1]] = "N"
        linha_n = nova_posicao[0]
        coluna_n = nova_posicao[1]
        cont_teletr+=1

        for linha in matriz:
            print(" ".join(linha))
        
        chave = False

    if hp_sam <= 40 and chave2 == False:
        print("Dollman: A Fragile comeu todos os criptobiontes da DHV Magalhães... Se curar não é uma opção. Tome cuidado, Sam.")
        chave2 = True

    rodadas+=1

# Cálculo de likes
likes = 1000 - (calculo_do_like*8) - (hits_fogo*10)

# Outputs depois da finalização da missão
if hp_neil <= 0:
    print()
    print("MISSÃO COMPLETA! - Investigue a Anomalia")
    print("========================================")
    print(f"Likes recebidos: 👍 {likes}")
else: 
    print()
    print("MISSÃO FALHOU")
    print("==============")
    print("Sam foi derrotado.")
    print("[Sua alma vaga pela Emenda, buscando reencontrar seu corpo perdido...]")