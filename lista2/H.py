vivos1 = 6
vivos2 = 6
mortos1 = 0
mortos2 = 0
print("Serão 12 desenvolvedores defendendo a honra de seus lados do código! Que vença a melhor stack!")

# Definindo os times
time1 = input()
while time1 != "Front-End" and time1 != "Back-End":
    print("Entrada inválida!")
    time1 = input()

if time1 == "Front-End":
    time2 = "Back-End"
else:
    time2 = "Front-End"

time_jogando = time1
lugar = "c"
while vivos1 != 0 and vivos2 !=0:
    # Ataque em campo
    while lugar == "c" and vivos1 > 0 and vivos2 > 0:
        chave = False
        resultado_ataque = input()
        while resultado_ataque != "acertou" and resultado_ataque != "errou":
            print("Entrada inválida!")
            resultado_ataque = input()
        # Time 1 atacando
        if time_jogando == time1:
            if resultado_ataque == "acertou":
                print(f"{time1} acertou um jogador!")
                vivos2-=1
                mortos2+=1
                if time1 == "Back-End":
                    print(f"Back-End: {vivos1} dev(s) em campo. | Front-End: {vivos2} dev(s) em campo.")
                else:
                    print(f"Back-End: {vivos2} dev(s) em campo. | Front-End: {vivos1} dev(s) em campo.")
                lugar = "m"
                time_jogando = time2
            else:
                if mortos1 == 0:
                    time_jogando = time2
                    chave = True
                else:
                    resultado_defesa = input()
                    while resultado_defesa != "pegou" and resultado_defesa != "deixou":
                        print("Entrada inválida!")
                        resultado_defesa = input()
                    if resultado_defesa == "pegou":
                        time_jogando = time2
                        chave = True
                    else:
                        lugar = "m"
                        time_jogando = time1
                        chave = True
        # Time 2 atacando
        if time_jogando == time2 and lugar == "c" and chave == False:
            if resultado_ataque == "acertou":
                print(f"{time2} acertou um jogador!")
                vivos1-=1
                mortos1+=1
                if time1 == "Back-End":
                    print(f"Back-End: {vivos1} dev(s) em campo. | Front-End: {vivos2} dev(s) em campo.")
                else:
                    print(f"Back-End: {vivos2} dev(s) em campo. | Front-End: {vivos1} dev(s) em campo.")
                lugar = "m"
                time_jogando = time1
            else:
                if mortos2 == 0:
                    time_jogando = time1
                else:
                    resultado_defesa = input()
                    while resultado_defesa != "pegou" and resultado_defesa != "deixou":
                        print("Entrada inválida!")
                        resultado_defesa = input()
                    if resultado_defesa == "pegou":
                        time_jogando = time1
                    else:
                        lugar = "m"
                        time_jogando = time2
    # Ataque no morto
    while lugar == "m" and vivos1 > 0 and vivos2 > 0:
        # Morto time 1
        if time_jogando == time1:  
            resultado_ataque = input()
            while resultado_ataque != "acertou" and resultado_ataque != "errou":
                print("Entrada inválida!")
                resultado_ataque = input()
            if resultado_ataque == "acertou":
                print(f"O morto do {time1} acertou um jogador!")
                vivos1+=1
                mortos1-=1
                vivos2-=1
                mortos2+=1
                if time1 == "Back-End":
                    print(f"Back-End: {vivos1} dev(s) em campo. | Front-End: {vivos2} dev(s) em campo.")
                else:
                    print(f"Back-End: {vivos2} dev(s) em campo. | Front-End: {vivos1} dev(s) em campo.")
                time_jogando = time2
            else:
                resultado_defesa = input()
                while resultado_defesa != "pegou" and resultado_defesa != "deixou":
                    print("Entrada inválida!")
                    resultado_defesa = input()
                if resultado_defesa == "pegou":
                    time_jogando = time2
                    lugar = "c"
                else:
                    lugar = "c"
                    time_jogando = time1
        # Morto time 2
        else:
            resultado_ataque = input()
            while resultado_ataque != "acertou" and resultado_ataque != "errou":
                print("Entrada inválida!")
                resultado_ataque = input()
            if resultado_ataque == "acertou":
                print(f"O morto do {time2} acertou um jogador!")
                vivos2+=1
                mortos2-=1
                vivos1-=1
                mortos1+=1
                if time1 == "Back-End":
                    print(f"Back-End: {vivos1} dev(s) em campo. | Front-End: {vivos2} dev(s) em campo.")
                else:
                    print(f"Back-End: {vivos2} dev(s) em campo. | Front-End: {vivos1} dev(s) em campo.")
                time_jogando = time1
            else:
                resultado_defesa = input()
                while resultado_defesa != "pegou" and resultado_defesa != "deixou":
                    print("Entrada inválida!")
                    resultado_defesa = input()
                if resultado_defesa == "pegou":
                    time_jogando = time1
                    lugar = "c"
                else:
                    lugar = "c"
                    time_jogando = time2
                    
if vivos1>vivos2 and time1 == "Back-End":
    print(f"Vitória do Back-End! Restaram {vivos1} devs ainda mantendo o servidor de pé!")
elif vivos1>vivos2 and time2 == "Back-End":
    print(f"Vitória do Front-End! Restaram {vivos1} devs ainda segurando o layout!")
elif vivos2>vivos1 and time1 == "Front-End":
    print(f"Vitória do Back-End! Restaram {vivos2} devs ainda mantendo o servidor de pé!")
elif vivos2>vivos1 and time2 == "Front-End":
    print(f"Vitória do Front-End! Restaram {vivos2} devs ainda segurando o layout!")
