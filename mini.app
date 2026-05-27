print("_- MINI APP -_")
print("  ")
print("1 - descobrir idade no próximo ano")
print("2 - contar vogais")
print("3 - descobrir a saída do cálculo")

oi = input("o que você quer jogar? ")

if oi == "1":
    name = input("Qual o seu nome? ")
    age = int(input("Quantos anos você tem? "))

    next_year_age = int(age) + int(1)

    print("Olá,", name + "!", "você terá", next_year_age, "anos em um ano!")

elif oi == "2":
    frase = input("digite uma frase/palavra: ")

    vogais = 0

    for letra in frase:
        if letra == "a":
            vogais += 1
        if letra == "e":
            vogais += 1
        if letra == "i":
            vogais += 1
        if letra == "o":
            vogais += 1
        if letra == "u":
            vogais += 1

    print("número de vogais:", vogais)

elif oi == "3":
    x = 5
    x = x + 2
    x *= 3

    print("resultado:", x)

else:
    print("opção inválida, tenta denovo")
