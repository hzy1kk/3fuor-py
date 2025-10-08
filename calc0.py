print("-----Calculadora-----")
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))

soma = n1 + n2
print(f"A soma é: {soma:.2f}")


subtracao = n1 - n2
print(f"A subtração é: {subtracao:.2f}")

resultado = n1 * n2
print(f"A multiplicação é: {resultado:.2f}")

if n2 != 0:
	resultado = n1 / n2
	print(f"A divisão é: {resultado:.2f}")
else:
	print("Não é possível dividir por zero.")
