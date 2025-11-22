vidas_m = 100

def resultado_ataque (vidas_m, ataque): # Função com os ataques de Badeline
    if ataque == "Você não tem o que é necessário para escalar.":
        vidas_m-=20
        print("Eu nunca vou conseguir chegar ao topo :(")
    elif ataque == "NÓS NUNCA DEVERÍAMOS TER SAÍDO DE CASA! VAMOS MORRER NESSA MONTANHA!":
        vidas_m-=50
        print("NAAÃO EU NUNCA DEVERIA TER INVENTADO DE ESCALAR ESSA MONTANHA!")

    return vidas_m

def resultado_reacao (vidas_m, reacao): # Função para somar as vidas de acordo com a reação de Madeline
    if reacao == "Calma Badeline, nós vamos conseguir.":
        vidas_m+=25
    elif reacao == "Eu sei que somos capazes! Vamos em frente!":
        respiracoes = int(input())
        vidas_m+=respiracoes*10
    elif reacao == "Madeline, nós estamos com você. Continue!":
        vidas_m+=60
    
    return vidas_m

while vidas_m > 0 and vidas_m < 150:
    ataque = input()
    vidas_m = resultado_ataque(vidas_m, ataque) # Atualizando as vidas e printando o resultado
    if vidas_m > 0 and vidas_m < 150:
        reacao = input()
        vidas_m = resultado_reacao(vidas_m, reacao)

if vidas_m >= 150:
    print("Madeline chegou ao topo! Ela se senta em um banco para descansar e apreciar a vista.")
elif vidas_m <= 0:
    print("Madeline e Badeline não conseguiram se entender... parece que elas nunca vão ver a cidade de cima.")