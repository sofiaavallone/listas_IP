print("INICIANDO SIMULAÇÃO...")
jogador1 = input()
while jogador1 != "Arthur" and jogador1 != "Samuel":
    print("Jogador inválido! Essa competição é apenas entre Arthur e Samuel!")
    jogador1 = input()
print(f"{jogador1} começa na corda!")

if jogador1 == "Arthur":
    jogador2 = "Samuel"
else:
    jogador2 = "Arthur"

quant_rodadas = int(input())
jogando = jogador1
pontos_jogador1 = 0
pontos_jogador2 = 0

for i in range(1, quant_rodadas+1): # Partidas
    print(f"Começa a {i}ª rodada!")
    if i == quant_rodadas:
        print("Última rodada! Valendo 2 pontos!")
    
    ritmo = int(input())
    aposta = int(input())

    if jogando == jogador1:
        print(f"{jogador2} aposta que {jogador1} não chega a {aposta} pulos! Vamos ver se é verdade! O ritmo de {jogador1} será {ritmo}!")
    elif jogando == jogador2:
        print(f"{jogador1} aposta que {jogador2} não chega a {aposta} pulos! Vamos ver se é verdade! O ritmo de {jogador2} será {ritmo}!")

    pulos = 0
    tropecos = 0
    ja_printou = False
    restante = aposta
    while pulos * ritmo < aposta and tropecos < 3: # Rodadas
        cont_algarismos = 0
        for algarismos in str(restante):
            cont_algarismos+=int(algarismos)

        # Calculando se está na sequência de Fibonacci
        if ((5*(cont_algarismos**2) + 4) == int(((5*(cont_algarismos**2) + 4)**0.5))**2) or ((5*(cont_algarismos**2) - 4) == int(((5*(cont_algarismos**2) - 4)**0.5))**2):
            tropecos+=1
            print(f"O número da soma é {cont_algarismos}, que faz parte da sequência de Fibonacci!! {jogando} tropeça!")
        elif restante < aposta/4 and ja_printou == False:
            print(f"{jogando} está quase chegando ao apostado! Falta pouco!")
            ja_printou = True
        else:
            print(f"{jogando} pula com maestria! Faltam {aposta-pulos*ritmo} pulos!")
        
        if tropecos == 3:
            print(f"E agora não tem jeito, {jogando} cai de cara no chão!")
        
        pulos+=1
        restante = aposta - ritmo * pulos
    
    if pulos * ritmo < aposta/2:
        print(f"Nossa!! Parece que {jogando} não chegou nem na metade do apostado! Ainda bem que não foi competir pra valer no Round 6!")
    elif pulos * ritmo >= aposta/2 and pulos * ritmo <= (aposta*3)/4:
        print(f"Nem muito perto, nem muito longe do apostado. Talvez {jogando} teve apenas azar!")
    elif pulos * ritmo > (aposta*3)/4 and pulos * ritmo < aposta:
        print(f"Quase lá! por pouco {jogando} não alcançou o apostado!")
    elif pulos * ritmo == aposta and tropecos < 3:
        print(f"{jogando} cumpriu o prometido e alcançou {aposta} pulos! Ponto merecidíssimo!")
    else:  
        if jogando == jogador1 and tropecos < 3:
            print(f"{jogador1} vai além, e supera a aposta em {pulos*ritmo-aposta} Ponto(s)! Deixou o {jogador2} no chinelo!")
        else:
            if tropecos < 3:
                print(f"{jogador2} vai além, e supera a aposta em {pulos*ritmo-aposta} Ponto(s)! Deixou o {jogador1} no chinelo!")

    # Pontuando e atualizando quem está jogando
    if jogando == jogador1:
        if pulos * ritmo >= aposta and i == quant_rodadas and tropecos < 3:
            pontos_jogador1+=2
        elif pulos * ritmo >= aposta and tropecos < 3:
            pontos_jogador1+=1
        jogando = jogador2
    else:
        if pulos  * ritmo >= aposta and i == quant_rodadas and tropecos < 3:
            pontos_jogador2+=2
        elif pulos * ritmo >= aposta and tropecos < 3:
            pontos_jogador2+=1
        jogando = jogador1     

print("COMPUTANDO PREVISÃO FINAL...")
if pontos_jogador1>pontos_jogador2 and jogador1 == "Arthur":
    print(f"Arthur venceu a competição com {pontos_jogador1} ponto(s)! Trouxe orgulho para Maceió!")
elif pontos_jogador1>pontos_jogador2 and jogador1 == "Samuel":
    print(f"Samuel venceu a competição com {pontos_jogador1} ponto(s)! O Messi careca em sua foto de perfil ficaria impressionado se soubesse!")
elif pontos_jogador2>pontos_jogador1 and jogador2 == "Arthur":
    print(f"Arthur venceu a competição com {pontos_jogador2} ponto(s)! Trouxe orgulho para Maceió!")
elif pontos_jogador2>pontos_jogador1 and jogador2 == "Samuel":
    print(f"Samuel venceu a competição com {pontos_jogador2} ponto(s)! O Messi careca em sua foto de perfil ficaria impressionado se soubesse!")
elif pontos_jogador1 == pontos_jogador2 and pontos_jogador1 > 0:
    print(f"Houve um empate técnico! Ambos fizeram {pontos_jogador1} ponto(s)! Óbvio que os dois monitores mais rápidos iriam empatar!")
else:
    print("Ninguém pontuou! Que competição sem graça! Acho que os monitores se garantem mais nas dúvidas de IP mesmo...")