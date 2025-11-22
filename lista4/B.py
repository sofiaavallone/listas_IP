nomes_digitais = []

# Cabeçalho
print("TRIBUNAL EM SESSÃO")
print("Juiz: Que comece o julgamento do caso em pauta.")
print()

# Diálogos iniciais
print("Promotor Edgeworth: A promotoria está pronta, Meritíssimo.")
print("Phoenix Wright: (Lá vamos nós... A reputação do escritório está em jogo.) A defesa está pronta.")
print()

# Sala de visitas
print("--- SALA DE VISITAS DO TRIBUNAL ---")
print("João Guilherme: Sr. Wright, eu juro, eu não o matei! Eu estive lá, mas... é só isso!")
print("Phoenix Wright: (Eu sinto que ele está escondendo algo... Devo pressioná-lo por mais detalhes ou confiar no que ele me disse?)")
print()

# Inputs e continuação do julgamento
escolha_inicial = input()

print("--- DE VOLTA AO TRIBUNAL ---")
print("Juiz: Promotoria, apresente as evidências.")
print("Promotor Edgeworth: A promotoria acusa este homem pelo crime de assassinato...")
print("Promotor Edgeworth: ...João Guilherme!")
print("Promotor Edgeworth: Comecemos com a evidência virtual chave, o registro da última modificação no computador da vítima.")

hora_modificacao = int(input())

print("Promotor Edgeworth: E, de acordo com o legista, a hora exata da morte.")

hora_morte = int(input())

print("Promotor Edgeworth: Finalmente, a prova irrefutável. O relatório de digitais da arma do crime, o troféu.")

numero_digitais = int(input())

print("Promotor Edgeworth: Que o escrivão leia os nomes encontrados na arma...")

for i in range(numero_digitais):
    nomes_digitais.append(input())

print()
print("ARGUMENTOS FINAIS")
print()

# Hora da modificação é posterior a da morte = INOCENTE
    # Tem as digitais de Elisson
# Não tem as digitais de JG = INOCENTE
# CULPADO 

digital_joao = False
digital_elisson = False
houve_contradicao = False
veredito = ""

def verificar_joao (numero_digitais, nomes_digitais, digital_joao): # Verificando se tem a digital de João Gui
    for i in range(numero_digitais):
        if nomes_digitais[i] == "João Guilherme":
            digital_joao = True
    
    return digital_joao

def verificar_elisson (numero_digitais, nomes_digitais, digital_elisson): # Verificando se tem a digital de Elisson
    for i in range(numero_digitais):
        if nomes_digitais[i] == "Elisson":
            digital_elisson = True
    
    return digital_elisson

def houve_modificacao (houve_contradicao): # Verificando se há contradição temporal
    if hora_modificacao > hora_morte:
        houve_contradicao =True
    
    return houve_contradicao

# Atualizando as variáveis com as funções
houve_contradicao = houve_modificacao(houve_contradicao)
digital_elisson = verificar_elisson(numero_digitais, nomes_digitais, digital_elisson)
digital_joao = verificar_joao(numero_digitais, nomes_digitais, digital_joao)

