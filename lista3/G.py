print("Iniciando investigação... Zé Felipe está focado.")
eventos = [] # Personagem, tipo de evento, hora início e hora fim
nivel_suspeita = 0

numero_eventos = int(input())
# Recebendo as informações e adicionando na matriz
for i in range(numero_eventos):
    entrada = input()
    linha_matriz = entrada.split(" - ")
    eventos.append(linha_matriz)

# Bubble sort para ordenar os eventos cronologicamente (Regra 0)
for i in range(len(eventos)-1):
    for j in range(len(eventos)-i-1):

        hora_inicio = int(eventos[j][-2].replace(":", ""))
        hora_inicio2 = int(eventos[j+1][-2].replace(":", ""))
        hora_fim = int(eventos[j][-1].replace(":", ""))
        hora_fim2 = int(eventos[j+1][-1].replace(":", ""))

        if hora_inicio > hora_inicio2:
            eventos[j], eventos[j+1] = eventos[j+1], eventos[j]
        elif hora_inicio == hora_inicio2:
            if hora_fim > hora_fim2:
                eventos[j], eventos[j+1] = eventos[j+1], eventos[j]

chave = False
i = 0
encontros_suspeitos = 0
alibis = 0
while i < len(eventos) and chave == False:
    # Evento inicial que está sendo analisado
    personagem = eventos[i][0]
    evento = eventos[i][1]
    inicio = int(eventos[i][2].replace(":", ""))
    fim = int(eventos[i][3].replace(":", ""))

    # Regra 1
    if personagem == "VJM":
        chave = True
        nivel_suspeita = 100
    else:
        for j in range(len(eventos)): # Comparando com o evento atual para pegar os eventos iguais
                # Evento que vai comparar com o inicial
                personagem2 = eventos[j][0]
                evento2 = eventos[j][1]
                inicio2 = int(eventos[j][2].replace(":", ""))
                fim2 = int(eventos[j][3].replace(":", ""))

                if evento2 == evento:
                    # Regra 2
                    if personagem2 == "JM" and personagem == "V":
                        if inicio < fim2 and inicio2 < fim:
                            nivel_suspeita+=35
                            encontros_suspeitos+=1
                    # Regra 3
                    elif personagem2 == "ZF" and personagem == "V":
                        if inicio < fim2 and inicio2 < fim:
                            nivel_suspeita-=20
                            if nivel_suspeita < 0:
                                nivel_suspeita = 0
                            alibis+=1
    i += 1

# Outputs
if chave == False:
    # Print da linha do tempo ordenada
    print()
    print("--- Linha do Tempo dos Eventos ---")
    for i in range(len(eventos)):
        if eventos[i][0] == "V":
            pessoa = "Virgínia"
        elif eventos[i][0] == "JM":
            pessoa = "Jogador Misterioso"
        elif eventos[i][0] == "ZF":
            pessoa = "Zé Felipe"
        else:
            pessoa = "Virgínia e Jogador Misterioso"
        print(f"{eventos[i][2]}-{eventos[i][3]}: {pessoa} - {eventos[i][1]}")
    # Resumo da análise
    print()
    print("--- Resumo da Análise ---")
    print(f"Encontros Suspeitos: {encontros_suspeitos}")
    print(f"Álibis Confirmados: {alibis}")

# Conclusão da análise
print()
if nivel_suspeita >= 100:
    print("TRAIÇÃO CONFIRMADA! Zé Felipe vai fazer uma música sobre isso.")
elif nivel_suspeita >= 70 and nivel_suspeita <= 99:
    print(f"Nível de Suspeita: {nivel_suspeita} - MUITO SUSPEITO! Zé Felipe vai ter uma conversa séria com a Virgínia.")
elif nivel_suspeita >= 30 and nivel_suspeita <= 69:
    print(f"Nível de Suspeita: {nivel_suspeita} - Hmmm, algo de estranho não está certo. Zé Felipe vai ficar de olho.")
else:
    print(f"Nível de Suspeita: {nivel_suspeita} - Não há motivo para preocupação. Zé Felipe pode respirar aliviado e voltar a brincar com a Maria Flor.")