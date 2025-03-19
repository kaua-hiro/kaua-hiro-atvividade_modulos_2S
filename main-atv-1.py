from modulos.contador_de_palavras import contar_palavra

texto = input("Digite o texto para análise: ")
resultado = contar_palavra(texto)

print("Frequência das palavras no texto:")
for palavra, contagem in resultado.items():
    print(f"{palavra}: {contagem}")