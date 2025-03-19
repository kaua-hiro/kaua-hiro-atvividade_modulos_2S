from modulos.n_primos import verifica_primo
from modulos.soma_lista import somar_lista_recursiva
from modulos.registrador import registrar_informacoes

numero = int(input("Digite um número para verificar se é primo: "))
print(f"{numero} é primo? {verifica_primo(numero)}")

lista_numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))
print(f"Soma da lista: {somar_lista_recursiva(lista_numeros)}")

args = input("Digite valores separados por espaço para argumentos posicionais (*args): ").split()
kwargs = {}
while True:
    chave = input("Digite o nome do argumento nomeado (ou pressione Enter para finalizar): ")
    if not chave:
        break
    valor = input(f"Digite o valor para {chave}: ")
    kwargs[chave] = valor

registrar_informacoes(*args, **kwargs)
