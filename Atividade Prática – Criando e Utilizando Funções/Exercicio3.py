# Exercício 3 – Calculando o valor de uma compra

# Crie uma função chamada calcular_total() que receba:

# o preço de um produto;
# a quantidade comprada.

# A função deve calcular e retornar o valor total da compra.

# Exemplo:

# total = calcular_total(50.0, 3)
# print(total)

# Resultado esperado: 150.0

# Requisitos:
# preco deve possuir type hint float.
# quantidade deve possuir type hint int.
# A função deve indicar que retorna um float.
# Utilize return para devolver o resultado.

def calcular_total(preco_produto: float, qtd_comprada: int) -> float:
    """
    Calcula e retorna o valor total da compra.
    
    Args:
        preco_produto (float): preço do produto.
        qtd_comprada (int): quantidade comprada.
        
    Returns (float):
        valor total da compra.
    """
    total = preco_produto * qtd_comprada

    return total