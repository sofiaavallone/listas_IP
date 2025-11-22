influencers = ["Sofia Santino", "Doarda", "Ciclopin", "Bruna Pinheiro"]
cantores = ["Thiaguinho", "Little Thiago", "Neiff", "O Diferenciado", "Veigh", "Mc Loma"]
pautas = ["Medo de ficar musculosa demais por causa da academia", "O cara que eu gosto não me quer, mas eu continuo insistindo. Acha que eu consigo algo?", "Meu chefe só me dá um dia de folga, mas eu precisava de dois.", "Pessoas que adoram se fazer de coitadinhas", "Essa história de que homem sofre calado"]
convidados = []

total = 0
cont_influencers = 0
cont_cantores = 0
confirmacao = input()
while confirmacao != "WhatsApp: 0 mensagens." and confirmacao != "CABOSSE! Bora simbora organizar essa festa.":
    confirmacao_split = confirmacao.split()
    chave = False
    nome = ""
    for dado in confirmacao_split:
        if chave == False and dado != "acabou":
            nome += dado + " "
            if dado != confirmacao_split[0]:
                chave = True
        else:
            chave = True
    confirmado = nome.strip()
    total+=1
    convidados.append(confirmado)

    if confirmado == "Mc Loma":
        convidados.append("Mirella Santos")
        convidados.append("Mariely Santos")

    if confirmado in influencers:
        cont_influencers+=1
    elif confirmado in cantores:
        cont_cantores+=1
    
    confirmacao = input()

# Ninguém confirmou
if confirmacao == "WhatsApp: 0 mensagens.":
    print("I hate to tell you this BUT")
    print("Bia tava achando que ia fazer um mousse. O mousse virou uma piada, parceira")
    print()
    print("Como a vida não precisa ser only fechos, a gente vai finalizar minha franja hoje:")
    print("Essa chapinha eu dei literalmente tipo 50 reais nela. Não é a mais potente, não é a mais mais... mas ela é algo. Às vezes a gente só precisa ser algo, não precisa ser tudo.")
    print("E o protetor térmico? Vei, a chapinha sabe que eu tô fazendo de coração, ela nunca queimaria meu cabelo.")
    print("Espera esfriar e você vai barbarizar quando tiver pronto")
    print("É isso, tchau meus amores")
else:
    # Todos são cantores
    if total == cont_cantores:
        print("<PLANOS PARA FESTA>")
        convidados_print = ""
        for convidado in convidados:
            if convidado == convidados[-1]:
                convidados_print += convidado + "."
            else:
                convidados_print += convidado + ", "
        print("Convidados: " + convidados_print)
        print("Tipo de comemoração: Paredão - Show na minha casa!!")
    # Todos são influencers
    elif total == cont_influencers:
        print("<TARDE DE FOFOCAS>")
        convidados_print = ""
        for convidado in convidados:
            if convidado == convidados[-1]:
                convidados_print += convidado + "."
            else:
                convidados_print += convidado + ", "
        print("Convidados: " + convidados_print)

        # Pautas
        for i in range(len(convidados)):
            pauta = input()
            if pauta == pautas[0]:
                print("AMIGA, ouça: tem nem o P do PERIGO de você ficar grandona sem querer. Não se preocupe!")
            elif pauta == pautas[1]:
                print("Claro que consegue, amiga! Consegue virar uma palhaça, consegue perder a autoestima... Consegue várias coisas :)")
            elif pauta == pautas[2]:
                print("Tem que ter pelo menos dois dias de descanso. Se seu chefe tem uma empresa que não pode passar dois dias fechada porque vai quebrar, ele deveria fechar! Isso não é nem uma empresa, é um quiosque!")
            elif pauta == pautas[3]:
                print("Eu detesto quem gosta de ficar pagando de coitadinho(a). Se for chorar… Na verdade, não chora não, que eu não quero nem ouvir.")
            else:
                print("Vocês ficam dizendo que homem sofre, que homem sofre calado… E por que eu ainda estou ouvindo? Por que eu ainda ouço???")
        
        quant_concordaram = int(input())
        if quant_concordaram == 0:
            print("Apois me interne, me prenda, me jogue fora que eu tô maluca!")
        else:
            print("É isso, eu vejo tanta coisa errada nesse mundo… Mas é como dizem, né?! Life snake, a vida cobra em inglês.")
    # Tudo misturado
    else:
        print("Cachaçaria na minha casa hoje, 21h.")
        print("Todo mundo lá em casa! Tem que ser uma festa que dure muito, tipo 27 anos e 3 meses!!")
