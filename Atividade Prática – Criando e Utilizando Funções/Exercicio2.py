# Exercício 2 – Identificando um produto

# Crie uma função chamada exibir_produto() que receba:

# o nome de um produto;
# o preço do produto.

# A função deve exibir uma mensagem no seguinte formato: Produto: Teclado | Preço: R$ 150.00

# Depois, chame a função passando um produto e um preço como argumentos.

# Requisitos:
# Utilize parâmetros.
# Adicione type hints nos parâmetros.
# A função deve retornar None.

def exibir_produto(nome: str, preco: float) -> None:
    """Exibe uma mensagem no seguinte formato: Produto: Teclado | Preço: R$ 150.00

    Args:
        nome (str): nome do produto.
        preco (float): preço do produto.

    Returns:
        None
    """
    print(f"Produto: {nome} | Preço: R$ {preco:.2f}")
    return None


exibir_produto("Teclado", 149.99)