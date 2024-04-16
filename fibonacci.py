num = int(input("Digite o número que deseja verificar se pertence à sequência de Fibonacci: "))

sequencia = 1
anterior = 1
while (sequencia < num):
	sequencia += anterior
	anterior = sequencia - anterior
	

if num == 0 or sequencia == num:
	print("O número pertence à sequência de Fibonacci")

else:
	print("O número não pertence à sequência de Fibonacci")