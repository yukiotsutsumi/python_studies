# exception = events detected during execution that interrupt the flow

try:
    numerator = int(input("Digite um número para fazer a divisão: "))
    denominador = int(input("Digite outro número para fazer a divisão: "))
    resultado = numerator / denominador
except ZeroDivisionError as e:
    print(e)
    print("Não pode dividir por zero!")
except ValueError as e:
    print(e)
    print("Digite apenas números!")
except Exception as e:
    print(e)
    print("Algo deu errado ):")
else:
    print(resultado)
finally:
    print("Isso sempre vai acontecer!")