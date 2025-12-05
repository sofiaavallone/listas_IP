def verificacao (entrada, ato, setlist, tempo_original, cont, tempo_atual):
    nome = entrada[0]
    genero = entrada[1]
    tempo_min_seg = entrada[2].split(":")
    tempo_seg = int(tempo_min_seg[0]) * 60 + int(tempo_min_seg[1])

    # Verificações
    if nome != "Actually Romantic": # Taylor diva master
        if (ato == 1 and (genero == "Hyperpop" or genero == "Pop")) or (ato == 2 and (genero == "Sentimental" or genero == "Ballad")) or (ato == 3 and (genero == "Hyperpop" or genero == "Banger")):
            if (tempo_atual + tempo_seg) <= tempo_original:
                # Passou por tudo, entâo adiciona na setlist
                lista = setlist[f"Ato {ato}"]
                lista.append((nome, genero, tempo_seg))
                tempo_atual+=tempo_seg
                
                print(f"{nome} adicionada ao Ato {ato} ;).")
            else:
                print(f"Muito longa! O Ato {ato} já está com {tempo_atual} segundos e essa música tem {tempo_seg} segundos.")
                cont+=1
        else:
            print("Gênero errado para esse ato! Cuidado, uma música deslocada mata a vibe de um show…")
            cont+=1
    else:
        cont+=1
    
    return setlist, tempo_atual, cont

def setlist_final(n):
    tempo = 0
    lista = setlist[f"Ato {n}"]
    if len(lista) > 0:
        for i in range(len(lista)):
            nome = lista[i][0]
            genero = lista[i][1]
            tempo+=lista[i][2]
            print(f"{nome} ({genero})")
    else:
        print("Nenhuma música adicionada a este Ato.")
    print(f"Duração total do ato: {tempo} segundos.")
    print()

setlist = {"Ato 1": [], "Ato 2": [], "Ato 3": []}

tempo_ato1 = 600
tempo_ato2 = 480
tempo_ato3 = 720

cont_music_descartadas = 0

print("Don't sleep, don't eat, just do it on repeat! Keep bumpin' that!!!")
print()

# Atos

for i in range(3):
    tempo_ato_atual = 0
    if i == 0:
        print(f"Iniciando montagem do Ato {i+1} (Hyperpop e Pop):")
    elif i == 1:
        print(f"Iniciando montagem do Ato {i+1} (Sentimental e Ballad):")
    else:
        print(f"Iniciando montagem do Ato {i+1} (Hyperpop e Banger):")
    print()

    entrada = input().split(", ")
    while entrada != ['FIM_ATO_1'] and entrada != ['FIM_ATO_2'] and entrada != ['FIM_SHOW']:
        print(f"Música em análise: {entrada[0]}")

        if entrada[0] == "Actually Romantic":
            print("Já não basta ter exposto a Charli nessa música, agora a Taylor quer que a própria cante? GOLPE BAIXÍSSIMO!!!")
        elif entrada[0] == "Talk Talk featuring troye sivan":
            print("A MAIOR AMIZADE DO POP NO PALCO? Talk to them in your own made-up language!")
        elif entrada[0] == "Von dutch a. g. cook remix featuring addison rae":
            print("‘CAUSE THEY’RE JUST LIVING THAT LIFE! Addison Rae, a maior revelação do pop desde Britney Spears, no palco ao lado da sua amiga Charli XCX!")
        elif entrada[0] == "Guess featuring billie eilish":
            print("Hey, Billie, you there?")

        if i == 0:
            retorno = verificacao(entrada, i+1, setlist, tempo_ato1, cont_music_descartadas, tempo_ato_atual)
            tempo_ato_atual = retorno[1]
        elif i == 1:
            retorno = verificacao(entrada, i+1, setlist, tempo_ato2, cont_music_descartadas, tempo_ato_atual)
            tempo_ato_atual = retorno[1]
        else:
            retorno = verificacao(entrada, i+1, setlist, tempo_ato3, cont_music_descartadas, tempo_ato_atual)
            tempo_ato_atual = retorno[1]
        
        cont_music_descartadas = retorno[2]
        setlist = retorno[0]

        entrada = input().split(", ")
        
    if i == 0:
        tempo_ato1 = tempo_ato_atual
    elif i == 1:
        tempo_ato2 = tempo_ato_atual
    else:
        tempo_ato3 = tempo_ato_atual

    print()

if (tempo_ato1 <= 0.7 * 600) or (tempo_ato2 <= 0.7 * 480) or (tempo_ato3 <= 0.7 * 720):
    print("Tem certeza que isso é um show? Rápido desse jeito, a Charli XCX deve estar pensando nos doces do backstage…")
    print()

# Setlist final
print("--- Ato 1 (Abertura) ---")
setlist_final(1)

print("--- Ato 2 (Sentimental) ---")
setlist_final(2)

print("--- Ato 3 (Encerramento) ---")
setlist_final(3)

# Resumo
musicas1 = setlist["Ato 1"]
musicas2 = setlist["Ato 2"]
musicas3 = setlist["Ato 3"]

print("=== RESUMO DO SHOW (BRAT APPROVED) ===")
print(f"Total de músicas na setlist: {len(musicas1) + len(musicas2) + len(musicas3)}")
print(f"Total de músicas barradas: {cont_music_descartadas}")
