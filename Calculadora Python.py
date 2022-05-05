from tkinter import N


print("***********Python Calculator*************\n\n"
"Selecione o numero da operação desejada:\n\n"

"1 - Soma\n"
"2 - Subtração\n"
"3 - Multiplicação\n"
"4 - Divisão\n"
)

opcao = float(input("Digite Sua Opção: "))
num1 = float(input("Digite o primeiro Numero: "))
num2 = float(input("Digite o segundo Numero: "))

if opcao == 1:
  print(num1 + num2)
elif opcao == 2:
  print(num1 - num2)
elif opcao == 3:
  print(num1 * num2)
elif opcao == 4:
  print(num1 / num2)
