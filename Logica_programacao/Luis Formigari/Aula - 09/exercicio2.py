# Exercicio 2:
# Escreva um programa que solicite ao usuário uma lista de palavras e
# conta quantas vezes cada palavra aparece na lista. O programa deve
# tratar os seguintes erros:

# - ValueError: se o usuario digitar um valor que não seja uma string

quantPalavras = int(input("Quantas palavras você deseja digitar?    "))
listapalavra = []
valorlista = 0
lastpalavra = ""
palavranum = 0

for i in range(quantPalavras):
    stri = str(input("Digite a palavra...  "))
    sim = listapalavra.append(stri)
    teste = str(listapalavra)
    if lastpalavra == stri:
        palavranum += 1

        
    lastpalavra = stri
  
sim2 = str(listapalavra)
valorlista = sim2.count(listapalavra[0])
if lastpalavra == stri:
    palavranum += 1
print(palavranum)

if quantPalavras >= 1:
    print(f"A sua primeira palavra é {listapalavra[0]} e ela é repetida: {sim2.count(listapalavra[0])}")
if quantPalavras >= 2:
    print(f"A sua segunda palavra é {listapalavra[palavranum -1]} e ela é repetida: {sim2.count(listapalavra[palavranum -1])}")
if quantPalavras >= 3:
    print(f"A sua terceira palavra é {listapalavra[palavranum+ 1]} e ela é repetida: {sim2.count(listapalavra[palavranum +1])}")

    
    
    



