"""
Laboratório de Computação Gráfica

Lempel-Ziv Data Compression Algorithm

Mateus Rocha de Carvalho Alves

"""


# 'empty()' verifica a existência do arquivo para compressão.
def empty():
    c, doc = 0, open('exist.txt', 'r')  # 'exist.txt' é aberto para leitura.

    for line in doc:
        if line != '\n':
            c += 1
    doc.close()

    return c == 1


# 'count()' realiza e contagem de caracteres iguais em uma string.
def count(lenght, word):
    c = 0

    for character in word:
        if character == word[lenght - 1]:
            c += 1

    return c


if __name__ == '__main__':
    name = ''

    if empty():
        print('\nNão existe nenhum arquivo contendo dados para compressão.')

        name = input('\nPara criar um novo arquivo, digite um nome à sua escolha e pressione ENTER.\n> ')

        File = open(str(name + '.txt'), 'x')
        print('\nO arquivo', File.name, 'foi criado com sucesso!')
        File.close()

        File = open('exist.txt', 'a')  # 'exist.txt' é aberto para adição, na próxima linha, de um marcador de
        # existência para o arquivo principal.
        File.write(str('\n' + name))
        File.close()

    File = open('exist.txt', 'r')  # 'exist.txt' é aberto para leitura.
    name = File.readlines()  # Obtenção do nome do arquivo principal.
    File.close()

    data = input('\nEntre com uma cadeia de caracteres qualquer.\n> ')

    File = open(str(name[1] + '.txt'), 'w')  # O arquivo principal é aberto para escrita.
    File.write(data)
    File.close()

    strings = sorted(list(set(data)))

    dictionary, v = {}, 1  # Dicionário, Valor

    for string in strings:
        dictionary[str(string)] = v
        v += 1

    i, j, = 0, 0

    # [L.73, ... 104] Lempel-Ziv Data Compression

    while j < len(data):
        if data[i: j + 1] in strings:
            j += 1
        else:
            dictionary[str(data[i: j + 1])] = v
            strings.append(data[i: j + 1])
            i = j + 1
            j += 1
            v += 1

    print("\nDicionário =", dictionary)
    print("\nStrings =", strings)

    alfanumeric = sorted(list(set(data)))  # Representação Alfanumérica

    for string in strings[len(alfanumeric):]:
        if count(len(string), string) != len(string):
            alfanumeric.append(str(dictionary[string[:len(string) - 1]]) + string[len(string) - 1])
        else:
            alfanumeric.append(dictionary[string])

    print("\nRepresentação Alfanumérica =", alfanumeric)

    File = open('compressed.txt', 'w')  # 'compressed.txt' é criado e aberto para escrita.

    compressed = ''

    for string in alfanumeric:
        compressed += str(string)

    File.write(compressed)
    File.close()
