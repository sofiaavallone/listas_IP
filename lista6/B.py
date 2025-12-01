# Categoria: item principal: quantidade

def checagem_especifica(palavra):
    retorno = exigencias.get(palavra, False)
    if retorno != False:
        if retorno[0] == "Gloss":
            if retorno[1] <= 0:
                print("TUDO! O Gloss tá on. O look de Glinda tá salvo!")
            else:
                print("CADÊ meu gloss? Como divarei? ... A Glinda tá chorando de raiva!")
        if retorno[0] == "latte":
            if retorno[1] <= 0:
                print("Latte gelado pronto! A voz de Glinda está salva. Pode vir o próximo take")
            else:
                print("Cadeia neles! Faltou o Mimo Sagrado. Essa equipe tá perdida!")
            
exigencias = {}

# Fase 1
exigencia = input().split(": ")
while len(exigencia) == 3:
    if exigencia[0] == "Bebidas" and exigencia[1] == "latte":
        exigencia[2] = int(exigencia[2]) + 1
    exigencias.update({exigencia[0]: (exigencia[1], exigencia[2])})

    exigencia = input().split(": ")

# Fase 2
reabastecimento = input().split()
while len(reabastecimento) == 8:
    categoria = reabastecimento[5]
    quantidade = int(reabastecimento[1])

    # Lógica de estoque
    retorno_get = exigencias.get(categoria, False)

    if retorno_get != False:
        tupla_inicial = exigencias[categoria]
        tupla_atualizada = (tupla_inicial[0], int(tupla_inicial[1]) - quantidade)
        exigencias.update({categoria: tupla_atualizada})

    reabastecimento = input().split()

# Relatório Final
estoque_negativo = 0
print("Relatório de Balanço Final:")
for categoria, tupla in exigencias.items():
    item = tupla[0]
    quantidade = int(tupla[1])

    # Frase
    if quantidade <= 0:
        frase = "Você entregou TUDO! O mimo tá mais que garantido."
    else:
        frase = f"Golpe BAIXÍSSIMO! Faltam {quantidade} mimos. Corre!"
        estoque_negativo+=1

    print(f"Categoria: {categoria} Item: {item} Status: {frase}")
print()

# Checagem específicas
checagem_especifica('Maquiagem')
checagem_especifica('Bebidas')

print()
# Veredito final
print("Veredito Final")
if estoque_negativo >= 3:
    print("Thank U, Next! A equipe de camarim foi demitida!")
else:
    print("Estoque Aprovado! Glinda vai brilhar em Wicked!")
