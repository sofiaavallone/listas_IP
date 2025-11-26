# {endereço: {bairro: "", quartos: "", preço: ""}}
# score_compatibilidade = quartos * 10
# quartos >= quartos_min
# preço <= orçamento_max
catalogo = {}
scores = []

# Função para adicionar casas no catálogo de Phil
def catalogando(n, catalogo):
    for i in range(n):
        dados = input().split(" - ")
        quartos_preco = dados[2].split("-")

        endereco = dados[1]
        bairro = dados[0]
        quartos = quartos_preco[0]
        preco = quartos_preco[1]

        catalogo.update({endereco: {'bairro': bairro, 'quartos': quartos, 'preco': preco}})

    return catalogo

print("Phil, querido... Você tem certeza que essa música é literalmente sobre... casas?")
print("A própria Sabrina disse que nada na música é uma metáfora! Além disso, o sobrenome dela é carpinteira, acho que ela tem lugar de fala…")
print()

n_propriedades = int(input())
catalogo_completo = catalogando(n_propriedades, catalogo)
print("Catálogo concluído! Quem será que irá comprar uma casa de Phil?")
print()

nome_cliente = input()
while nome_cliente != "FIM":
    # (quartos_min, orçamento_max)
    tupla_requisitos = (int(requisitos[0]), int(requisitos[1]))

    lista_keys = list(catalogo.keys())
    i = 0
    for info in catalogo.values():
        quartos = info['quartos']
        preco = info['preço']

        if quartos >= tupla_requisitos[0] and preco <= tupla_requisitos[1]:
            score_total = quartos * 10
            scores.append((lista_keys[i], score_total))
        
        i+=1

    if len(scores) == 0: # Não tem casas válidas
        print(f"Puxa, {nome_cliente}, vou te avisar se algo aparecer. Não tenho nada com esses requisitos.")
        print()
    #else:
        # print das casas válidas
    # Bubble sort para achar o maior score (com opção de empate)

    nome_cliente = input()
    requisitos = input().split("-")