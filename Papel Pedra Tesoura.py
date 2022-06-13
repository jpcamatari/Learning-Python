import random

print("========================================")
print("Bem Vindo ao Jogo Papel, Pedra, Tesoura")
print("========================================")
print("\n")
print("Escolha seu lance:")
numero = int(input("0 - Papel || 1 - Pedra || 2 - Tesoura:"))
while ((numero) < 0) or ((numero) > 3):
    print("O numero não é valido.")
    numero = int(input("0 - Papel || 1 - Pedra || 2 - Tesoura:"))


dict_lance = {0: "Papel", 1: "Pedra", 2: "Tesoura"}
computador = random.randint(0, 3)
print(f"Seu Lance:{dict_lance.get(numero)}")
print(f"Lance do Computador:{dict_lance.get(computador)}")


if numero == 0:
    if computador == 0:
        print("O Jogo Empatou!")
    elif computador == 1:
        print("Você Ganhou!")
    else:
        print("O Computador Ganhou!")
elif numero == 1:
    if computador == 0:
        print("O Computador Ganhou!")
    elif computador == 1:
        print("O Jogo Empatou!")
    else:
        print("Você Ganhou!")
elif numero == 2:
    if computador == 0:
        print("Você Ganhou!")
    elif computador == 1:
        print("Você Perdeu!")
    else:
        print("O Jogo Empatou!")
else:
    print("Reinicie o Jogo.")
