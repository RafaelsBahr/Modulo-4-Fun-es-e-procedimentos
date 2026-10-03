# Exercício 7 – Calculando consumo médio

# Um veículo percorreu determinada distância utilizando uma quantidade de combustível.

# Crie uma função chamada calcular_consumo_medio() que receba:

# distância percorrida em quilômetros;
# quantidade de litros utilizados.

# A função deve retornar quantos quilômetros o veículo percorreu por litro.

# Exemplo: consumo = calcular_consumo_medio(420.0, 35.0)
# Resultado: 12.0

def calcular_consumo_medio(distancia_km: float, qtd_litros: float) -> float:
    """
    Calcula e retorna quantos quilômetros o veículo percorreu por litro
    
    Args:
        distancia_km (float): distância percorrida em quilômetros
        qtd_litros (float): quantidade de litros utilizados
    
    Returns (float): quantos quilômetros o veículo percorreu por litro
    """
    km_por_litro = distancia_km / qtd_litros
    return km_por_litro

# Depois, crie uma segunda função chamada exibir_consumo() que receba o resultado e exiba: Consumo médio: {resultado} km/l

def exibir_consumo(consumo: float) -> None:
    """
    Exibe resultado do consumo médio no modelo 'Consumo médio: {resultado} km/l'
    
    Args:
        consumo (float): quantos quilômetros o veículo percorreu por litro

    Returns: None    
    """
    print(f"Consumo médio: {consumo} km/l")
    return None

# Requisitos:
# As duas funções devem possuir type hints.
# calcular_consumo_medio() deve retornar float.
# exibir_consumo() deve retornar None.
# As duas funções devem possuir docstrings.
# O resultado da primeira função deve ser passado como argumento para a segunda.

distancia = 60
qtd_litros = 15

consumo = calcular_consumo_medio(distancia, qtd_litros)

exibir_consumo(consumo)