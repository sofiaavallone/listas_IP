# Entrada da quantidade de bolinhas iniciais
bolinhas_a = int(input())
bolinhas_b = int(input())
bolinhas_c = int(input())

cont_vivos = 3
jogador = "a"
erro_consecutivo_a = 0
erro_consecutivo_b = 0
erro_consecutivo_c = 0
# Está ou não no jogo
vivo_a = True
vivo_b = True
vivo_c = True

while cont_vivos>=2:

    resultado = input()

    # André
    if jogador == "a":
        if resultado == "acertou" and cont_vivos > 2:
            bolinhas_a+=2
            bolinhas_b-=1
            bolinhas_c-=1
            erro_consecutivo_a = 0
        elif resultado == "acertou" and cont_vivos == 2:
            bolinhas_a+=1
            bolinhas_b-=1
            bolinhas_c-=1
            erro_consecutivo_a = 0
        else:
            erro_consecutivo_a+=1
            # Saiu porque errou 3x consecutivas
            if erro_consecutivo_a == 3:
                vivo_a = False
                cont_vivos-=1
                print("andre perdeu feio")
    # Bruno
    elif jogador == "b":
        if resultado == "acertou" and cont_vivos > 2:
            bolinhas_b+=2
            bolinhas_a-=1
            bolinhas_c-=1
            erro_consecutivo_b = 0
        elif resultado == "acertou" and cont_vivos == 2:
            bolinhas_b+=1
            bolinhas_a-=1
            bolinhas_c-=1
            erro_consecutivo_b = 0
        else:
            erro_consecutivo_b+=1
            # Saiu porque errou 3x consecutivas
            if erro_consecutivo_b == 3:
                vivo_b = False
                cont_vivos-=1
                print("bruno perdeu feio")
    # Clara
    else:
        if resultado == "acertou" and cont_vivos > 2:
            bolinhas_c+=2
            bolinhas_a-=1
            bolinhas_b-=1
            erro_consecutivo_c = 0
        elif resultado == "acertou" and cont_vivos == 2:
            bolinhas_c+=1
            bolinhas_a-=1
            bolinhas_b-=1
            erro_consecutivo_c = 0
        else:
            erro_consecutivo_c+=1
            # Saiu porque errou 3x consecutivas
            if erro_consecutivo_c == 3:
                vivo_c = False
                cont_vivos-=1
                print("clara perdeu feio")
    
    # André saiu porque acabou as bolinhas
    if bolinhas_a == 0 and vivo_a == True:
        cont_vivos-=1
        vivo_a = False
        print("andre saiu do jogo")
    # Bruno saiu porque acabou as bolinhas
    if bolinhas_b == 0 and vivo_b == True:
        cont_vivos-=1
        vivo_b = False
        print("bruno saiu do jogo")
    # Clara saiu porque acabou as bolinhas
    if bolinhas_c == 0 and vivo_c == True:
        cont_vivos-=1
        vivo_c = False
        print("clara saiu do jogo")

    if jogador == "a" and vivo_b == True:
        jogador = "b"
    elif jogador == "a" and vivo_b == False:
        jogador = "c"
    elif jogador == "b" and vivo_c == True:
        jogador = "c"
    elif jogador == "b" and vivo_c == False:
        jogador = "a"
    elif jogador == "c" and vivo_a == True:
        jogador = "a"
    elif jogador == "c" and vivo_a == False:
        jogador = "b"

if bolinhas_a < 0:
    bolinhas_a = 0
if bolinhas_b < 0:
    bolinhas_b = 0
if bolinhas_c < 0:
    bolinhas_c = 0

if bolinhas_a>bolinhas_b and bolinhas_a>bolinhas_c:
    print("andre ganhou")
elif bolinhas_b>bolinhas_a and bolinhas_b>bolinhas_c:
    print("bruno ganhou")
else:
    print("clara ganhou")

# Saída das bolinhas finais
print("a quantidade final de bolas foi:")
print(f"andre: {bolinhas_a}")
print(f"bruno: {bolinhas_b}")
print(f"clara: {bolinhas_c}")
