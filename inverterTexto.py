texto = input("Digite o texto a ser invertido: ")
reverso = ""
for a in range(len(texto), 0, -1):
	reverso += texto[a-1]

print(reverso)