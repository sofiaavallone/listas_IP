alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T' ,'U', 'V' ,'W', 'X', 'Y' ,'Z']
frase_criptografada_lista = []
armadilhas = []

# Mi = índice da letra da frase descriptografada
# Ci = índice da letra da frase criptografada
# Ki = índice da chave
# fórmula para descobrir o Mi (índice da letra da frase descriptografada): Mi = (Ci - Ki) % 26

def decriptacao(alfabeto, frase_inicial, chave):
    # Caso base
    if len(frase_inicial) == 0:
        return ""
    # Caso indutivo
    else:
        for i in range(len(alfabeto)):
            if alfabeto[i] == chave:
                Ki = i
            
            if alfabeto[i] == frase_inicial[0]:
                Ci = i
        frase_inicial.pop(0)
        
        Mi = (Ci - Ki) % 26
        chave = alfabeto[Mi]

        return chave + decriptacao(alfabeto, frase_inicial, chave)

chave_inicial = input()
frase_criptografada = input()
# Retirando as armadilhas
for i in range(len(frase_criptografada)):
    frase_criptografada_lista.append(frase_criptografada[i])
    if frase_criptografada[i] not in alfabeto:
        armadilhas.append(i)
        frase_criptografada_lista.pop()

# Outputs
print("Decifrando mensagem do Trickster...")
if len(armadilhas) > 0:
    print(f"Esse Trickster é um picareta mesmo. Foram encontradas armadilhas nas posições:", end=" ")
    for i in range(len(armadilhas)):
        if i != len(armadilhas)-1:
            print(f"{armadilhas[i]}", end=", ")
        else:
            print(f"{armadilhas[i]}")
else:
    print("Nenhuma armadilha encontrada! Até que o Trickster foi bonzinho.")

frase_decifrada = decriptacao(alfabeto, frase_criptografada_lista, chave_inicial)

print(f"Mensagem revelada: {frase_decifrada}")
