doces = int(input("Digite a qauntidade de doces: "))
jogador1 = input("Digite o nome do jogador 1: ")
jogador2 = input("Digite o nome do jogador 2: ")
rodadas = int(doces/10)
# Tratando a rodada se não for divisível por 10
if doces%10 != 0:
    rodadas = (doces // 10) + 1

# Conferindo se Arthur está ou não no jogo
if jogador1 != "Arthur" and jogador2 != "Arthur":
    print("Epa!!! E cadê o dono dos doces??")
else:
    print("A batalha vai começar!")
    # Rodadas
    for i in range(rodadas):
        vidas1 = 10
        vidas2 = 10
        if i == 0 and doces%10 != 0:
            print(f"Pra aquecer, essa primeira vale menos, só {doces%10} doces!")
        else:
            print(f"Batalha número {i+1}!")
        
        # Turnos
        while vidas1 > 0 and vidas2 > 0:
            jogada1 = input("Digite a jogada do primeiro jogador: ")
            jogada2 = input("Digite a jogada do segundo jogador: ")

            # Empate
            if jogada1 == jogada2:
                print("Eita, jogaram a mesma coisa dessa vez.")
            # Papel e tesoura
            elif (jogada1 == "papel" and jogada2 == "tesoura") or (jogada1 == "tesoura" and jogada2 == "papel"):
                if jogada1 == "papel":
                    vidas1-=3
                    vidas2+=1
                else:
                    vidas1+=1
                    vidas2-=3
            # Pedra e papel
            elif (jogada1 == "pedra" and jogada2 == "papel") or (jogada1 == "papel" and jogada2 == "pedra"):
                if jogada1 == "papel":
                    vidas1+=2
                    vidas2-=2
                else:
                    vidas1-=2
                    vidas2+=2
            # Pedra e tesoura
            elif (jogada1 == "pedra" and jogada2 == "tesoura") or (jogada1 == "tesoura" and jogada2 == "pedra"):
                if jogada1 == "pedra":
                    vidas2-=4
                else:
                    vidas1-=4
            
            if jogada1 != jogada2:
                print(f"Esse turno terminou com {jogador1} tendo {vidas1} de vida e {jogador2} tendo {vidas2}!")

        if vidas1 == 0:
            vencedor = jogador2
        else:
            vencedor = jogador1
        print(f"A rodada {i+1} vai para {vencedor}, que garante seus doces!")