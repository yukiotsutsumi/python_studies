# Aceitar o texto de até 30 caracteres
texto = input("Digite um texto de até 30 caracteres: ")

# Verificar se o texto tem no máximo 30 caracteres
if len(texto) <= 30:
    # 1. Mostrar o texto com os 30 caracteres de trás pra frente
    reverso = texto[::-1]
    print("Texto de trás pra frente:", reverso)

    # 2. Mostrar só o texto digitado
    print("Texto digitado:", texto)

    # 3. Mostrar só as consoantes
    consoantes = ''.join([letra for letra in texto if letra.isalpha() and letra.lower() not in 'aeiou'])
    print("Consoantes:", consoantes)

    # 4. Mostrar só as vogais
    vogais = ''.join([letra for letra in texto if letra.lower() in 'aeiou'])
    print("Vogais:", vogais)
else:
    print("O texto excede 30 caracteres.")
