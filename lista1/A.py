# Informações dos competidores
nome_competidor1 = input("Digite o nome do primeiro competidor: ")
pasteis_competidor1 = int(input("Digite a quantidade de pastéis consumidos pelo competidor 1: "))
nome_competidor2 = input("Digite o nome do segundo competidor: ")
pasteis_competidor2 = int(input("Digite a quantidade de pastéis consumidos pelo competidor 2: "))
nome_competidor3 = input("Digite o nome do terceiro competidor: ")
pasteis_competidor3 = int(input("Digite a quantidade de pastéis consumidos pelo competidor 3: "))

# Comparação para saber o campeão
if pasteis_competidor1 > pasteis_competidor2:
    nome_campeao = nome_competidor1
    pasteis_campeao = pasteis_competidor1
elif pasteis_competidor1 < pasteis_competidor2: 
    nome_campeao = nome_competidor2
    pasteis_campeao = pasteis_competidor2

if pasteis_campeao < pasteis_competidor3:
    nome_campeao = nome_competidor3
    pasteis_campeao = pasteis_competidor3

# Especificações
if "Lineu" == nome_competidor1 or "Lineu" == nome_competidor2 or "Lineu" == nome_competidor3:
    print("Lineu comeu um pastel com gosto estranho e usou sua autoridade na vigilancia sanitaria para acabar com a competição, Beiçola tá desolado!")
else:
    # Revalção do campeão com outros comentários específicos
    print(f"A(O) campeã(o) é {nome_campeao}, com {pasteis_campeao} pastéis consumidos!")
    if "Floriano" == nome_competidor1 or "Floriano" == nome_competidor2 or "Floriano" == nome_competidor3:
        if nome_campeao != "Floriano":
            print(f"Anos comendo pastel e perdeu justo para {nome_campeao}, lastimável, Sr. Flor!")
    
    if nome_campeao == "Agostinho" and pasteis_campeao > 100:
        print("Acho que o Agostinho deve ter escondido alguns pastéis na calça, pilantra!")
    elif nome_campeao == "Agostinho" and pasteis_campeao > 50:
        print("Agostinho madrugou no taxi e veio cheio de fome para a competição!")
