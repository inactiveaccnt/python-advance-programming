import random

class Game:

    def __init__(self):
        self.com_move   = [ 'paper', 'rock', 'scissor' ]
        self.weapon     = { '1':'paper', '2':'rock', '3':'scissor' }
        self.score      = 0
        self.com_score  = 0
        self.round      = 0
        self.play()

    def display_weapons(self):
        print('1: %s'%self.weapon['1'])
        print('2: %s'%self.weapon['2'])
        print('3: %s'%self.weapon['3'])

    def play(self):
        while self.round < 10:
            self.display_weapons()
            self.i_choose = input('Choose your weapon: ')
            if self.i_choose == '1' or self.i_choose == '2' or self.i_choose == '3':
                self.ran_num = random.randint(0, 2)
                if self.com_move[self.ran_num] == self.weapon[self.i_choose]:
                    print("The match is draw")
                elif self.weapon[self.i_choose] == 'paper' and self.com_move[self.ran_num] == 'rock':
                    self.score += 1
                    print("(Your move is %s, Opponent's move %s)\nYou win!\n Your Score %s:\nOpponent Score %s: \n"
                    %(self.weapon[self.i_choose], self.com_move[self.ran_num], self.score, self.com_score))
                elif self.weapon[self.i_choose] == 'paper' and self.com_move[self.ran_num] == 'scissor':
                    self.com_score += 1
                    print("(Your move is %s, Opponent's move %s)\nYou lose!\nYour Score %s:\nOpponent Score %s: \n"
                    %(self.weapon[self.i_choose], self.com_move[self.ran_num], self.score, self.com_score))
                elif self.weapon[self.i_choose] == 'rock' and self.com_move[self.ran_num] == 'paper':
                    self.com_score += 1
                    print("(Your move is %s, Opponent's move %s)\nYou lose!\nYour Score %s:\nOpponent Score %s: \n"
                    %(self.weapon[self.i_choose], self.com_move[self.ran_num], self.score, self.com_score))
                elif self.weapon[self.i_choose] == 'rock' and self.com_move[self.ran_num] == 'scissor':
                    self.score += 1
                    print("(Your move is %s, Opponent's move %s)\nYou win!\nYour Score %s:\nOpponent Score %s: \n"
                    %(self.weapon[self.i_choose], self.com_move[self.ran_num], self.score, self.com_score))
                elif self.weapon[self.i_choose] == 'scissor' and self.com_move[self.ran_num] == 'rock':
                    self.com_score += 1
                    print("(Your move is %s, Opponent's move %s)\nYou lose!\nYour Score %s:\n Opponent Score %s: \n"
                    %(self.weapon[self.i_choose], self.com_move[self.ran_num], self.score, self.com_score))
                elif self.weapon[self.i_choose] == 'scissor' and self.com_move[self.ran_num] == 'paper':
                    self.score += 1
                    print("(Your move is %s, Opponent's move %s)\nYou win!\nYour Score %s:\n Opponent Score %s: \n"
                    %(self.weapon[self.i_choose], self.com_move[self.ran_num], self.score, self.com_score))
            else:
                print("invalid move")
            self.round += 1
