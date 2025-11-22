monitores = ["Adrieli Queiroz", "Arthur Jorge", "César Cavalcanti", "Elisson Oliveira", "Filipe Moreira", "Gabriela Alves", "Joab Henrique", "Maria Fernanda", "Miriam Gonzaga", "Sofia Remindes"]
monitores_disponiveis = ["Adrieli Queiroz", "Arthur Jorge", "César Cavalcanti", "Elisson Oliveira", "Filipe Moreira", "Gabriela Alves", "Joab Henrique", "Maria Fernanda", "Miriam Gonzaga", "Sofia Remindes"]
desfilantes = []
intrusos = []
numero_desfilantes = int(input())

marca_patrocinador = input()
if marca_patrocinador == "Tha Beauty":
    patrocinador = "Thais Linares"
elif marca_patrocinador == "DeGuê?":
    patrocinador = "Davi Brito"
else:
    patrocinador = "Edu e Fih"

# Recebendo os desfilantes
cont_invasoes = 0
core = False
for i in range(numero_desfilantes):
    desfilante = input()
    if desfilante in monitores:
        desfilantes.append(desfilante)
        monitores_disponiveis.remove(desfilante)
    # Invasão tolerada (patrocinador)
    elif desfilante == patrocinador:
        if cont_invasoes == 3 and core == False:
            desfilantes.append("Core")
            desfilantes.append(desfilante)
            intrusos.append(desfilante)
            core = True
        else:
            desfilantes.append(desfilante)
    # Invasão não tolerada
    else:
        if cont_invasoes == 3 and core == False:
            desfilantes.append("Core")
            desfilantes.append(desfilante)
            intrusos.append(desfilante)
            core = True
        else:
            desfilantes.append(desfilante)
            intrusos.append(desfilante)
        cont_invasoes+=1
    
    if cont_invasoes == 3 and core == False:
            desfilantes.append("Core")
            core = True


# Substituindo os invasores não tolerados e outputs
print("Senhoras e senhores, o desfile de gala do CIn vai começar!")
for i in range(len(desfilantes)):
    s_substituicao = False

    if desfilantes[i] not in monitores and desfilantes[i] != patrocinador and desfilantes[i] != "Core":
        print(f"{desfilantes[i]} invadiu a passarela! Segurem ele(a), produção!")
        if len(monitores_disponiveis) > 0:
            desfilantes[i] = monitores_disponiveis[0]
            monitores_disponiveis.remove(monitores_disponiveis[0])
        else:
            s_substituicao = True

    if desfilantes[i] == patrocinador:
        print(f"Invasão tolerada por motivos de patrocínio!")
    elif desfilantes[i] == "Core":
        print("Muitas invasões estão deixando a galera irritada... Chama o Core pra acalmar os ânimos!")

    if s_substituicao == False:
        print(f"Desfilante de n° {i+1}: {desfilantes[i]}!")
    else:
        print(f"Desfilante de n° {i+1}: {desfilantes[i]}?! Pelo visto não havia como substituir...")

# Outputs especiais
if "Gretchen" in intrusos or "Tulla Luana" in intrusos or "Inês Brasil" in intrusos:
    print("Nas arquibancadas do CIn, sussurros indignados agitam a multidão...")
    for i in range(len(intrusos)):
        if intrusos[i] == "Gretchen":
            print('"Eles tem que respeitar os meus 37 anos de carreira! Eu hoje sou um ícone, se eu morrer hoje eu vou continuar sendo a Gretchen!"')
        elif intrusos[i] == "Tulla Luana":
            print('"Ninguém ser humano está acima de mim! Mas eu estou acima de muitos... é assim que eu penso."')
        elif intrusos[i] == "Inês Brasil":
            print('"É aquele ditado... Vamo fazer o quê?"')
