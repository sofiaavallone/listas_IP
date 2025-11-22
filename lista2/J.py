print("Que comece o jogo! Adivinhe a palavra, mas cuidado para não cair na armadilha.")

numero_rodadas = int(input())

for i in range(numero_rodadas): # Rodadas
    print(f"Rodada {i+1}/{numero_rodadas}:")

    palavra_secreta = input().lower()

    chave = False
    while chave == False: # While para receber a palavra fantasma nas condições
        palavra_fantasma = input().lower()

        letras_iguais = 0
        ja_contadas = ""

        for letra in palavra_fantasma: # Conferindo quantas letras iguais as palavras tem
            if letra in palavra_secreta and letra not in ja_contadas:
                letras_iguais +=1
                ja_contadas += letra
        
        if letras_iguais >= 3:
            chave = False
            print(f"A palavra fantasma possui {letras_iguais} letras presentes na palavra secreta. Tente uma com menos de 3 letras iguais.")
        else:
            chave = True

    acertou = False
    vidas_adivinho = 6
    letras_chutadas = ""
    letras_descobertas = "_"*len(palavra_secreta)
    tentativas = 0

    # Print inicial da palavra
    print(f"Palavra:", end="")
    for caracter in letras_descobertas:
        print(f" {caracter}", end="")
    print()
    while acertou == False and vidas_adivinho > 0:
        chute = input().lower()

        if chute in palavra_secreta and chute not in letras_chutadas: 
            ps_completando = ""
            for letra_secreta, letra_descoberta in zip(palavra_secreta, letras_descobertas): # Colocando a letra no seu lugar na palavra
                if letra_secreta == chute:
                    ps_completando += chute
                else:
                    ps_completando += letra_descoberta
            
            letras_descobertas = ps_completando
            print(f"Boa! A letra '{chute}' está na palavra.")
        elif chute in letras_chutadas:
            print(f"Você já tentou a letra '{chute}'. Tente outra.")
        elif chute not in palavra_secreta and chute not in palavra_fantasma:
            vidas_adivinho-=1
            print(f"Naao! A letra '{chute}' não está na palavra. Você perdeu 1 vida.")
        elif chute not in palavra_secreta and chute in palavra_fantasma:
            vidas_adivinho-=2
            print(f"CUIDADO! A letra '{chute}' é uma armadilha! Você perdeu 2 vidas.")

        if letras_descobertas == palavra_secreta:
            acertou = True

        if letras_descobertas != palavra_secreta and chute not in letras_chutadas and vidas_adivinho > 0:
            letras_chutadas += chute
            tentativas += 1
            print("=====================")
            print(f"Palavra:", end="")
            for caracter in letras_descobertas:
                print(f" {caracter}", end="")
            print()
            print(f"Vidas restantes: {vidas_adivinho}")
            saida = "Letras chutadas: "
            for j in range(len(letras_chutadas)):
                saida += letras_chutadas[j]
                if j != len(letras_chutadas) - 1:
                    saida += ", "
            print(saida)
            print("=====================")
    
    if acertou == True:
        print(f"Parabéns, Adivinho! Você descobriu a palavra secreta: {palavra_secreta.capitalize()}.")
        print(f"Total de tentativas: {tentativas+1}")
    else:
        print(f"Fim de jogo! A forca está completa e o Adivinho perdeu. A palavra secreta era: {palavra_secreta.capitalize()}.")
