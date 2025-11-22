# Especificações de cada projeto
memoria = [[256, "Redstone"], [64, "Repetidores"], [128, "Tochas de Redstone"]]
calculadora = [[512, "Redstone"], [128, "Repetidores"], [64, "Tochas de Redstone"], [256, "Lâmpadas de Redstone"]]
sequenciador = [[1024, "Redstone"], [256, "Repetidores"], [64, "Blocos de Notas"], [128, "Observadores"]]
processador = [[4096, "Redstone"], [1024, "Repetidores"], [2048, "Lâmpadas de Redstone"], [512, "Pistões Aderentes"]]
display = [[2048, "Redstone"], [512, "Repetidores"], [256, "Comparadores"], [128, "Pistões"]]
supercomputador = [[8192, "Redstone"], [2048, "Repetidores"], [1024, "Comparadores"], [1024, "Pistões Aderentes"]]

uteis = []
inuteis = []

# Definindo o projeto e matriz base para conferir os componentes
nome_projeto = input()
if nome_projeto == "Memória ROM Simples":
    matriz = memoria
elif nome_projeto == "Calculadora de 4 bits":
    matriz = calculadora
elif nome_projeto == "Sequenciador Musical":
    matriz = sequenciador
elif nome_projeto == "Processador de 8 Bits":
    matriz = processador
elif nome_projeto == "Display de Vídeo 8x8":
    matriz = display
else:
    matriz = supercomputador

rodadas = 0
chave = False
while chave == False: # Loop para definir se ainda precisa receber mais componentes ou não
    componente_quantidade = input().split()
    while componente_quantidade != ['Construir!']:
        componente = ""
        quantidade = 0
        for i in range(len(componente_quantidade)-1):
            if i == len(componente_quantidade) - 2:
                componente += componente_quantidade[i]
            else:
                componente += componente_quantidade[i] + " "
        quantidade = int(componente_quantidade[-1])

        # Outputs de cada componente que foi coletado
        tem = False
        for j in range(len(matriz)):
            if componente == matriz[j][1]:
                tem = True
        if tem == False: # O componente não é útil para o projeto
            print(f"Hmm, {componente} não parece ser útil para este projeto.")
            inuteis.append([quantidade, componente])
        else:
            if componente == "Redstone":
                print(f"Mais redstone! A energia que move o progresso! (+{quantidade} Redstone)")
            elif componente == "Repetidores":
                print(f"Repetidores para garantir que o sinal chegue longe! Perfeito! (+{quantidade} Repetidores)")
            elif componente == "Tochas de Redstone":
                print(f"Tochas de Redstone! Ótimo para inverter um sinal ou energizar o sistema. (+{quantidade} Tochas de Redstone)")
            elif componente == "Lâmpadas de Redstone":
                print(f"Lâmpadas para o display! O resultado vai ficar bem visível. (+{quantidade} Lâmpadas de Redstone)")
            elif componente == "Blocos de Notas":
                print(f"Blocos de Notas! Quem sabe não rola uma musiquinha no final? (+{quantidade} Blocos de Notas)")
            elif componente == "Observadores":
                print(f"Observadores a postos! Nenhuma atualização de bloco passará despercebida. (+{quantidade} Observadores)")
            elif componente == "Comparadores":
                print(f"Comparadores para a lógica! A precisão é a alma do negócio. (+{quantidade} Comparadores)")
            elif componente == "Pistões":
                print(f"Pistões para mover as coisas de lugar. Isso vai ser útil! (+{quantidade} Pistões)")
            else:
                print(f"Pistões Aderentes! Perfeitos para criar mecanismos retráteis. (+{quantidade} Pistões Aderentes)")

            if rodadas > 0:
                quantidade_anterior = 0
                quantidade_total = quantidade_anterior + quantidade
                ja_tinha = False
                for z in range(len(uteis)):
                    if componente == uteis[z][1]:
                        quantidade_anterior = uteis[z][0]
                        quantidade_total = quantidade_anterior + quantidade
                        indice = z
                        ja_tinha = True
                if ja_tinha == True:
                    uteis[indice][0] = quantidade_total
                else:
                    uteis.append([quantidade_total, componente])
            else:
                uteis.append([quantidade, componente])

        componente_quantidade = input().split()

    print()
    igual = 0
    # Conferindo os componentes
    if len(uteis) == len(matriz):
        for i in range(len(uteis)):
            for j in range(len(uteis)):
                if uteis[j][1] == matriz[i][1]:
                    if uteis[j][0] >= matriz[i][0]:
                        igual+=1

    if igual == len(matriz): # Se tiver tudo completo
        print(f"Viniccius13 conseguiu construir o {nome_projeto}! Partiu programar!")
        print()
        print(f"Para construirmos a(o) {nome_projeto}, utilizamos:")
        print()
        for i in range(len(uteis)):
            print(f"{uteis[i][1]} : {uteis[i][0]}")
        
        if len(inuteis) > 0:
            print()
            print("Mas, em nossa jornada, também coletamos:")
            print()
            for i in range(len(inuteis)):
                print(f"{inuteis[i][1]} : {inuteis[i][0]}")
    
        chave = True
    else: # Tá faltando coisa
        faltantes = []
        for i in range(len(matriz)):
            componente_necessario = matriz[i][1]
            quantidade_necessaria = matriz[i][0]
            quantidade_coletada = 0

            for j in range(len(uteis)):
                if uteis[j][1] == componente_necessario:
                    quantidade_coletada = uteis[j][0]
                
            if quantidade_coletada < quantidade_necessaria:
                faltando = quantidade_necessaria - quantidade_coletada
                packs_faltando = faltando // 64

                if packs_faltando == 0:
                    packs_faltando = 1
                faltantes.append([packs_faltando, componente_necessario])
            
        
        print(f"Ainda não é possível construir o {nome_projeto}! Faltam:")
        print()
        for k in range(len(faltantes)):
            print(f"{faltantes[k][0]} pack(s) de {faltantes[k][1]}")
        print()
        
    rodadas+=1