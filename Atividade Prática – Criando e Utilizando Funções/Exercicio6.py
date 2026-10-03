# Exercício 6 – Convertendo temperatura

# Crie uma função chamada converter_celsius_para_fahrenheit().

# A função deve receber uma temperatura em Celsius e retornar o valor convertido para Fahrenheit.

# Use a fórmula: fahrenheit = (celsius * 9 / 5) + 32

# Depois, armazene o resultado em uma variável e imprima a temperatura convertida.

# Requisitos:

# Receba a temperatura por parâmetro.
# Utilize type hint float.
# A função deve retornar um float.
# Utilize return.
# Adicione uma docstring explicando a função.

def converter_celsius_para_fahrenheit(celsius: float) -> float:
    """
    Recebe valor de temperatura em Celsius, converte e retorna valor em Fahrenheit.

    Args:
    celsius (float): Valor Celsius

    Returns (float): Valor em Fahrenheit
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

temperatura_celsius = 11
resultado = converter_celsius_para_fahrenheit(temperatura_celsius)

print(f"A temperatura é {resultado}º Fahrenheit")