if escolha_inicial == "pressionar": # A escolha foi pressionar
    # Cena do flashback com a confissão de João Gui
    print("--- FLASHBACK: SALA DE VISITAS ---")
    print("Phoenix Wright: HOLD IT! João, não é só isso! Eu não posso te defender se você não me contar tudo. O que realmente aconteceu naquela noite?")
    print("João Guilherme: (soluço)... Certo... Eu vou contar. Não era sobre a rixa... era sobre o 'Ticket Fantasma'.")
    print("João Guilherme: Um bug impossível no sistema da faculdade. Eu criei um código que o resolvia. Era a minha chance de conseguir o estágio dos sonhos.")
    print("João Guilherme: Eu... eu confiei em Arthur. Mostrei o código a ele para uma revisão. E ele... ele o roubou. Apresentou como se fosse dele, levou todo o crédito.")
    print("João Guilherme: E o pior, Sr. Wright... eu cometi o erro de comentar sobre meu progresso com o Elisson, o 'monitor do povo'. Ele era o único, além de mim e de Arthur, que sabia da história toda. Ele observava nossa agilidade com os tickets com um sentimento sombrio! Se houver dedo dele nisso, ele certamente tentará depôr para contar do roubo do meu código por Arthur para me incriminar!")
    print("--- FIM DO FLASHBACK ---")
    print()

    # Argumento inicial da promotoria e a objeção da defesa
    print("Promotor Edgeworth: A lógica é simples. O acusado tinha o motivo, suas digitais estão na arma, e a perícia mostra que o arquivo do 'Ticket Fantasma' foi modificado após a morte, provando que ele permaneceu na cena do crime!")
    print("Phoenix Wright: OBJEÇÃO!")
    print()

    # Regras do veredito (sub-bifurcação)
    if houve_contradicao == True: 
        veredito = "INOCENTE"
        print("Phoenix Wright: A sua lógica tem uma falha fatal, promotor! É impossível que meu cliente tenha modificado aquele arquivo!")
        print("Phoenix Wright: Pois a defesa pode provar que, no exato momento da modificação, João Guilherme estava a quilômetros de distância, comprando um café na 'Cafeteria Byte'! Temos o registro da transação e uma testemunha ocular!")
        print("Phoenix Wright: A contradição temporal, combinada com este álibi, prova apenas uma coisa: a existência de uma terceira pessoa na cena do crime!")

        if digital_elisson == True: # Elisson foi pego
            print("Phoenix Wright: Se meu cliente tem um álibi, quem poderia ser? Quem alteraria o arquivo do 'Ticket Fantasma' para incriminar João Guilherme?")
            print("Phoenix Wright: Só poderia ser alguém que conhecia a história... alguém que meu cliente confessou ter contado!")
            print("Phoenix Wright: A defesa descobriu que apenas UMA outra pessoa sabia da história do código... uma pessoa cujas digitais, convenientemente, também estão na arma do crime!")
            print("Phoenix Wright: A pessoa que matou Arthur Sean para eliminar um rival e incriminar o outro foi você...")
            print("Phoenix Wright: ELISSON!!!")
            print()
            print("Elisson: N-NÃÃÃÃÃOOOOO! COMO... ELE TE CONTOU?! MEU PLANO ERA PERFEITO!")
        print()
    elif digital_joao == False:
        veredito = "INOCENTE"
        print("Phoenix Wright: A promotoria não pode sequer provar que meu cliente tocou na arma do crime! Não há digitais dele!")
        print()
    else:
        veredito = "CULPADO"
        print("Phoenix Wright: (Droga... As digitais estão na arma e a linha do tempo da promotoria é sólida... Não tenho objeções...)")
        print()
else: # A escolha foi confiar
    print("(Voz da Consciência de Phoenix: Eu confiei em João... mas agora, essa 'hora da modificação' não faz sentido para mim. Não tenho como usar essa evidência!)")
    print()
    print("Promotor Edgeworth: A lógica é simples. O acusado tinha o motivo, e suas digitais estão na arma. O caso está encerrado.")
    print("Phoenix Wright: OBJEÇÃO!")
    print()

    if digital_joao == False:
        veredito = "INOCENTE"
        print("Phoenix Wright: A promotoria não pode provar que meu cliente tocou na arma do crime! Não há digitais dele!")
        print()
    else:
        veredito = "CULPADO"
        print("Phoenix Wright: (Droga... As digitais estão na arma e a linha do tempo da promotoria é sólida... Estou sem argumentos!)")
        print()

# Juiz anuncia o verdito
print("Juiz: ...Compreendo. Após analisar todas as evidências e os argumentos...")
print(f"Juiz: O veredito para o caso de João Guilherme é: {veredito}!")
print()

if veredito == "INOCENTE":
    if escolha_inicial == "pressionar" and houve_contradicao == True and digital_elisson == True: # Elisson confessou
        print("Juiz: Que esta corte jamais esqueça o dia em que a verdade foi revelada contra todas as probabilidades.")
    
    print("A reputação do escritório Fey & Co. continua impecável.")
else:
    print("Edgeworth... Você ainda não venceu o debate final.")