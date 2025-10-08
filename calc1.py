print("-----Calculadora-----")
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))

print("Escolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
op = input("Digite o número da operação desejada: ")

if op == "1" or op == "+":
    resultado = n1 + n2
    print(f"A soma é: {resultado:.2f}")
elif op == "2" or op == "-":
    resultado = n1 - n2
    print(f"A subtração é: {resultado:.2f}")
elif op == "3" or op == "*":
    resultado = n1 * n2
    print(f"A multiplicação é: {resultado:.2f}")
elif op == "4" or op == "/":
    if n2 == 0:
        print("Divisão por zero não é permitida.")
    else:
        resultado = n1 / n2
        print(f"A divisão é: {resultado:.2f}")
else:
    print("Operação inválida.")
