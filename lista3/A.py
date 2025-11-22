frases = ['Que tiro foi esse?', 'Segura a marimba', 'Tá com raiva? Morde as costas', 'Bateu de frente é só rajadão']
quant_novas_frases = int(input())

for i in range(quant_novas_frases):
    frases.append(input())

# Contabilizando as repetições
frases2 = []
for j in range(len(frases)):
    repeticoes = 0
    for frase in frases:
        if frases[j] == frase:
            repeticoes+=1
    
    if j == 0 and repeticoes > 0:
        frases2.append(frases[j])
        print(f'"{frases2[-1]}": {repeticoes}')

    if repeticoes > 0 and not(frases[j] in frases2):
        frases2.append(frases[j])
        print(f'"{frases2[-1]}": {repeticoes}')

frases.sort()
print(frases)