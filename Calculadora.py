input("Aperta a tecla Enter para iniciar.\n")

class Calculadora:
    def __init__(self):
        return

    def menu(self):
        return input("Selecione a operação desejada.\n \n1. Adição \n2. Subtração \n3. Multiplicação \n4. Divisão\n")

    def addition(self):
        num1 = float(input("\nDigite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        return num1 + num2

    def subtraction(self):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        return num1 - num2

    def multiplication(self):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        return num1 * num2

    def division(self):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num1 == 0 or num2 == 0:

            return 0

        else:

            return num1 / num2

calculadora = Calculadora()

while True:
    choice = calculadora.menu()
    if choice in {"1", "2", "3", "4"}:
        if choice == "1":
            print(f"\nResultado: {calculadora.addition()}")
            break

        elif choice == "2":
            print(f"Resultado: {calculadora.subtraction()}")
            break

        elif choice == "3":
            print(f"Resultado: {calculadora.multiplication()}")
            break

        elif choice == "4":
            print(f"Resultado: {calculadora.division()}")
            break

    elif choice == "":
        continue

    else:
        print("\nOpção inválida.")
