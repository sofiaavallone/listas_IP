print("Sejam bem-vindos à Big Sub Brasil, onde a fama é temporária, os barracos são eternos, e só um vai conquistar o título de maior subcelebridade do país!")
maiores1 = []
menores1 = []
resto1 = []
matriz1 = []
maiores2 = []
menores2 = []
resto2 = []
matriz2 = []

participantes = input().split(", ")
participante1 = participantes[0].capitalize()
participante2 = participantes[1].capitalize()

print(f"{participante1} e {participante2} disputarão entre si.")

# Participante 1
entrada1 = input().split()
numeros1 = []
for n in entrada1:
    numeros1.append(int(n))
numeros1.sort()

maiores1 = numeros1[-3:]
matriz1.append(maiores1)
menores1 = numeros1[:3]
matriz1.append(menores1)
resto1.append(numeros1[3] + 1)
resto1.append(numeros1[4] + 1)
resto1.append(numeros1[5] + 1)
matriz1.append(resto1)
determinante1 = (matriz1[0][0]*matriz1[1][1]*matriz1[2][2]) + (matriz1[0][1]*matriz1[1][2]*matriz1[2][0]) + (matriz1[0][2]*matriz1[1][0]*matriz1[2][1]) - (matriz1[0][2]*matriz1[1][1]*matriz1[2][0]) - (matriz1[0][1]*matriz1[1][0]*matriz1[2][2]) - (matriz1[0][0]*matriz1[1][2]*matriz1[2][1])
for linha in matriz1:
    for i in range(len(linha)):
        if i == len(linha) - 1:
            print(linha[i], end="")
        else:
            print(linha[i], end=" ")
    print()
print(f"{participante1} está com pontuação {determinante1} pontos.")

# Participante 2
entrada2 = input().split()
numeros2 = []
for n in entrada2:
    numeros2.append(int(n))
numeros2.sort()

maiores2 = numeros2[-3:]
matriz2.append(maiores2)
menores2 = numeros2[:3]
matriz2.append(menores2)
resto2.append(numeros2[3] + 1)
resto2.append(numeros2[4] + 1)
resto2.append(numeros2[5] + 1)
matriz2.append(resto2)
determinante2 = (matriz2[0][0]*matriz2[1][1]*matriz2[2][2]) + (matriz2[0][1]*matriz2[1][2]*matriz2[2][0]) + (matriz2[0][2]*matriz2[1][0]*matriz2[2][1]) - (matriz2[0][2]*matriz2[1][1]*matriz2[2][0]) - (matriz2[0][1]*matriz2[1][0]*matriz2[2][2]) - (matriz2[0][0]*matriz2[1][2]*matriz2[2][1])
for linha in matriz2:
    for i in range(len(linha)):
        if i == len(linha) - 1:
            print(linha[i], end="")
        else:
            print(linha[i], end=" ")
    print()
print(f"{participante2} está com pontuação {determinante2} pontos.")

empate_total = False
# Resultado
if determinante1 == determinante2: # Empate
    print("RODADA DESEMPATE!!")
    if numeros1[6] > numeros2[6]: # 1 ganhou
        print(f"Contra todas as expectativas (inclusive as nossas), {participante1} venceu a rodada!")
        print(f"Seu momento de brilhar virou eclipse {participante2}. Melhor sorte no próximo flop!")
        ganhador = participante1
    elif numeros1[6] < numeros2[6]: # 2 ganhou
        print(f"Contra todas as expectativas (inclusive as nossas), {participante2} venceu a rodada!")
        print(f"Seu momento de brilhar virou eclipse {participante1}. Melhor sorte no próximo flop!")
        ganhador = participante2
    else: # Empate no empate
        print("Como isso é possível?? Os participantes empataram até na rodada desempate! EU DESISTO!!!")
        empate_total = True

if empate_total == False:
    if determinante1 > determinante2:
        print(f"Com talento duvidoso e esforço máximo, a vitória é de {participante1}!")
    elif determinante1 < determinante2:
        print(f"Com talento duvidoso e esforço máximo, a vitória é de {participante2}!")
    else:
        print(f"Com talento duvidoso e esforço máximo, a vitória é de {ganhador}!")