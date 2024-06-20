# Abrir o arquivo e ler o conteúdo
with open('lista.txt', 'r', encoding='utf-8') as file:
    linhas = file.readlines()

# Remover quebras de linha e espaços extras
linhas = [linha.strip() for linha in linhas]

# Imprimir as linhas originais e seus comprimentos para depuração
print("Linhas originais e comprimentos:")
for linha in linhas:
    print(f"'{linha}' -> {len(linha)} caracteres")

# Ordenar a lista pela quantidade de caracteres no texto
linhas_ordenadas = sorted(linhas, key=len)

# Imprimir as linhas ordenadas e seus comprimentos para depuração
print("\nLinhas ordenadas e comprimentos:")
for linha in linhas_ordenadas:
    print(f"'{linha}' -> {len(linha)} caracteres")

# Escrever o resultado ordenado em um novo arquivo
with open('lista_ordenada.txt', 'w', encoding='utf-8') as file:
    for linha in linhas_ordenadas:
        file.write(linha + '\n')

print("\nLista ordenada salva em 'lista_ordenada.txt'")
