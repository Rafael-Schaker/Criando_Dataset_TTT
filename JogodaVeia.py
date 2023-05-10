import random

def generate_tic_tac_toe_games(num_games, num_blank):
    games = []

    for _ in range(num_games):
        # Inicializando o tabuleiro com espaços em branco
        board = ['b']*9

        # Preenchendo o tabuleiro com 'x' e 'o'
        for i in range(9 - num_blank):
            # Escolhendo uma posição aleatória para a próxima jogada
            pos = random.choice([i for i, x in enumerate(board) if x == 'b'])
            # Alternando entre 'x' e 'o'
            board[pos] = 'x' if i % 2 == 0 else 'o'

        # Verificando se o jogo está em andamento
        lines = [
            board[0:3], board[3:6], board[6:9],  # linhas
            board[0:7:3], board[1:8:3], board[2:9:3],  # colunas
            board[0:9:4], board[2:7:2]  # diagonais
        ]
        if any(line == ['x', 'x', 'x'] for line in lines) or any(line == ['o', 'o', 'o'] for line in lines):
            # Se alguém ganhou, descartamos o jogo e tentamos novamente
            continue
        else:
            # Se ninguém ganhou, adicionamos o jogo à lista
            if board not in games:
                games.append(','.join(board + ['continue']))

    return games

num_games = 200
num_blank = 1
games = generate_tic_tac_toe_games(num_games, num_blank)
#for game in games:
#    print(game)
lista_anterior=[]
with open('Continue.txt', 'r') as arquivo:
    # percorre o arquivo linha por linha
    for linha in arquivo:
        lista_anterior.append(linha)


# abre o arquivo para escrita
with open('Continue.txt', 'w') as arquivo:
    # escreve as listas únicas no arquivo
    for game in games:
        arquivo.write(game + '\n')
    for linha in lista_anterior:
        arquivo.write(linha)