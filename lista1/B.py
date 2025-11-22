# Entrada das informações
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
aulas_totais = int(input("Digite a quantidade de aulas totais: "))
faltas = int(input("Digite a quantidade de aulas faltadas: "))

# Cálculo da média e da presença
media = (nota1 + nota2 + nota3) / 3
presenca = ((aulas_totais - faltas)/aulas_totais) * 100

# Mostrando os resultados
print(f"Chris, você conseguiu média {media:.2f} e {presenca:.2f}% de presença.")

# Mostrando se Chris será aprovado ou não
if media >= 8.0 and presenca >= 75:
    print(f"Chris está APROVADO por nota e por presença! 🎉\nPisante maneiro, Chris! Agora é só torcer pros outros não vacilarem.")
elif media >= 7.0 and media < 8.0 and presenca >= 75:
    print(f"Chris está APROVADO! ✅\nSacomé, né? Passou raspando, mas a pizza ainda ficou longe.")
elif media >= 7.0 and presenca < 75:
    print(f"Chris ESTÁ REPROVADO por FALTA. ❌\nTrágico! Não adianta só saber, tem que aparecer.")
elif media < 7.0 and presenca >= 75:
    print(f"Chris ESTÁ REPROVADO por NOTA. ❌\nChris, já pro seu quarto ou eu vou te bater até você virar o avesso!")
else:
    print(f"Chris ESTÁ REPROVADO por NOTA e por FALTA. ❌\nChris, você perdeu o juízo? Eu trouxe você para esse mundo e posso muito bem tirar você dele.")
