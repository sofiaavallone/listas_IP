n = int(input()) # Número de tentativas dos jogadores

completou_ana = False
completou_adrieli = False
completou_joab = False
completou_duda = False

cont_vencedores = 0

for i in range(n): # Ana
    pulo_ana = int(input())
    if pulo_ana == 5:
        completou_ana = True

print(f"Ana tentou {n} vezes e completou a última casa {pulo_ana}")
if completou_ana == True:
    print("Ana completou a amarelinha!")
    cont_vencedores+=1
else:
    print("Ana não conseguiu completar a amarelinha!")

for i in range(n): # Adrieli
    pulo_adrieli = int(input())
    if pulo_adrieli == 5:
        completou_adrieli = True
    
print(f"Adrieli tentou {n} vezes e completou a última casa {pulo_adrieli}")
if completou_adrieli == True:
    print("Adrieli completou a amarelinha!")
    cont_vencedores+=1
else:
    print("Adrieli não conseguiu completar a amarelinha!")

for i in range(n): # Joab
    pulo_joab = int(input())
    if pulo_joab == 5:
        completou_joab = True

print(f"Joab tentou {n} vezes e completou a última casa {pulo_joab}")
if completou_joab == True:
    print("Joab completou a amarelinha!")
    cont_vencedores+=1
else:
    print("Joab não conseguiu completar a amarelinha!")

for i in range(n): # Duda
    pulo_duda = int(input())
    if pulo_duda == 5:
        completou_duda = True

print(f"Duda tentou {n} vezes e completou a última casa {pulo_duda}")
if completou_duda == True:
    print("Duda completou a amarelinha!")
    cont_vencedores+=1
else:
    print("Duda não conseguiu completar a amarelinha!")

if cont_vencedores == 1:
    if completou_ana == True and completou_adrieli == False and completou_joab == False and completou_duda == False:
        print("O vencedor é Ana!")
    elif completou_ana == False and completou_adrieli == True and completou_joab == False and completou_duda == False:
        print("O vencedor é Adrieli!")
    elif completou_ana == False and completou_adrieli == False and completou_joab == True and completou_duda == False:
        print("O vencedor é Joab!")
    elif completou_ana == False and completou_adrieli == False and completou_joab == False and completou_duda == True:
        print("O vencedor é Duda!")
elif cont_vencedores == 2:
    if completou_ana == True and completou_adrieli == True and completou_joab == False and completou_duda == False:
        print("Houve empate entre: Ana, Adrieli")
    elif completou_ana == True and completou_adrieli == False and completou_joab == True and completou_duda == False:
        print("Houve empate entre: Ana, Joab")
    elif completou_ana == True and completou_adrieli == False and completou_joab == False and completou_duda == True:
        print("Houve empate entre: Ana, Duda")
    elif completou_ana == False and completou_adrieli == True and completou_joab == False and completou_duda == False:
        print("Houve empate entre: Adrieli, Joab")
    elif completou_ana == False and completou_adrieli == True and completou_joab == False and completou_duda == True:
        print("Houve empate entre: Adrieli, Duda")
    elif completou_ana == False and completou_adrieli == True and completou_joab == True and completou_duda == True:
        print("Houve empate entre: Joab, Duda")
elif cont_vencedores == 3:
    if completou_ana == True and completou_adrieli == True and completou_joab == True and completou_duda == False:
        print("Houve empate entre: Ana, Adrieli, Joab")
    elif completou_ana == True and completou_adrieli == True and completou_joab == False and completou_duda == True:
        print("Houve empate entre: Ana, Adrieli, Duda")
    elif completou_ana == True and completou_adrieli == False and completou_joab == True and completou_duda == True:
        print("Houve empate entre: Ana, Joab, Duda")
    elif completou_ana  == False and completou_adrieli == True and completou_joab == True and completou_duda == True:
        print("Houve empate entre: Adrieli, Joab, Duda")
else:
    print("Houve empate entre: Ana, Adrieli, Joab, Duda")