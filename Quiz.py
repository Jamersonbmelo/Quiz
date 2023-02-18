################################INICIANDO O PROGRAMA DE QUIZ################################
print("Sejam muito bem vindo ao QUIZ!")
answer_user = input("Quer começar? (S/N) ")
if answer_user != "S":
    quit()

pontuacao = 0

print("Começando...")
print()
################################PRIMEIRA PERGUNTA DO QUIZ################################
print("Qual clube é o maior campeão nacional do Brasil? \n (A) Palmeiras \n (B) Cruzeiro \n (C) São Paulo \n (D) Flamengo \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print()
    print("Certa resposta!")
    pontuacao = pontuacao + 1
    print()
else:
    print("Resposta errada!")
################################SEGUNDA PERGUNTA DO QUIZ################################
print("Quantos titulos brasileiro tem o Palmeiras? \n (A) Oito taças \n (B) 9 taças \n (C) 10 taças \n (D) 11 taças \n")
answer_2 = input("Resposta: ")

if answer_2 =="D":
    print()
    print("Certa resposta!")
    pontuacao = pontuacao + 1
    print()
else:
    print("Resposta errada!")
################################TERCEIRA PERGUNTA DO QUIZ################################
print("A História da Sociedade Esportiva Palmeiras começa no dia 26 de agosto de 1914, quando o clube foi fundado por imigrantes? \n (A) Ingleses \n (B) Portugueses \n (C) Espanhois \n (D) Italianos \n")
answer_3 = input("Resposta: ")

if answer_3 =="D":
    print()
    print("Certa resposta!")
    pontuacao = pontuacao + 1
    print()
else:
    print("Resposta errada!")
########################################################################################

print(f"Quiz acabou... Pontuação: {pontuacao}/3")