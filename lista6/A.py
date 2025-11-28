# {endereço: {bairro: "", quartos: "", preço: ""}}
# score_compatibilidade = quartos * 10
# quartos >= quartos_min
# preço <= orçamento_max
catalogo = {}

# Função para adicionar casas no catálogo de Phil
def catalogando(n, catalogo):
    for i in range(n):
        dados = input().split(" - ")
        quartos_preco = dados[2].split("-")

        endereco = dados[1]
        bairro = dados[0]
        quartos = quartos_preco[0]
        preco = quartos_preco[1]

        catalogo.update({endereco: {'bairro': bairro, 'quartos': quartos, 'preço': preco}})

    return catalogo

def validacao(catalogo, requisitos):
    lista = []
    lista_keys = list(catalogo.keys()) # Lista dos endereços
    i = 0
    for info in catalogo.values():
        quartos = int(info['quartos'])
        preco = int(info['preço'])

        if quartos >= requisitos[0] and preco <= requisitos[1]: # Lista com as casas válidas e seus respectivos scores
            score_total = quartos * 10
            lista.append((lista_keys[i], score_total))
        
        i+=1

    return lista

def analise_melhor_casa(scores, catalogo):
    melhor_casa = ""
    melhor_score = 0
    for j in range(len(scores)):
        #endereco = scores[j][0]
        #bairro = catalogo[bairro]['bairro']
        #score_total = scores[j][1]

        if melhor_score < scores[j][1]:
            melhor_casa = scores[j][0] # Endereço
            melhor_score = scores[j][1] # Score

    bairro = catalogo[melhor_casa]['bairro'] # Bairro

    return melhor_casa, melhor_score, bairro

print("Phil, querido... Você tem certeza que essa música é literalmente sobre... casas?")
print("A própria Sabrina disse que nada na música é uma metáfora! Além disso, o sobrenome dela é carpinteira, acho que ela tem lugar de fala…")
print()

n_propriedades = int(input())
catalogo_completo = catalogando(n_propriedades, catalogo)
print("Catálogo concluído! Quem será que irá comprar uma casa de Phil?")
print()

vendas = 0
nome_cliente = input()
while nome_cliente != "FIM":
    # (quartos_min, orçamento_max)
    requisitos = input().split("-")
    tupla_requisitos = (int(requisitos[0]), int(requisitos[1]))

    scores = validacao(catalogo, tupla_requisitos)

    if len(scores) == 0: # Não tem casas válidas
        print(f"Puxa, {nome_cliente}, vou te avisar se algo aparecer. Não tenho nada com esses requisitos.")
        print()
    else:
        tupla_melhor_casa = analise_melhor_casa(scores, catalogo) # (endereço, score, bairro)

        print(f"🎤 Bem-vindo ao House Tour de {tupla_melhor_casa[2]}, {nome_cliente}!")
        print(f"➡ Casa: {tupla_melhor_casa[0]}")
        print(f"💖 Score: {tupla_melhor_casa[1]} pontos")
        print()

        if tupla_melhor_casa[1] >= 40:
            if nome_cliente == "Sabrina Carpenter":
                print('"Uau, Phil! Acho que finalmente encontrei o cenário perfeito para o clipe de House Tour!"')
            elif nome_cliente == "Taylor Swift":
                print('"Essa casa é perfeita para passar as férias na praia!"')
            else:
                print(f'"{nome_cliente} ficou encantado(a)! Phil comemora mais uma venda de sucesso!"')
            print()
            print('Venda concluída! Phil dança triunfante ao som de "House Tour"!')
            vendas+=1
        else:
            if nome_cliente == "Sabrina Carpenter":
                print('"Hmm... Sabe Phil, a letra não era tão literal assim…"')
            elif nome_cliente == "Taylor Swift":
                print('"Nós nunca vamos comprar essa casa juntos, Phil!"')
            else:
                print('"Parece que a música não ajudou nas vendas dessa vez…"')
            print()
            print('Talvez a Sabrina realmente não estivesse falando de imóveis…')
        print()

    nome_cliente = input()

# Relatório Final
print("===== RELATÓRIO DE VENDAS =====")
print(f"Total de casas vendidas: {vendas}")
print("===============================")
