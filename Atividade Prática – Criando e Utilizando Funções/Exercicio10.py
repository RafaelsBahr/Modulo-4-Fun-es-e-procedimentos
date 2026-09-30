# xercício 10 – Sistema de Aprovação de Empréstimo

# Você está desenvolvendo uma parte de um sistema bancário responsável por analisar solicitações de empréstimo.

# O programa deverá utilizar várias funções, e cada uma terá uma responsabilidade específica.


# 1. Calcular comprometimento da renda
# Crie uma função chamada calcular_comprometimento_renda() que receba:

# renda mensal;
# valor da parcela do empréstimo.
# Ela deve calcular qual percentual da renda mensal seria comprometido pela parcela.

# Use:

# percentual = (parcela / renda) * 100


# A função deve retornar esse percentual.



# 2. Analisar o empréstimo
# Crie uma segunda função chamada analisar_emprestimo() que receba:

# renda mensal;
# valor solicitado;
# percentual de comprometimento da renda.
# A função deve retornar uma das seguintes classificações:

# "Aprovado"
# "Análise manual"
# "Recusado"


# Utilize estas regras:

# Se o comprometimento da renda for maior que 40%, retorne "Recusado".
# Se o comprometimento for menor ou igual a 40%, mas o valor solicitado for maior que 5 vezes a renda mensal, retorne "Análise manual".
# Caso contrário, retorne "Aprovado".


# 3. Calcular o total do pagamento
# Crie uma terceira função chamada calcular_total_pagamento() que receba:

# valor da parcela;
# quantidade de parcelas.
# Ela deve retornar o valor total que será pago ao final do empréstimo.

# Exemplo:

# Parcela: R$ 850.00
# Quantidade: 24

# Total pago: R$ 20400.00
# 4. Exibir o resultado final
# Por fim, crie uma função chamada exibir_resultado() que receba:

# valor solicitado;
# percentual de comprometimento;
# total que será pago;
# resultado da análise.
# Ela deve apenas exibir um resumo como:

# --- Análise do empréstimo ---

# Valor solicitado: R$ 15000.00
# Comprometimento da renda: 28.3%
# Total a pagar: R$ 20400.00

# Resultado: Aprovado


# Essa função não deve retornar nenhuma informação.



# Requisitos
# Todas as funções devem possuir type hints.
# Todas devem possuir docstrings.
# calcular_comprometimento_renda() deve retornar float.
# analisar_emprestimo() deve retornar str.
# calcular_total_pagamento() deve retornar float.
# exibir_resultado() deve retornar None.
# Os cálculos devem acontecer dentro das funções responsáveis por eles.
# Não repita cálculos fora das funções.
# Os valores retornados pelas funções devem ser armazenados em variáveis e reutilizados nas próximas etapas.
# A função exibir_resultado() deve apenas receber os resultados já calculados e exibi-los.
# Não utilize *args, **kwargs, parâmetros com valores padrão ou outros recursos ainda não vistos nesta aula.

# Fluxo esperado

# dados do empréstimo
# ↓
# calcular comprometimento da renda
# ↓
# analisar empréstimo
# ↓
# calcular total do pagamento
# ↓
# exibir resultado final


# O objetivo é organizar um problema maior em funções menores, fazendo com que o retorno de uma etapa seja utilizado pelas próximas.