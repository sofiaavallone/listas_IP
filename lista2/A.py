print("Vai começar a brincadeira! Será que a palavra vai ficar igual até o fim?")
n = int(input("Digite um número: "))

cont_trocas = 0 # Contador de erros
acerto = True

for i in range(n):
    jogador = input(f"Nome jogador {i+1}: ")

    # Atualizando a palavra anterior e recebendo a atual
    if i == 0:
        palavra_inicial = input("Digite a palavra: ")
    else:
        if i == 1:
            palavra_anterior = palavra_inicial
            palavra_atual = input("Digite a palavra: ")
        else:
            palavra_anterior = palavra_atual
            palavra_atual = input("Digite a palavra: ")
    
    # Conferindo se a palavra atual está errada
    if i != 0 and palavra_atual != palavra_anterior:
        acerto = False
        print(f"Parece que {jogador} não conseguiu ouvir muito bem e acabou passando pra frente uma palavra diferente da que escutou…")
        cont_trocas+=1 # Alimentando contador de erros
        if cont_trocas == 1:
            jogador_errado1 = jogador
            palavra_errada1 = palavra_atual
        elif cont_trocas == 2:
            jogador_errado2 = jogador
    
    if cont_trocas == 5 and acerto == False:
        print(f"Caramba, que confusão! A palavra {palavra_inicial} já tá toda embaralhada e virou {palavra_atual}!")

    # Conferindo o resultado final
    if i == n-1:
        if palavra_atual == palavra_inicial and cont_trocas == 0:
            print(f"Impressionante, todos os jogadores ouviram e falaram perfeitamente a palavra {palavra_inicial}! Talvez os telefones modernos comecem a perder espaço pra moda antiga.")
        elif palavra_atual == palavra_inicial and cont_trocas != 0:
            print(f"Parece que ocorreram {cont_trocas} trocas durante o processo, mas mesmo com essa pequena confusão, a palavra {palavra_inicial} conseguiu chegar no fim do telefone sem fio.")
        elif palavra_atual != palavra_inicial and cont_trocas == 1:
            print(f"Poxa, foi por pouco, só quem errou foi {jogador_errado1} que disse {palavra_errada1} ao invés de {palavra_inicial}…")
        elif palavra_atual != palavra_inicial and cont_trocas == 2:
            print(f"Se não fosse pelos erros de {jogador_errado1} e {jogador_errado2} a palavra {palavra_inicial} poderia ter chegado até o fim, talvez eles devessem tentar de novo.")
        elif palavra_atual != palavra_inicial and cont_trocas > 2:
            print(f"É, parece que os alunos se confundiram bastante durante a brincadeira e a palavra {palavra_inicial} acabou virando {palavra_atual}. No total, ocorreram {cont_trocas} trocas.")