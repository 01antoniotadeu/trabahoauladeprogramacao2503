# Definindo as variáveis
numeros = [10, 20, 30, 40]
frase = "Esta é uma frase de exemplo."
palavra = "python"

# Calculando a média aritmética dos números
media = sum(numeros) / len(numeros)
print("Média aritmética dos números:", media)

# Calculando o quadrado de um dos números
numero_quadrado = numeros[0] ** 2
print("Quadrado do primeiro número:", numero_quadrado)

# Calculando o dobro de um dos números
numero_dobro = numeros[1] * 2
print("O dobro do segundo número:", numero_dobro)

# Contando a quantidade de letras da palavra
quantidade_letras_palavra = len(palavra)
print("Quantidade de letras na palavra:", quantidade_letras_palavra)

# Contando a quantidade de espaços em branco na frase
quantidade_espacos_frase = frase.count(' ')
print("Quantidade de espaços em branco na frase:", quantidade_espacos_frase)

# Verificando se o primeiro número é maior que o segundo
primeiro_maior_que_segundo = numeros[0] > numeros[1]
print("O primeiro número é maior que o segundo?", primeiro_maior_que_segundo)

# Encontrando o maior número
maior_numero = max(numeros)
print("O maior número é:", maior_numero)