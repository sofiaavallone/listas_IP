# Times oponentes possíveis
# Lorelei 
lorelei = [["Lapras", "agua", 220, 50, "Raio de Gelo", 60, "agua", 60],
    ["Blastoise", "agua", 180, 55, "Hidro Bomba", 65, "agua", 78],
    ["Victreebel", "grama", 160, 40, "Folha Navalha", 55, "grama", 70],
    ["Ninetales", "fogo", 170, 45, "Lança-chamas", 60, "fogo", 100]]

# Bruno
bruno = [["Charizard", "fogo", 190, 40, "Presa de Fogo", 70, "fogo", 100],
    ["Arcanine", "fogo", 180, 50, "Velocidade Extrema", 60, "fogo", 95],
    ["Kingler", "agua", 170, 60, "Caranguejo Martelo", 65, "agua", 75],
    ["Jolteon", "eletrico", 150, 35, "Choque do Trovão", 55, "eletrico", 130]]

# Agatha 
agatha = [["Venusaur", "grama", 180, 50, "Raio Solar", 70, "grama", 80],
    ["Vileplume", "grama", 160, 45, "Pó do Sono", 50, "grama", 50],
    ["Raichu", "eletrico", 160, 40, "Investida Trovão", 65, "eletrico", 110],
    ["Poliwrath", "agua", 190, 55, "Soco Dinâmico", 60, "agua", 70]]

# Lance 
lance = [["Electabuzz", "eletrico", 180, 45, "Soco de Trovão", 75, "eletrico", 105],
    ["Jolteon", "eletrico", 170, 35, "Onda de Trovão", 60, "eletrico", 130],
    ["Exeggutor", "grama", 160, 40, "Bomba de Semente", 65, "grama", 55],
    ["Magmar", "fogo", 175, 40, "Giro de Fogo", 55, "fogo", 93]]

time_jogador = []

# Fase de preparação
print("Hora de montar seu time Pokémon!")
for i in range(4): # Montagem do time jogador
    entrada = input().split(" - ") # Nome, tipo, HP, defesa, nome do ataque, poder do ataque, tipo do ataque, velocidade, HP inicial (adicionado lá na frente)
    time_jogador.append(entrada)

# Escolha do oponente
print()
print("Qual membro da Elite Four você deseja enfrentar?")
oponente = input().lower()
if oponente == "lorelei":
    time_oponente = lorelei.copy()
elif oponente == "bruno":
    time_oponente = bruno.copy()
elif oponente == "agatha":
    time_oponente = agatha.copy()
else:
    time_oponente = lance.copy()
print()

def iniciar (pokemon1, pokemon2):
    if int(pokemon2[7]) > int(pokemon1[7]):
        pokemon1, pokemon2 = pokemon2, pokemon1
    return [pokemon1, pokemon2]

# Função de cálculo do dano
def dano (pokemon1, pokemon2, atacante):
    tipo_pokemon1 = pokemon1[1]
    tipo_pokemon2 = pokemon2[1]

    if atacante == pokemon1:
        # Super efetivos
        if (tipo_pokemon1 == "fogo" and tipo_pokemon2 == "grama") or (tipo_pokemon1 == "agua" and tipo_pokemon2 == "fogo") or (tipo_pokemon1 == "grama" and tipo_pokemon2 == "agua") or (tipo_pokemon1 == "eletrico" and tipo_pokemon2 == "agua"):
            multiplicador_tipo = 2
            tipo_ataque = "super efetivo"
        # Não muito efetivo
        elif (tipo_pokemon1 == "grama" and tipo_pokemon2 == "fogo") or (tipo_pokemon1 == "fogo" and tipo_pokemon2 == "agua") or (tipo_pokemon1 == "agua" and tipo_pokemon2 == "grama") or (tipo_pokemon1 == "agua" and tipo_pokemon2 == "eletrico"):
            multiplicador_tipo = 0.5
            tipo_ataque = "não muito efetivo"
        # Neutro
        else:
            multiplicador_tipo = 1
            tipo_ataque = "neutro"

        # Calculando o dano
        poder_ataque = int(pokemon1[5])
        defesa_defensor = int(pokemon2[3])
        dano_final = int((poder_ataque - (defesa_defensor / 2)) * multiplicador_tipo)
    else:
        # Não muito efetivo
        if (tipo_pokemon1 == "fogo" and tipo_pokemon2 == "grama") or (tipo_pokemon1 == "agua" and tipo_pokemon2 == "fogo") or (tipo_pokemon1 == "grama" and tipo_pokemon2 == "agua") or (tipo_pokemon1 == "eletrico" and tipo_pokemon2 == "agua"):
            multiplicador_tipo = 0.5
            tipo_ataque = "não muito efetivo"
        # Super efetivo
        elif (tipo_pokemon1 == "grama" and tipo_pokemon2 == "fogo") or (tipo_pokemon1 == "fogo" and tipo_pokemon2 == "agua") or (tipo_pokemon1 == "agua" and tipo_pokemon2 == "grama") or (tipo_pokemon1 == "agua" and tipo_pokemon2 == "eletrico"):
            multiplicador_tipo = 2
            tipo_ataque = "super efetivo"
        # Neutro
        else:
            multiplicador_tipo = 1
            tipo_ataque = "neutro"

        # Calculando o dano
        poder_ataque = int(pokemon2[5])
        defesa_defensor = int(pokemon1[3])
        dano_final = int((poder_ataque - (defesa_defensor / 2)) * multiplicador_tipo)

    if dano_final <= 0:
        dano_final = 1

    return [tipo_ataque, dano_final]

