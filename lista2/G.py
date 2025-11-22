print("Começa agora o treinamento para grande final mundial de cabo de guerra!")
quant_partidas = 0
# Loop com condição para o número de partidas serem ímpar
while quant_partidas%2 == 0:
    if quant_partidas != 0:
        print("Não deverá haver empates! O número de partidas deverá ser ímpar.")
    quant_partidas = int(input())
print(f"Eles batalharão em {quant_partidas} longas partidas.")

# Entradas
forca_arthur = int(input())
forca_joao = int(input())
resistencia_inicial = int(input())

# Variáveis para saber quantas partidas ganhou
pontos_partida_joao = 0
pontos_partida_arthur = 0

i=0
while (i < quant_partidas) and (abs(pontos_partida_arthur-pontos_partida_joao) <= quant_partidas-i): # Partidas
    i+=1
    print(f"Começa a {i}ª partida!")
    print(f"Placar geral: {pontos_partida_arthur} X {pontos_partida_joao}")
    resistencia_arthur = resistencia_inicial
    resistencia_joao = resistencia_inicial

    # Variáveis para saber quantas rodadas ganhou
    pontos_rodada_joao = 0
    pontos_rodada_arthur = 0

    while resistencia_arthur != 0 and resistencia_joao != 0: # Rodadas
        primo = True
        num = int(input())
        if num < 2:
            primo = False
        else:
            for j in range(2, num): # Conferindo se o número é primo
                if num % j == 0:
                    primo = False
        
        if primo == True: # João ganhou a rodada
            resistencia_joao+=1
            resistencia_arthur-=1
            pontos_rodada_joao+=1
            print("O primo do primo é primo do primo? João puxa mais forte!")
        elif int(num**0.5) == num**0.5: # Arthur ganhou a rodada
            resistencia_arthur+=1
            resistencia_joao-=1
            pontos_rodada_arthur+=1
            print("O número é um quadrado perfeito! Arthur consegue puxar mais forte.")
        else:
            if forca_arthur>forca_joao: # Arthur ganhou por força
                resistencia_arthur+=1
                resistencia_joao-=1
                pontos_rodada_arthur+=1
                print("Arthur é o mais forte! João não consegue segurar.")
            else: # João ganhou por força
                resistencia_joao+=1
                resistencia_arthur-=1
                pontos_rodada_joao+=1
                print("João é o mais forte! Arthur não consegue segurar.")
    
    if pontos_rodada_joao>pontos_rodada_arthur: # João ganhou a partida
        pontos_partida_joao+=1
        print("João usa seus talentos de mangueboy e leva essa para casa!")
    else: # Arthur ganhou a partida
        pontos_partida_arthur+=1
        print("Arthur dá orgulho para Maceió e ganha a partida!")

print()
print("Agora eles estão prontos para o mundial!")
print(f"Placar final: {pontos_partida_arthur} X {pontos_partida_joao}")
# Conferindo quem ganhou/perdeu
if pontos_partida_joao>pontos_partida_arthur:
    perdedor = "Arthur"
    vencedor = "João"
else:
    perdedor = "João"
    vencedor = "Arthur"

# Prints específicos dos resultados
if perdedor == "Arthur" and pontos_partida_arthur == 0:
    print(f"{perdedor} não teve chance! {vencedor} venceu todas as partidas.")
elif perdedor == "João" and pontos_partida_joao == 0:
    print(f"{perdedor} não teve chance! {vencedor} venceu todas as partidas.")
elif vencedor == "Arthur":
    print(f"O ganhador foi {vencedor} com uma diferença de {pontos_partida_arthur-pontos_partida_joao} partidas.")
else:
    print(f"O ganhador foi {vencedor} com uma diferença de {pontos_partida_joao-pontos_partida_arthur} partidas.")
