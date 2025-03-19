from modulos.soma_notas import calcular_soma
from modulos.media_alunos import calcular_media

aluno = input("Digite o nome do aluno: ")
notas = list(map(float, input("Digite as notas separadas por espaço: ").split()))
soma = calcular_soma(notas)
media = calcular_media(soma, len(notas))
print(f"A média das notas do aluno {aluno} é: {media:.2f}")
