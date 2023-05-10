import itertools
import random

num_cases = 100000
winning_cases = []

for i in range(num_cases):
    # Sorteia uma posição aleatória para cada valor de 'x' e 'o'
    random_positions = random.sample(range(9), 2)
    x_pos, o_pos = random_positions[0], random_positions[1]
    game = [''] * 9
    game[x_pos] = 'x'
    game[o_pos] = 'o'
    # Preenche as posições restantes com 'x' ou 'o' de forma aleatória
    for j in range(9):
        if j not in random_positions:
            game[j] = random.choice(['x', 'o'])
    # Verifica se há um vencedor
    rows = [game[i:i+3] for i in range(0, 9, 3)]
    cols = [game[i::3] for i in range(3)]
    diags = [[game[0], game[4], game[8]], [game[2], game[4], game[6]]]
    if any(all(cell == 'x' for cell in line) or all(cell == 'o' for cell in line)
           for line in rows + cols + diags):
        continue
    # Verifica se o jogo está empatado
    if all(cell != '' for cell in game):
        winning_cases.append(','.join(game)+ ',draw')
                        
    # Sai do loop se já tivermos gerado o número necessário de casos
    if len(winning_cases) == num_cases:
        break

# Escreve a lista de casos em um arquivo de texto
with open('empate.txt', 'w') as f:
    f.write('\n'.join(winning_cases))