# Função das batalhas de turnos (duelo individual)
def batalha_turnos (pokemon1, pokemon2, derrotados_jogador, derrotados_oponente, hp_inicial1, hp_inicial2):
    n_turno = 1
    while int(pokemon1[2]) > 0 and int(pokemon2[2]) > 0:
        print()
        print(f"-- Turno {n_turno} --")
        # Ataque do pokémon 1
        atacante = pokemon1

        lista_dano = dano(pokemon1, pokemon2, atacante)
        dano_final = lista_dano[1]
        tipo_ataque = lista_dano[0]

        if int(pokemon1[2]) > 0:
            print()
            if pokemon1 in time_jogador:
                print(f"{pokemon1[0]} usa {pokemon1[4]}!")
            else:
                print(f"{pokemon1[0]} do oponente usa {pokemon1[4]}!")

            if tipo_ataque == "super efetivo":
                print(f"{pokemon1[4]} é super efetivo!")
            elif tipo_ataque == "não muito efetivo":
                print(f"{pokemon1[4]} não é muito efetivo...")

            pokemon2[2] = int(pokemon2[2]) - dano_final
            if int(pokemon2[2]) < 0:
                pokemon2[2] = 0
            print(f"Causou {dano_final} de dano. HP de {pokemon2[0]} agora é {int(pokemon2[2])}/{hp_inicial2}.")

        # Ataque do pokémon 2
        atacante = pokemon2

        lista_dano = dano(pokemon1, pokemon2, atacante)
        dano_final = lista_dano[1]
        tipo_ataque = lista_dano[0]
        
        if int(pokemon2[2]) > 0:
            print()
            if pokemon2 in time_jogador:
                print(f"{pokemon2[0]} usa {pokemon2[4]}!")
            else:
                print(f"{pokemon2[0]} do oponente usa {pokemon2[4]}!")

            if tipo_ataque == "super efetivo":
                print(f"{pokemon2[4]} é super efetivo!")
            elif tipo_ataque == "não muito efetivo":
                print(f"{pokemon2[4]} não é muito efetivo...")

            pokemon1[2] = int(pokemon1[2]) - dano_final
            if int(pokemon1[2]) < 0:
                pokemon1[2] = 0
            print(f"Causou {dano_final} de dano. HP de {pokemon1[0]} agora é {int(pokemon1[2])}/{hp_inicial1}.")

        n_turno+=1

    # Fim do duelo
    print()
    if int(pokemon1[2]) <= 0:
        if pokemon1 in time_jogador:
            print(f"{pokemon1[0]} foi derrotado!")
            time_jogador.remove(pokemon1)
            derrotados_jogador+=1
        else:
            print(f"{pokemon1[0]} do oponente foi derrotado!")
            time_oponente.remove(pokemon1)
            derrotados_oponente+=1
    elif int(pokemon2[2]) <= 0:
        if pokemon2 in time_jogador:
            print(f"{pokemon2[0]} foi derrotado!")
            time_jogador.remove(pokemon2)
            derrotados_jogador+=1
        else:
            print(f"{pokemon2[0]} do oponente foi derrotado!")
            time_oponente.remove(pokemon2)
            derrotados_oponente+=1

    return [time_jogador, time_oponente, derrotados_jogador, derrotados_oponente]

# Batalhas
print("====================")
print("A BATALHA VAI COMEÇAR!")
print("====================")

derrotados_jogador = 0
derrotados_oponente = 0
n_rodada = 1
while len(time_oponente) > 0 and len(time_jogador) > 0:
    pokemon1 = time_jogador[0]
    pokemon2 = time_oponente[0]
    print()
    print(f"--- Rodada {n_rodada} ---")
    print(f"{pokemon1[0]}, eu escolho você!")
    print(f"{pokemon2[0]}, vai!")
    print("--------------------")
    # Definindo a ordem correta (de acordo com a velocidade)
    ordem = iniciar(pokemon1, pokemon2)
    pokemon1 = ordem[0] # Ataque
    pokemon2 = ordem[1] # Defesa
    pokemon1.append(pokemon1[2])
    pokemon2.append(pokemon2[2])
    hp_inicial1 = int(pokemon1[8])
    hp_inicial2 = int(pokemon2[8])

    lista_retorno_turnos = batalha_turnos(pokemon1, pokemon2, derrotados_jogador, derrotados_oponente, hp_inicial1, hp_inicial2)
    time_jogador = lista_retorno_turnos[0]
    time_oponente = lista_retorno_turnos[1]
    derrotados_jogador = lista_retorno_turnos[2]
    derrotados_oponente = lista_retorno_turnos[3]

    # Placar
    print()
    print("--------------------")
    print()
    print(f"Placar: {derrotados_oponente} X {derrotados_jogador}")

    n_rodada+=1

if len(time_jogador) > 0:
    print()
    print("========================================")
    print("Parabéns! Você venceu a batalha Pokémon!")
    print("========================================")
else:
    print("========================================")
    print("Que pena! Você foi derrotado.")
    print("========================================")
