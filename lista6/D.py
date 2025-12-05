# Seção 1
vida_amorosa = {'Jake Gyllenhaal': ('All too Well', 'We are never getting back together', 'Red', 2010), 'Joe Jonas': ('Forever & Always', 'Holy Ground', 2008), 'Taylor Lautner': ('Back to December', 'I can see you', 'Midnight rain', 2009), 'Tom Hiddleston': ('Getaway Car', 2016), 'Joe Alwyn': ('Paper Rings', 'Lover', 'So Long London', 2020), 'Harry Styles': ('Style', 'Out of the Woods', 'All You Had to Do Was Stay', 2012), 'Travis Kelce': ('The Fate of Ophelia', 'The Alchemy', 'Wi$h Li$t', 2023)}

# Seção 2
eras = {'Fearless': ('Ganhou o VMA 2009, porém Kanye West interrompeu seu discurso de vitória. Também ganhou o Grammy de Álbum do Ano (2010), sendo a artista mais jovem da história (na época) a receber esse prêmio.',), 
        'Speak Now': ('Teve uma turnê mundial massiva que consolidou seu status de superestrela global, o albúm Speak Now vendeu mais de 1 milhão de cópias na primeira semana, superando qualquer outro álbum dos últimos dois anos.',),
        '1989': ('“1989” tornou-se o primeiro álbum de Taylor exclusivamente pop; a artista emplacou dois hits mundiais: Blank Space e Bad Blood. Fun Fact: Taylor nasceu em 13 de dezembro de 1989.',),
        'Reputation': ('O álbum foi uma resposta à mídia, às traições públicas e ao controle da narrativa sobre sua imagem. Além disso, em 2019, Taylor tem os direitos autorais de seus álbuns roubados.',),
        'The Eras Tour': ('The Eras Tour é uma turnê comemorativa, com detalhes que buscam fazer jus á tudo que Taylor Swift fez e alcançou em seus anos de carreira. No Brasil, aconteceram seis apresentações em novembro de 2023 em São Paulo e no Rio de Janeiro.',)}

albuns_roubados = []

status = ''
entrada = input()
while entrada != "Já chega de fatos sobre a Taylor, vai fazer a lista de IP":
    if entrada == "Qual a situação de relacionamento?":
        pessoa = input()
        ano = int(input())

        tupla = vida_amorosa[pessoa]
        if tupla[-1] == ano:
            status = 'estão namorando'
        else:
            status = 'não estão namorando'

        print(f"{pessoa} e Taylor Swift {status} em {ano}" )
    elif entrada == "Qual pessoa está relacionada essa música?":
        musica = input()
        pessoa_relacionada = ''

        for key, value in vida_amorosa.items():
            for song in value:
                if song == musica:
                    pessoa_relacionada = key

        print(f"A pessoa relacionada é {pessoa_relacionada}, Taylor nunca erra em suas músicas")
    elif entrada == "Quais são todas as músicas relacionadas a essa pessoa?":
        pessoa = input()

        print(f"Cartas de amor ou indiretas, as músicas dedicadas a {pessoa} são: ", end='')
        for key, value in vida_amorosa.items():
            if key == pessoa:
                nova_tupla = value[:-1]
                for i in range(len(nova_tupla)):
                    if i != len(nova_tupla)-1:
                        print(f"{nova_tupla[i]}", end=", ")
                    else:
                        print(nova_tupla[i])
    elif entrada == "O que aconteceu nessa era?":
        era = input()

        if era == "Fearless":
            valor = eras['Fearless']
            print(valor[0])
        elif era == "Speak Now":
            valor = eras['Speak Now']
            print(valor[0])
        elif era == "1989":
            valor = eras['1989']
            print(valor[0])
        elif era == "Reputation":
            valor = eras['Reputation']
            print(valor[0])
        else:
            valor = eras['The Eras']
            print(valor[0])
    elif entrada == "Wayne nunca deixará Taylor vencer! O CIn precisa manter o hate na diva pop, eu vou alterar as informações":
        era = input()

        print("Cuidado, há um impostor no guia... Informações comprometidas")

        tupla = eras[era]
        nova_tupla = (tupla[0] + ' Que grande mentira! Taylor Swift só mente',)
        eras[era] = nova_tupla
    else:
        era = input()

        print(f"Para onde foi a história sobre {era}? Parece que alguém roubou tudo e não avisou a Taylor")

        albuns_roubados.append(era)
        eras.pop(era)

    entrada = input()

if len(albuns_roubados) > 0:
    print("Big Machine Records roubou:")
    for i in range(len(albuns_roubados)):
        print(albuns_roubados[i])
