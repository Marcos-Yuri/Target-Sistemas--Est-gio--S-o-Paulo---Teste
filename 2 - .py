def pertence_fibonacci(num):
    if num < 0:
        return False

    a, b = 0, 1

    # Se o número é 0 ou 1, ele pertence à sequência

    if num == a or num == b:
        return True

    # Gera a sequência de Fibonacci até encontrar o número ou passar dele

    while b <= num:
        a, b = b, a + b
        if b == num:
            return True

    return False


def main():
    # Solicita ao usuário que insira um número

    try:
        numero = int(input("Informe um número: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        return

    # Verifica se o número pertence à sequência de Fibonacci

    if pertence_fibonacci(numero):
        print(f"{numero} pertence à sequência de Fibonacci.")
    else:
        print(f"{numero} não pertence à sequência de Fibonacci.")


if __name__ == "__main__":
    main()
