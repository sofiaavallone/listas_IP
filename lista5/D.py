# Função para descobrir conflitos
def livre(ala_atual, lote_atual, n, cemiterio):
    for i in range(ala_atual):
        if cemiterio[i][lote_atual] == 1:
            return False

    i = ala_atual - 1
    j = lote_atual - 1
    while i >= 0 and j >= 0:
        if cemiterio[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = ala_atual - 1
    j = lote_atual + 1
    while i >= 0 and j < n:
        if cemiterio[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

# Função para contar a quantidade de formas de organizar o cemitério (Backtracking)
def contagem(ala_atual, n, cemiterio, ala_ocupada, lote_ocupado):
    formas_organizacao = 0

    # Caso Base
    if ala_atual == n:
        return 1
    # Caso indutivo
    else:
        for lote in range(n):
            # Se não for o lote e ala ocupada
            if ala_atual != ala_ocupada or lote != lote_ocupado:
                if livre(ala_atual, lote, n, cemiterio):
                    cemiterio[ala_atual][lote] = 1
                    formas_organizacao+= contagem(ala_atual + 1, n, cemiterio, ala_ocupada, lote_ocupado)
                    cemiterio[ala_atual][lote] = 0
        
        return formas_organizacao

n = int(input()) # Almas, lotes e alas
cemiterio = []

# Lugar ocupado
chave = True
while chave:
    ala_ocupada = int(input()) - 1
    lote_ocupado = int(input()) - 1

    if (ala_ocupada <= n and ala_ocupada >= 0) and (lote_ocupado <= n and lote_ocupado >= 0):
        print(f"Rogério e Chaguinha conseguiram encontrar o túmulo ocupado em ({ala_ocupada + 1}, {lote_ocupado + 1})!")
        chave = False
    else:
        print(f"Rogério e Chaguinha não encontraram o túmulo ocupado na posição ({ala_ocupada + 1}, {lote_ocupado + 1}). Assim eles nunca vão conseguir sair do cemitério!")
print()

# Montando o cemitério vazio
for i in range(n):
    linha = [0] * n
    cemiterio.append(linha)

# Outputs
total_possibilidades = contagem(0, n, cemiterio, ala_ocupada, lote_ocupado)
print(f"Rogério e Chaguinha conseguiram encontrar {total_possibilidades} possíveis posições para as almas se posicionarem sem conflitos!")

if total_possibilidades == 0:
    print("Não existe nenhuma configuração segura para as almas... Rogério e Chaguinha estão presos no meio da guerra das almas!")
elif total_possibilidades >= 1 and total_possibilidades <= 10:
    print("Os amigos vão precisar tomar muito cuidado para não pegar um caminho errado!")
elif total_possibilidades > 10 and total_possibilidades <= 50:
    print("Uau! São tantas opções que eles até se perderam contando!")
else:
    print("Em pleno Halloween e as almas descansando em paz! Rogério e Chaguinha vão conseguir sair logo do cemitério.")
