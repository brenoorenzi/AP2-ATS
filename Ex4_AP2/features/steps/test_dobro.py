from behave import given, when, then

# 1. Defina a função (como o exercício pede)
def calcular_dobro(numero):
    return numero * 2

# 2. Copie o código gerado/crie os steps
@given('que o número de entrada é {numero:d}')
def step_impl_entrada(context, numero):
    # Guardamos o número no contexto para usar no próximo passo
    context.numero_entrada = numero

@when('a função calcular_dobro for executada')
def step_impl_execucao(context):
    # Executamos a função que definimos ali em cima
    context.resultado = calcular_dobro(context.numero_entrada)

@then('o resultado retornado deverá ser {valor_esperado:d}')
def step_impl_verificacao(context, valor_esperado):
    # Comparamos se a saída da nossa função bate com o que o Feature espera
    assert context.resultado == valor_esperado, f"Falhou! Esperava {valor_esperado}, mas a função retornou {context.resultado}"