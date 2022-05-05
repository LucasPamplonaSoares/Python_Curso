# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

# A) Quantos espaços em branco existem na frase.
# B) Quantas vezes aparecem as vogais a, e, i, o, u.

frase = str(input("Digite um frase: "))
vogais = 0
espacos = 0
for letra in frase:
    if letra == " ":
        espacos += 1
    elif letra in "aeiou":
        vogais += 1

print("A frase tem %d vogais e %d espaços. "% (vogais, espacos))        