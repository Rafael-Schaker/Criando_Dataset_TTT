# abre o arquivo para leitura
with open('continue.txt', 'r') as arquivo:
    # cria uma lista vazia para armazenar as listas únicas
    listas_unicas = []
    count=0

    # percorre o arquivo linha por linha
    for linha in arquivo:
        # transforma a linha em uma lista de valores
        lista = linha.strip().split(',')

        # verifica se a lista já está na lista de listas únicas
        if lista not in listas_unicas:
            # adiciona a lista à lista de listas únicas
            listas_unicas.append(lista)
            count+=1
# abre o arquivo para escrita
with open('continue.txt', 'w') as arquivo:
    # escreve as listas únicas no arquivo
    for lista in listas_unicas:
        arquivo.write(','.join(lista) + '\n')
print(count)