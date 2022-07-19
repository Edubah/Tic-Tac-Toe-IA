import math
import random

class Player: #Classe do jogador

    def __init__(self, letter):
        #Letra x ou o
        self.letter = letter

    #Queremos todos os jogadores tenham os seus movimentos
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player): #Classe do computador

    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, game):

        # Pega um SOPT randômico e válido para outro movimento
        square = random.choice(game.avaliable_moves())
        return square


class HumanPlayer(Player): #Classe do jogador humano

    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, game):

        valid_square = False
        val = None

        while not valid_square:
            square = input(self.letter + '\'s turno. Entre como o movimento (0 - 8): ')
            # Vamos checar se este é o valor correto
            # E ver se é inteiro, se não for, então ele diz que é invalido
            # Se o spot não estiver disponível no quadro, falamos que ele é invalido
            try:
                val = int(square)
                if val not in game.avaliable_moves():
                    raise ValueError
                valid_square = True #Se for um sucesso é uma BOA!
            except ValueError:
                print('Quadrado inválido, tente novamente!')
        return val

class GeniusComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.avaliable_moves()) == 9:
            square = random.choice(game.avaliable_moves()) #Escolhe um randomicamente
        else:
            #Escolhe o quadrado baseado no algoritmo de mínimo e máximo
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter #Jogador, no caso sou eu!
        other_player = 'O' if player == 'X' else 'X' #Este é o outro jogador

        #Primeiro, checar se o movimento previsto é o vencedor
        #Este é o caso base!
        if state.current_winner == other_player:
            #Retornará a posição e a pontuação porque preciso precisamos manter o controle da pontuação
            #Para que o algoritmo minimax funcione
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)

                    }
        elif not state.empty_squares(): #Para não ter quadrados vazios
            return {'position': None, 'score': 0}


        if player == max_player:
            best = {'position': None, 'score': -math.inf} #Cada pontuação deve maximizar!!

        else:
            best = {'position': None, 'score': math.inf} #Cada pontuação deve minimizar!!

        for possible_move in state.avaliable_moves():
            # 1 - fazer um movimento, try o ponto certo
            state.make_move(possible_move, player)

            # 2 - recursar para usar o minimax para simular o jogo depois de fazer o movimento
            sim_score = self.minimax(state, other_player) #Agora, os jogadores alternam

            # 3 - Desfazer o movimento
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # 4 - Atualizar os dicionários se necessário
            if player == max_player: #Aqui tento maximizar o max_player
                if sim_score['score'] > best['score']:
                    best = sim_score #Substitui o melhor
            else: #Minimizar o player
                if sim_score['score'] < best['score']:
                    best = sim_score #Substitui o melhor

        return best