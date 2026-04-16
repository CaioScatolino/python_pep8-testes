try:
    numero = int(input("Digite um número: "))
    print(f"Você digitou: {numero}")

except ValueError:
    print("Valor digitado não é um número inteiro")

except FileNotFoundError:
    print("O arquivo não existe")

except Exception:
    print(f"Deu erro aqui")

