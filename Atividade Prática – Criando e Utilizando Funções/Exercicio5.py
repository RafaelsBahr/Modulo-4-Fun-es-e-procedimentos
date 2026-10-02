# Exercício 5 – Processando um pedido

# Você precisa criar duas funções para representar uma pequena parte de um sistema de pedidos.

# A primeira função deve se chamar: calcular_valor_final()

# Ela deve receber:

# preço unitário;
# quantidade;
# desconto em formato decimal.
# Por exemplo, 0.10 representa 10% de desconto.

# A função deve calcular e retornar o valor final do pedido após o desconto.
def calcular_valor_final(preco_unitario: float, qtd: float, desconto: float) -> float:
    """
    Calcula e retorna o valor final do pedido após o desconto.

    Args:
        preco_unitario (float): preço unitário.
        qtd (float): quantidade.
        desconto (float): desconto em formato decimal. Por exemplo 0.10 representa 10%

    Returns (float):
        Valor final com desconto
    """
    valor_final = preco_unitario * qtd * (1 - desconto)

    return valor_final


# Depois, crie uma segunda função chamada: exibir_resumo_pedido()

# Ela deve receber:
# número do pedido;
# valor final.

# E exibir uma mensagem como: Pedido #1025 finalizado. Total: R$ 270.00
def exibir_resumo_pedido(n_pedido: int, valor_final: float) -> None:
    """
    Exibe mensagem com número do pedido e valor final, exemplo: Pedido #1025 finalizado. Total: R$ 270.00

    Args:
        n_pedido (int): número do pedido:
        valor_final (float): valor final

    Returns: None
    """
    print(f"Pedido #{n_pedido} finalizado. Total: R$ {valor_final:.2f}")

    return None

# Requisitos:
# As duas funções devem possuir type hints.
# calcular_valor_final() deve retornar um float.
# exibir_resumo_pedido() deve retornar None.
# As duas funções devem possuir docstrings.
# O valor retornado por calcular_valor_final() deve ser passado como argumento para exibir_resumo_pedido().
# Não faça o cálculo diretamente fora da função.

valor = calcular_valor_final(150.0, 2, 0.10)
exibir_resumo_pedido(1025, valor)