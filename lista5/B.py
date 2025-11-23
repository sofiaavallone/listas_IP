def possibilidades(valor, notas, nota_observada, modo):
    # Caso base
    if valor == 0:
        if modo == 0:
            return 1
        else:
            return 0
    elif valor < 0 or len(notas) == 0:
        return 0
    # Caso indutivo
    else:
        resto = notas[1:]
        nota = notas[0]

        resultado = possibilidades(valor - nota, notas, nota_observada, modo) + possibilidades(valor, resto, nota_observada, modo)

        if modo == 1 and nota == nota_observada:
            resultado+=possibilidades(valor - nota, notas, nota_observada, 0)

    return resultado

notas = [100, 50, 20, 10, 5]

valor_conta = int(input())
print(f"Calculando possibilidades para o valor: {valor_conta}")

formas_de_pagar = possibilidades(valor_conta, notas, 0, 0) # Modo 0 = contagem de possibilidades

if formas_de_pagar == 1:
    print("\nEssa foi fácil! Só existe 1 possibilidade de pagar essa conta.")
elif formas_de_pagar == 0:
    print("\nInfelizmente, não há como pagar essa conta com as notas disponíveis.")

print(f"\nTotal de possibilidades: {formas_de_pagar}")
print("\nUso das notas:")
for nota in notas:
    usos = possibilidades(valor_conta, notas, nota, 1) # Modo 1 = contagem de recorrências
    print(f"R${nota}: usada em {usos} combinações")
