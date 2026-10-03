# Exercício 8 – Verificando uma meta de vendas

# Crie uma função chamada calcular_percentual_meta() que receba:
# valor da meta;
# valor vendido.

def calcular_percentual_meta(meta: (float), vendido: (float)) -> float:
    """
    Calcula e retorna o percentual da meta que foi atingido

    Args:
        meta (float): valor da meta
        vendido (float): valor vendido
        
    Returns: percentual da meta que foi atingido
    """
    percentual_meta_atingida = (vendido / meta) * 100
    return percentual_meta_atingida

# A função deve calcular e retornar o percentual da meta que foi atingido.

# Exemplo: percentual = calcular_percentual_meta(10000.0, 7500.0)
# Resultado: 75.0

# Depois, crie uma função chamada exibir_status_meta() que receba esse percentual.

def exibir_status_meta(percentual_meta: (float)) -> None:
    """
    Recebe percentual da meta atingido e exibe mensagem de meta atingida ou não
    
    Arg:
        percentual_meta (float): percentual de meta atingido
        
    Returns: none
    """
    if percentual_meta < 100:
        print("Meta ainda não atingida.")
    else:
        print("Meta atingida!")

# Ela deve exibir: Meta atingida!
# caso o percentual seja maior ou igual a 100.

# Caso contrário, deve exibir: Meta ainda não atingida.

meta = 149000
vendido = 100000
percentual_batido = calcular_percentual_meta(meta, vendido)
exibir_status_meta(percentual_batido)


# Requisitos:
# Utilize type hints.
# calcular_percentual_meta() deve retornar float.
# exibir_status_meta() deve retornar None.
# Utilize o valor retornado por uma função como argumento da outra.
# Adicione docstrings nas duas funções.
# Não repita o cálculo do percentual fora da função.