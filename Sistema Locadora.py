print("===========")
print("Bem vindo a Locadora de Carros")
print("===========")


carros = [
    ("Hyundai HB20", 95),
    ("Fiat Mobi", 70),
    ("Volkswagen Polo", 120),
    ("Jeep Renegade", 150),
    ("Toyota Hilux", 250),
]

alugados = []


def mostrar_lista_carros(lista_carros):
    for i, car in enumerate(lista_carros):
        print("[{}] {} | Valor: R${},00".format(i, car[0], car[1]))


while True:
    print("Carros Disponiveis - 1 | Alugar Carro - 2 | Devolver Carro - 3")
    op = int(input())
    while op not in [1, 2, 3]:
        op = int(input("Opção invalida, tente novamente:"))

    if op == 1:
        print(mostrar_lista_carros(carros))

    elif op == 3:
        print(mostrar_lista_carros(alugados))
        print("Escolha um Carro para Devolver:")
        devolver_carro = int(input())
        carros.append(alugados.pop(devolver_carro))

    elif op == 2:
        print(mostrar_lista_carros(carros))
        alugar_carro = int(input("Escolha um Carro para alugar:"))
        while alugar_carro not in [0, 1, 2, 3, 4]:
            alugar_carro = int(input("Opção Invalida, tente novamente:"))
        escolha = carros[alugar_carro]
        dias = int(input("Deseja alugar por quantos dias:"))
        valor_aluguel = escolha[1]*dias
        print("Parabens, você alugou {} por {} dias com valor total de R${},00".format(
            escolha[0], dias, valor_aluguel))
        alugados.append(escolha)
        carros.remove(escolha)
    print("Digite 1 para SAIR")
    if input() == 1:
        break
