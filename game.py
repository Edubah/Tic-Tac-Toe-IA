import time
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #Usamos esta lista para representar uma matrix 3x3
        self.current_winner = None #Deixar o jogador marcado

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: #Para pegar as rolagens
            print(' | ' + ' | '.join(row) + ' | ')

    @staticmethod
    def print_board_nums():
        #0 | 1 | 2 etc (Mostra qual número corresponde a qual caixa
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range (3)]
        for row in number_board:
            print(' | ' + ' | '.join(row) + ' | ')

    def avaliable_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     #['x', 'x', 'o'] ---> [('0', x), ('1', 'x'), ('2', 'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')
        # return len(self.avaliable_moves())


    def make_move(self, square, letter):
        #Se for um movimento válido, então faça o movimento
        #Então retorna para verdadeiro, se for válido, retorna falso.
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return  True
        return False


    def winner(self, square, letter):
        #Ganha quem fizer 3 X ou O no jogo, tenho que checar
        #Primeiro checar
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        #Checar as colunas
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #Checar as diagonais
        #Somente se os quadrados forem números uniformes
        #Estes são os únicos movimentos para ganhar nas diagonais
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #Diagonal da esquerda para a direita
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #Diagonal da direita para a esquerda
            if all([spot == letter for spot in diagonal2]):
                return True
        #Se todas as checagens forem falsas
        return False


def play(game, x_player, o_player, print_game=True):
    #Retornar o vencedor ou o game! Caso haja um empate.
    if print_game:
        game.print_board_nums()

    letter = 'X' #Letrar inicial
    # iterar(repetir) enquanto o jogo continua com quadrados vazios
    #não temos que nos preocupar com vencedores porque vamos sismplismente retornar para quebrar o loop

    while game.empty_squares():
        #Pegar os movimentos do playerr apropriado
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #Definir uma função para fazer o movimento!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' Fez um movimento para o quadrado {square}')
                game.print_board()
                print('') #Apenas uma linha vazia

            if game.current_winner:
                if print_game:
                    print(letter + ' Ganhou!')
                return letter

            #Depois de fazermos nosso movimento, precisamos alternar as letras
            letter = 'O' if letter == 'X' else 'X'

        #Pequena pausa para que possamos ler
        if print_game:
            time.sleep(0.8)

    if print_game:
            print('É um empate')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

# if __name__ == '__main__':
#     x_wins = 0
#     o_wins = 0
#     ties = 0
#     for _ in range(30):
#         x_player = GeniusComputerPlayer('X')
#         o_player = GeniusComputerPlayer('O')
#         t = TicTacToe()
#         result = play(t, x_player, o_player, print_game=False)
#         if result == 'X':
#             x_wins += 1
#         elif result == 'O':
#             o_wins += 1
#         else:
#             ties +=1
#     print(f'Depois de {_} interações, vimos que o jogador X ganhou {x_wins} vezes, o jogador O ganhou {o_wins} vezes e tivemos {ties} empates!')