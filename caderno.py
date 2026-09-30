def calcular_total(preco: float, 
                   quantidade: int, 
                   desconto: float
            ) -> float:
    """
    Calcula o valor final de um item após aplicar o desconto.
    
    Args:
        preco: Preço unitário do produto.
        quantidade: Quantidade comprada.
        desconto: Percentual de desconto em formato decimal.
        
    Returns:
        Valor final da compra.
    """
    subtotal: float = preco * quantidade
    valor_desconto: float = subtotal * desconto
    total: float = subtotal - valor_desconto
    
    return total

help(calcular_total)