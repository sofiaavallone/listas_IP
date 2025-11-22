# Entrada dos valores
artigos_s = int(input("Digite o número de artigos lidos por Sheldon: "))
artigos_l = int(input("Digite o número de artigos lidos por Leonard: "))
artigos_r = int(input("Digite o número de artigos lidos por Raj: "))
artigos_h = int(input("Digite o número de artigos lidos por Howard: "))
experimentos_s = int(input("Digite o número de experimentos realizados por Sheldon: "))
experimentos_l = int(input("Digite o número de experimentos realizados por Leonard: "))
experimentos_r = int(input("Digite o número de experimentos realizados por Raj: "))
experimentos_h = int(input("Digite o número de experimentos realizados por Howard: "))

# Cálculo das pontuações
pontuacao_s = artigos_s * 2 + experimentos_s * 3
pontuacao_l = artigos_l * 2 + experimentos_l * 3
pontuacao_r = artigos_r * 2 + experimentos_r * 3
pontuacao_h = artigos_h * 2 + experimentos_h * 3

# Saída das pontuações de cada um
print(f"Pontuação final:")
print(f"Sheldon: {pontuacao_s}")
print(f"Leonard: {pontuacao_l}")
print(f"Raj: {pontuacao_r}")
print(f"Howard: {pontuacao_h}\n")

# Descobrir o vencedor
if pontuacao_s > pontuacao_r:
    vencedor = pontuacao_s
    vencedor_nome = "Sheldon"
else:
    vencedor = pontuacao_r
    vencedor_nome = "Raj"
if pontuacao_l > vencedor:
    vencedor = pontuacao_l
    vencedor_nome = "Leonard"
if pontuacao_h > vencedor:
    vencedor = pontuacao_h
    vencedor_nome = "Howard"

# Conferir empates
empate_s = pontuacao_s == vencedor
empate_l = pontuacao_l == vencedor
empate_r = pontuacao_r == vencedor
empate_h = pontuacao_h == vencedor

# Declarando vencedores em cada caso de empate
if empate_s:
    vencedor_nome = "Sheldon"
elif empate_l:
    vencedor_nome = "Leonard"
elif empate_r:
    vencedor_nome = "Raj"
elif empate_h:
    vencedor_nome = "Howard"

# Saída do resultado
print(f"O cientista da semana é: {vencedor_nome}")
if vencedor_nome == "Sheldon":
    print("Não é atoa que ele ganhou o prêmio Nobel")
elif vencedor_nome == "Leonard":
    print("A vitória dele prova que aguentar o Sheldon já é um experimento científico por si só.")
elif vencedor_nome == "Raj":
    print("Ele comemora... mas ainda precisa da ajuda do cachorro para falar com mulheres.")
elif vencedor_nome == "Howard":
    print("Um pequeno passo para a ciência, um grande salto para alguém com mestrado.")
