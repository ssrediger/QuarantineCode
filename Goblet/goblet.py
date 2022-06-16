import math
from tracemalloc import stop

# just a structure for easy setup. This defines unique attributes of different pieces
class gamePiece():
    def __init__(self,color,size):
        self.color = color
        self.size = size

#define a tile, effectively a GameBoard subclass
class Tile():
    def __init__(self, shells = []):
        self.shells = shells

    def update_shell(self,piece):
        if len(self.shells) == 0:
            self.shells = [piece]
            return True
        elif int(piece.size) > int(self.shells[0].size):
            self.shells.insert(0,piece)
            return True
        else:
            return False 


#the gameboard, essentially the structure of the entire game
class GameBoard():
    def __init__(self,t1=Tile(),t2=Tile(),t3=Tile(),t4=Tile(),t5=Tile(),t6=Tile(),t7=Tile(),t8=Tile(),t9=Tile(),t10=Tile(),t11=Tile(),t12=Tile(),t13=Tile(),t14=Tile(),t15=Tile(),t16=Tile()):

        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.t7 = t7
        self.t8 = t8
        self.t9 = t9
        self.t10 = t10
        self.t11 = t11
        self.t12 = t12
        self.t13 = t13
        self.t14 = t14
        self.t15 = t15
        self.t16 = t16

        self.whiteStack1 = [gamePiece('w','4'),gamePiece('w','3'),gamePiece('w','2'),gamePiece('w','1')]
        self.whiteStack2 = [gamePiece('w','4'),gamePiece('w','3'),gamePiece('w','2'),gamePiece('w','1')]
        self.whiteStack3 = [gamePiece('w','4'),gamePiece('w','3'),gamePiece('w','2'),gamePiece('w','1')]

        self.blackStack1 = [gamePiece('b','4'),gamePiece('b','3'),gamePiece('b','2'),gamePiece('b','1')]
        self.blackStack2 = [gamePiece('b','4'),gamePiece('b','3'),gamePiece('b','2'),gamePiece('b','1')]
        self.blackStack3 = [gamePiece('b','4'),gamePiece('b','3'),gamePiece('b','2'),gamePiece('b','1')]

    def destack_piece(self, stack, destination, turn):
        if stack == '1' and turn == 'w':
            self.whiteStack1.remove(self.whiteStack1[0])
        elif stack == '2' and turn == 'w':
            self.whiteStack2.remove(self.whiteStack2[0])
        elif stack == '3' and turn == 'w':
            self.whiteStack3.remove(self.whiteStack3[0])
        elif stack == '1' and turn == 'b':
            self.blackStack1.remove(self.blackStack1[0])
        elif stack == '2' and turn == 'b':
            self.blackStack2.remove(self.blackStack2[0])
        elif stack == '3' and turn == 'b':
            self.blackStack3.remove(self.blackStack3[0])
        else:
            pass

    def spawn_piece(self, stack, destination, turn):
        
        piece = 0
        if True:
            if stack == '1' and turn == 'w' and len(self.whiteStack1) > 0:
                piece = self.whiteStack1[0]
            elif stack == '2' and turn == 'w' and len(self.whiteStack2) > 0:
                piece = self.whiteStack2[0]
            elif stack == '3' and turn == 'w' and len(self.whiteStack3) > 0:
                piece = self.whiteStack3[0]
            elif stack == '1' and turn == 'b' and len(self.blackStack1) > 0:
                piece = self.blackStack1[0]
            elif stack == '2' and turn == 'b' and len(self.blackStack2) > 0:
                piece = self.blackStack2[0]
            elif stack == '3' and turn == 'b' and len(self.blackStack3) > 0:
                piece = self.blackStack3[0]
            else:
                return False

        if destination == '1':
            x = self.t1.update_shell(piece)
            if x == True:
                self.destack_piece(stack, destination, turn)
                return True
            else:
                return False
        elif destination == '2':
            x = self.t2.update_shell(piece)
            if x == True:
                self.destack_piece(stack, destination, turn)
                return True
            else:
                return False
        elif destination == '3':
            x = self.t3.update_shell(piece)
            if x == True:
                self.destack_piece(stack, destination, turn)
                return True
            else:
                return False
        elif destination == '4':
            x = self.t4.update_shell(piece)
            if x == True:
                self.destack_piece(stack, destination, turn)
                return True
            else:
                return False
        elif destination == '5':
            x = self.t5.update_shell(piece)
            if x == True:
                self.destack_piece(stack, destination, turn)
                return True
            else:
                return False
        elif destination == '6':
            x = self.t6.update_shell(piece)
            if x == True:
                self.destack_piece(stack, destination, turn)
                return True
            else:
                return False
        elif destination == '7':
            x = self.t7.update_shell(piece)
            if x == True:
                self.destack_piece(stack, destination, turn)
                return True
            else:
                return False
        elif destination == '8':
            x = self.t8.update_shell(piece)
            if x == True:
                self.destack_piece(stack, destination, turn)
                return True
            else:
                return False
        elif destination == '9':
            x = self.t9.update_shell(piece)
            if x == True:
                self.destack_piece(stack, destination, turn)
                return True
            else:
                return False
        elif destination == '10':
            x = self.t10.update_shell(piece)
            if x == True:
                self.destack_piece(stack, destination, turn)
                return True
            else:
                return False
        elif destination == '11':
            x = self.t11.update_shell(piece)
            if x == True:
                self.destack_piece(stack, destination, turn)
                return True
            else:
                return False
        elif destination == '12':
            x = self.t12.update_shell(piece)
            if x == True:
                self.destack_piece(stack, destination, turn)
                return True
            else:
                return False
        elif destination == '13':
            x = self.t13.update_shell(piece)
            if x == True:
                self.destack_piece(stack, destination, turn)
                return True
            else:
                return False
        elif destination == '14':
            x = self.t14.update_shell(piece)
            if x == True:
                self.destack_piece(stack, destination, turn)
                return True
            else:
                return False
        elif destination == '15':
            x = self.t15.update_shell(piece)
            if x == True:
                self.destack_piece(stack, destination, turn)
                return True
            else:
                return False
        elif destination == '16':
            x = self.t16.update_shell(piece)
            if x == True:
                self.destack_piece(stack, destination, turn)
                return True
            else:
                return False

    def remove_old_piece(self,start):
        if start == '1':
            self.t1.shells.remove(self.t1.shells[0])
        elif start == '2':
            self.t2.shells.remove(self.t2.shells[0])
        elif start == '3':
            self.t3.shells.remove(self.t3.shells[0])
        elif start == '4':
            self.t4.shells.remove(self.t4.shells[0])
        elif start == '5':
            self.t5.shells.remove(self.t5.shells[0])
        elif start == '6':
            self.t6.shells.remove(self.t6.shells[0])
        elif start == '7':
            self.t7.shells.remove(self.t7.shells[0])
        elif start == '8':
            self.t8.shells.remove(self.t8.shells[0])
        elif start == '9':
            self.t9.shells.remove(self.t9.shells[0])
        elif start == '10':
            self.t10.shells.remove(self.t10.shells[0])
        elif start == '11':
            self.t11.shells.remove(self.t11.shells[0])
        elif start == '12':
            self.t12.shells.remove(self.t12.shells[0])
        elif start == '13':
            self.t13.shells.remove(self.t13.shells[0])
        elif start == '14':
            self.t14.shells.remove(self.t14.shells[0])
        elif start == '15':
            self.t15.shells.remove(self.t15.shells[0])
        elif start == '16':
            self.t16.shells.remove(self.t16.shells[0])
        else:
            pass

    def move_piece(self, start, destination, turn):
        #these ifs exist so I can minimize the long repetitive bits of code. First verifies starting point and second the ending point
        if True:
            init = gamePiece('+','+')
            if start == '1':
                if len(self.t1.shells) > 0 and self.t1.shells[0].color == turn:
                    init = self.t1.shells[0]
            elif start == '2':
                if len(self.t2.shells) > 0 and self.t2.shells[0].color == turn:
                    init = self.t2.shells[0]
            elif start == '3':
                if len(self.t3.shells) > 0 and self.t3.shells[0].color == turn:
                    init = self.t3.shells[0]
            elif start == '4':
                if len(self.t4.shells) > 0 and self.t4.shells[0].color == turn:
                    init = self.t4.shells[0]
            elif start == '5':
                if len(self.t5.shells) > 0 and self.t5.shells[0].color == turn:
                    init = self.t5.shells[0]
            elif start == '6':
                if len(self.t6.shells) > 0 and self.t6.shells[0].color == turn:
                    init = self.t6.shells[0]
            elif start == '7':
                if len(self.t7.shells) > 0 and self.t7.shells[0].color == turn:
                    init = self.t7.shells[0]
            elif start == '8':
                if len(self.t8.shells) > 0 and self.t8.shells[0].color == turn:
                    init = self.t8.shells[0]
            elif start == '9':
                if len(self.t9.shells) > 0 and self.t9.shells[0].color == turn:
                    init = self.t9.shells[0]
            elif start == '10':
                if len(self.t10.shells) > 0 and self.t10.shells[0].color == turn:
                    init = self.t10.shells[0]
            elif start == '11':
                if len(self.t11.shells) > 0 and self.t11.shells[0].color == turn:
                    init = self.t11.shells[0]
            elif start == '12':
                if len(self.t12.shells) > 0 and self.t12.shells[0].color == turn:
                    init = self.t12.shells[0]
            elif start == '13':
                if len(self.t13.shells) > 0 and self.t13.shells[0].color == turn:
                    init = self.t13.shells[0]
            elif start == '14':
                if len(self.t14.shells) > 0 and self.t14.shells[0].color == turn:
                    init = self.t14.shells[0]
            elif start == '15':
                if len(self.t15.shells) > 0 and self.t15.shells[0].color == turn:
                    init = self.t15.shells[0]
            elif start == '16':
                if len(self.t16.shells) > 0 and self.t16.shells[0].color == turn:
                    init = self.t16.shells[0]
            else:
                return False
        if init.color == turn:
            if destination == '1':
                res = self.t1.update_shell(init)
                if res == False:
                    return False
            
            elif destination == '2':
                res = self.t2.update_shell(init)
                if res == False:
                    return False
            
            elif destination == '3':
                res = self.t3.update_shell(init)
                if res == False:
                    return False
            
            elif destination == '4':
                res = self.t4.update_shell(init)
                if res == False:
                    return False
            
            elif destination == '5':
                res = self.t5.update_shell(init)
                if res == False:
                    return False
            
            elif destination == '6':
                res = self.t6.update_shell(init)
                if res == False:
                    return False
            
            elif destination == '7':
                res = self.t7.update_shell(init)
                if res == False:
                    return False
            
            elif destination == '8':
                res = self.t8.update_shell(init)
                if res == False:
                    return False
            
            elif destination == '9':
                res = self.t9.update_shell(init)
                if res == False:
                    return False
            
            elif destination == '10':
                res = self.t10.update_shell(init)
                if res == False:
                    return False
            
            elif destination == '11':
                res = self.t11.update_shell(init)
                if res == False:
                    return False
            
            elif destination == '12':
                res = self.t12.update_shell(init)
                if res == False:
                    return False
            
            elif destination == '13':
                res = self.t13.update_shell(init)
                if res == False:
                    return False
            
            elif destination == '14':
                res = self.t14.update_shell(init)
                if res == False:
                    return False
            
            elif destination == '15':
                res = self.t15.update_shell(init)
                if res == False:
                    return False
            
            elif destination == '16':
                res = self.t16.update_shell(init)
                if res == False:
                    return False
            
            self.remove_old_piece(start)
            return True
        else:
            return False

    def parse_input(self, inp, turn):
        if inp[0] == 'spawn':
            self.spawn_piece(inp[1],inp[2],turn)
        elif inp[0] == 'move':
            self.move_piece(inp[1],inp[2],turn)
        else:
            pass
    
    def print_board(self):
        s1 = '--'
        if len(self.t1.shells) > 0:
            s1 = self.t1.shells[0].size + self.t1.shells[0].color
        s2 = '--'
        if len(self.t2.shells) > 0:
            s2 = self.t2.shells[0].size + self.t2.shells[0].color
        s3 = '--'
        if len(self.t3.shells) > 0:
            s3 = self.t3.shells[0].size + self.t3.shells[0].color
        s4 = '--'
        if len(self.t4.shells) > 0:
            s4 = self.t4.shells[0].size + self.t4.shells[0].color
        s5 = '--'
        if len(self.t5.shells) > 0:
            s5 = self.t5.shells[0].size + self.t5.shells[0].color
        s6 = '--'
        if len(self.t6.shells) > 0:
            s6 = self.t6.shells[0].size + self.t6.shells[0].color
        s7 = '--'
        if len(self.t7.shells) > 0:
            s7 = self.t7.shells[0].size + self.t7.shells[0].color
        s8 = '--'
        if len(self.t8.shells) > 0:
            s8 = self.t8.shells[0].size + self.t8.shells[0].color
        s9 = '--'
        if len(self.t9.shells) > 0:
            s9 = self.t9.shells[0].size + self.t9.shells[0].color
        s10 = '--'
        if len(self.t10.shells) > 0:
            s10 = self.t10.shells[0].size + self.t10.shells[0].color
        s11 = '--'
        if len(self.t11.shells) > 0:
            s11 = self.t11.shells[0].size + self.t11.shells[0].color
        s12 = '--'
        if len(self.t12.shells) > 0:
            s12 = self.t12.shells[0].size + self.t12.shells[0].color
        s13 = '--'
        if len(self.t13.shells) > 0:
            s13 = self.t13.shells[0].size + self.t13.shells[0].color
        s14 = '--'
        if len(self.t14.shells) > 0:
            s14 = self.t14.shells[0].size + self.t14.shells[0].color
        s15 = '--'
        if len(self.t15.shells) > 0:
            s15 = self.t15.shells[0].size + self.t15.shells[0].color
        s16 = '--'
        if len(self.t16.shells) > 0:
            s16 = self.t16.shells[0].size + self.t16.shells[0].color
        print("┌―――――――――――┐\n│{}│{}│{}│{}│\n│{}│{}│{}│{}│\n│{}│{}│{}│{}│\n│{}│{}│{}│{}│\n└―――――――――――┘".format(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16))

    def check_for_win(self):
        if len(self.t1.shells) > 0 and len(self.t2.shells) > 0 and len(self.t3.shells) > 0 and len(self.t4.shells) > 0:
            if self.t1.shells[0].color == self.t2.shells[0].color and self.t2.shells[0].color == self.t3.shells[0].color and self.t3.shells[0].color == self.t4.shells[0].color:
                return True
            else:
                return False
        elif len(self.t5.shells) > 0 and len(self.t6.shells) > 0 and len(self.t7.shells) > 0 and len(self.t8.shells) > 0:
            if self.t5.shells[0].color == self.t6.shells[0].color and self.t6.shells[0].color == self.t7.shells[0].color and self.t7.shells[0].color == self.t8.shells[0].color:
                return True
            else:
                return False
        elif len(self.t9.shells) > 0 and len(self.t10.shells) > 0 and len(self.t11.shells) > 0 and len(self.t12.shells) > 0:
            if self.t9.shells[0].color == self.t10.shells[0].color and self.t10.shells[0].color == self.t11.shells[0].color and self.t11.shells[0].color == self.t12.shells[0].color:
                return True
            else:
                return False
        elif len(self.t13.shells) > 0 and len(self.t14.shells) > 0 and len(self.t15.shells) > 0 and len(self.t16.shells) > 0:
            if self.t13.shells[0].color == self.t14.shells[0].color and self.t14.shells[0].color == self.t15.shells[0].color and self.t15.shells[0].color == self.t16.shells[0].color:
                return True
            else:
                return False
        elif len(self.t1.shells) > 0 and len(self.t5.shells) > 0 and len(self.t9.shells) > 0 and len(self.t13.shells) > 0:
            if self.t1.shells[0].color == self.t5.shells[0].color and self.t5.shells[0].color == self.t9.shells[0].color and self.t9.shells[0].color == self.t13.shells[0].color:
                return True
            else:
                return False
        elif len(self.t2.shells) > 0 and len(self.t6.shells) > 0 and len(self.t10.shells) > 0 and len(self.t14.shells) > 0:
            if self.t2.shells[0].color == self.t6.shells[0].color and self.t6.shells[0].color == self.t10.shells[0].color and self.t10.shells[0].color == self.t14.shells[0].color:
                return True
            else:
                return False
        elif len(self.t3.shells) > 0 and len(self.t7.shells) > 0 and len(self.t11.shells) > 0 and len(self.t15.shells) > 0:
            if self.t3.shells[0].color == self.t7.shells[0].color and self.t7.shells[0].color == self.t11.shells[0].color and self.t11.shells[0].color == self.t15.shells[0].color:
                return True
            else:
                return False
        elif len(self.t4.shells) > 0 and len(self.t8.shells) > 0 and len(self.t12.shells) > 0 and len(self.t16.shells) > 0:
            if self.t4.shells[0].color == self.t8.shells[0].color and self.t8.shells[0].color == self.t12.shells[0].color and self.t12.shells[0].color == self.t16.shells[0].color:
                return True
            else:
                return False
        elif len(self.t1.shells) > 0 and len(self.t6.shells) > 0 and len(self.t11.shells) > 0 and len(self.t16.shells) > 0:
            if self.t1.shells[0].color == self.t6.shells[0].color and self.t6.shells[0].color == self.t11.shells[0].color and self.t11.shells[0].color == self.t16.shells[0].color:
                return True
            else:
                return False
        elif len(self.t4.shells) > 0 and len(self.t7.shells) > 0 and len(self.t10.shells) > 0 and len(self.t13.shells) > 0:
            if self.t4.shells[0].color == self.t7.shells[0].color and self.t7.shells[0].color == self.t10.shells[0].color and self.t10.shells[0].color == self.t13.shells[0].color:
                return True
            else:
                return False
        else:
            return False

    def broadcast_win(self,winner):
        if winner == 'w':
            print("\n\n\nWhite wins!")
            stop
        else:
            print("\n\n\nBlack wins!")
            stop

