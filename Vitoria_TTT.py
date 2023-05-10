import random

# define o número de jogadas necessárias para vencer
jogadas_vencedoras = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

# define o número de jogadas que devem ser geradas
num_jogadas = 100

# cria um contador para controlar o número de jogadas geradas
jogadas_geradas = 0

# define um loop para gerar jogadas aleatórias até que o número necessário de jogadas seja gerado
while jogadas_geradas < num_jogadas:
    # cria um tabuleiro vazio
    tabuleiro = ['b'] * 9

    # define um loop para alternar entre jogadores até que um jogador ganhe ou empate
    while True:
        # escolhe qual jogador deve jogar
        jogadas_x = tabuleiro.count('x')
        jogadas_o = tabuleiro.count('o')
        if jogadas_x == jogadas_o:
            jogador = 'x'
        elif jogadas_x == jogadas_o + 1:
            jogador = 'o'
        else:
            # o número de jogadas de "x" e "o" é inválido
            break

        # escolhe uma jogada aleatória
        jogadas_disponiveis = [i for i, j in enumerate(tabuleiro) if j == 'b']
        if not jogadas_disponiveis:
            # o jogo terminou em empate
            break
        posicao = random.choice(jogadas_disponiveis)
        tabuleiro[posicao] = jogador

        # verifica se um jogador venceu
        for jogada in jogadas_vencedoras:
            if all([tabuleiro[i] == jogador for i in jogada]):
                print(','.join(tabuleiro) + ',positive')
                break
        else:
            continue
        break

    jogadas_geradas += 1
