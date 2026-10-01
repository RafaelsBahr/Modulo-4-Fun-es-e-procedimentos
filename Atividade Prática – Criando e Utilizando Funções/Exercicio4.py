# Exercício 4 – Calculando a média de avaliações

# Uma plataforma armazena três avaliações dadas por usuários para um produto.

# Crie uma função chamada calcular_media_avaliacoes() que receba três notas e retorne a média entre elas.

# Depois, utilize o resultado retornado pela função para exibir a média das avaliações

# Requisitos:

# Utilize parâmetros e argumentos.
# Adicione type hints.
# Utilize return.
# Adicione uma docstring explicando o que a função recebe e o que retorna.
# Guarde o resultado da função em uma variável antes de exibi-lo.

def calcular_media_avaliacoes(valor1: int, valor2: int, valor3: int) -> float:
    """
    Calcula e retorna a media de três valores.

    Args:
    valor1 (int): primeiro valor.
    valor2 (int): segundo valor.
    valor3 (int): terceiro valor.

    Returns (float):
        Média dos 3 valores.
    """
    media = (valor1 + valor2 + valor3) / 3

    return media

media = calcular_media_avaliacoes(1, 3, 4)

print(f"Média das avaliações: {media:.2f}")