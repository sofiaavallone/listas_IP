print(f"Ativando a máquina...\n")

# Entrada das informações
nome = input("Digite o nome do inventor: ").capitalize()
ano = int(input("Digite o ano da invenção: "))

# Contador da quantidade de letras no nome
cont_caracter = 0
for letra in nome:
    cont_caracter+=1

# Cálculo para decisão se é confiável ou não
if ano % cont_caracter == 0:
    if nome == "Frink":
        print(f"Professor Frink irá inventar o rebigulador?! A máquina deve estar com defeito! Glavin!")
    else:
        print(f"Previsão confiável! O rebigulador será real em {ano}!")
elif ano % cont_caracter != 0:
    if nome == "Frink":
        print(f"Nem precisava colocar os dados! O rebigulador jamais existiria em qualquer universo!")  
    else:
         print(f"Previsão instável! {nome} também deve achar que o rebigulador é ridículo...")
