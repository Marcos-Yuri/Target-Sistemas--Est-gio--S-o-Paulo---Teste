def inverter_string(texto):
    """Inverte os caracteres de uma string.

    Args:
      texto: A string a ser invertida.

    Returns:
      A string invertida.
    """

    texto_invertido = ''
    for i in range(len(texto) - 1, -1, -1):
        texto_invertido += texto[i]
    return texto_invertido

# Entrada do usuário


texto = input("Digite a string que você deseja inverter: ")


# Inverte a string

texto_invertido = inverter_string(texto)


# Imprime os resultados

print(f"Texto original: {texto}")
print(f"Texto invertido: {texto_invertido}")