board = GameBoard()

#little bit of engine
gameOver = False
turn = 'b'
while gameOver == False:
    if turn == 'w':
        turn = 'b'
    else:
        turn = 'w'

    valturn = False
    while valturn == False:
        inp = input("Command? ('spawn stack# destination' to place from stacks, 'move startplace destination' to move a piece)")
        refinp = inp.split()

        if refinp[0] == 'spawn':
            valturn = board.spawn_piece(refinp[1],refinp[2],turn)
        elif refinp[0] == 'move':
            valturn = board.move_piece(refinp[1],refinp[2],turn)
        else:
            pass
        
        board.print_board()
        if board.check_for_win() == True:
            board.broadcast_win(turn)



'''
#place on a piece
res = board.spawn_piece('1','3','w')
print(res)
board.print_board()

#trying illegal placement
res = board.spawn_piece('1','3','b')
print(res)
board.print_board()

#fixing illegal placement
res = board.spawn_piece('1','4','b')
print(res)
board.print_board()

#prepping for eat/placing smaller piece
res = board.spawn_piece('1','11','w')
print(res)
board.print_board()

#trying moving
res = board.move_piece('4','8','b')
print(res)
board.print_board()

#trying illegal move
res = board.move_piece('3','8','w')
print(res)
board.print_board()

#trying eating
res = board.move_piece('8','11','b')
print(res)
board.print_board()

#moving off eaten piece to see if it stays
res = board.move_piece('11','1','b')
print(res)
board.print_board()

#emptying a stack onto the board
res = board.spawn_piece('2','13','b')
print(res)
board.print_board()

res = board.spawn_piece('2','14','b')
print(res)
board.print_board()

res = board.spawn_piece('2','15','b')
print(res)
board.print_board()

res = board.spawn_piece('2','16','b')
print(res)
board.print_board()

#trying to place from empty stack
res = board.spawn_piece('2','6','b')
print(res)
board.print_board()

┌―――――――――――┐
│--│--│--│--│
│--│--│--│--│
│--│--│--│--│
│--│--│--│--│
└―――――――――――┘
'''


