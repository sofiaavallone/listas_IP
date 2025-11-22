print("--- Simulador de Cancelamento ---")
print()
n_artistas = int(input())
artista_seguidores = [] # Artista, seguidores, acontecimento

for i in range(n_artistas):
    informacoes = input()
    informacoes_split = informacoes.split(" - ")
    artista_seguidores.append(informacoes_split)

for i in range(len(artista_seguidores)):
    print(f"A subcelebridade da vez é: {artista_seguidores[i][0]}")
    artista_seguidores[i].append(int(input()))

    # Acontecimento 1
    if artista_seguidores[i][-1] == 1:
        print(f"{artista_seguidores[i][0]} perdeu 10% dos seguidores!")
        seguidores = int(artista_seguidores[i][1])
        seguidores -= (0.1 * seguidores)
        artista_seguidores[i][1] = int(seguidores)
    # Acontecimento 2
    elif artista_seguidores[i][-1] == 2:
        print(f"{artista_seguidores[i][0]} ganhou 5% de seguidores!")
        seguidores = int(artista_seguidores[i][1])
        seguidores += (0.05 * seguidores)
        artista_seguidores[i][1] = int(seguidores)
    # Acontecimento 3
    elif artista_seguidores[i][-1] == 3:
        print(f"{artista_seguidores[i][0]} perdeu 15% dos seguidores!")
        seguidores = int(artista_seguidores[i][1])
        seguidores -= (0.15 * seguidores)
        artista_seguidores[i][1] = int(seguidores)
    # Outros acontecimentos
    else:
        print("Nenhum evento relevante. Seguidores continuam os mesmos.")

print()
print("--- RANKING FINAL DE SEGUIDORES ---")
# Bubble Sort
for k in range(n_artistas-1):
    for z in range(n_artistas-k-1):
        if int(artista_seguidores[z][1]) < int(artista_seguidores[z+1][1]):
            artista_seguidores[z], artista_seguidores[z+1] = artista_seguidores[z+1], artista_seguidores[z]

top3 = artista_seguidores[:3]

for i in range(len(top3)):
    print(f"{i+1}º Lugar: {top3[i][0]} com {top3[i][1]} seguidores.")
