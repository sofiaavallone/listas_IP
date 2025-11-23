def particao(n, k):
    if n == 0:
        return 1
    elif n < 0 or k == 0:
        return 0
    else:
        return particao(n, k-1) + particao(n-k, k)
    

print("DOCES OU TRAVESSURAS???")

quant_doces = int(input())

quant_particoes = particao(quant_doces, quant_doces)

print(f"sem travessuras por hoje! tenho {quant_particoes} sacolinhas pra vocês")

if quant_particoes % 2 != 0:
    print("hmm... número ímpar de sacolinhas 🍭 cuidado com as bruxas!")
else:
    print("doces equilibrados, sem travessuras!")