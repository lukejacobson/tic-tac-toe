from tkinter import Tk, Canvas, Frame, BOTH, Button, Text
from time import sleep
from AI import getNextMove, isWinState, isInt, isDrawState

WIDTH = 600
HEIGHT = int((13/11) * WIDTH)
SIZE = int((3/11) * WIDTH)
GAP = int((1/22) * WIDTH)

BOX_BOUNDS = [
    [GAP,GAP+SIZE],
    [2*GAP + SIZE, 2*(GAP + SIZE)], 
    [3*GAP + 2*SIZE, 3*(GAP + SIZE)]
]

WHITE = "#FFFFFF"
BLACK = "#000000"
GREY = "#BBBBBB"
FIRE = "#E23C22"
GREEN = "#5BC236"
RED = "#FF0000"
YELLOW = "#FFFF00"

PLAYER_1 = 'X'
COMPUTER = 'O'

def draw_game():
    root = Tk()
    ex = Main(root)
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    root.mainloop()

class Main(Frame):

    def __init__(self, master):
        super().__init__()
        self.initUI(master)
    
    def initUI(self, master):
        self.master = master
        master.title("Board")
        self.pack(fill=BOTH, expand = 1)
        self.board = self.initialiseBoard()
        self.canvas = Canvas(self)
        self.canvas['bg'] = GREY
        self.whos_turn = PLAYER_1
        self.message = "It's YOUR turn"
        self.winner = None
        self.AI_move = None

        draw_squares(self.canvas, self.board, self.message)

        self.master.bind("<Button-1>", self.do_move)

        self.end_button = Button(master, text="Reset Game", command = self.reset_game)
        self.end_button.pack()
    
    # called when PLAYER_1 makes a move
    def do_move(self,event):
        
        x = event.x
        y = event.y
        x = find_column(x)
        y = find_column(y)
        win_state = False
        bg_colour = GREY
        board_full = False

        # check if actually clicked on a square
        if isInt(x) and isInt(y):
            # make sure square is empty
            if self.board[x][y] != ' ':
                self.message = "Oops, you can't go here, silly!"
                bg_colour = FIRE
            else:
                self.board[x][y] = self.whos_turn
                win_state = isWinState(self.board)
                
                if win_state and not self.winner:
                    self.winner = win_state

                board_full = isDrawState(self.board)

                # is the game is still going, calculate COMPUTER's response
                if not self.winner and not board_full:
                    self.whos_turn = COMPUTER
                    (a,b) = getNextMove(self.board, COMPUTER) 
                    self.board[a][b] = self.whos_turn
                    self.winner = isWinState(self.board)
                    self.whos_turn = PLAYER_1
                    self.message = "It's YOUR turn"
        
        else:
            self.message = "Please click on a valid square!"
            bg_colour = FIRE
        
        if self.winner == PLAYER_1:
            self.message = "Congrats, YOU Won!!!"
            bg_colour = GREEN
        elif self.winner == COMPUTER:
            self.message = "Damn, COMPUTER Won"
            bg_colour = RED
        elif board_full:
            self.winner = 'D'
            self.message = "Its A Draw"
            bg_colour = YELLOW

        

        self.canvas.destroy()
        self.canvas = Canvas(self)
        self.canvas['bg'] = bg_colour
        draw_squares(self.canvas, self.board, self.message)


    def initialiseBoard(self):
        return [[' ' for i in range(3)] for i in range(3)]
    
    def reset_game(self):
        self.board = self.initialiseBoard()
        self.canvas.destroy()
        self.canvas = Canvas(self)
        self.canvas['bg'] = GREY
        self.whos_turn = PLAYER_1
        self.message = "It's YOUR turn!!"
        self.winner = None
        self.AI_move = None
        draw_squares(self.canvas, self.board, self.message)





def find_column(x):
    for i,bound in enumerate(BOX_BOUNDS):
        if x >= bound[0] and x <= bound[1]:
            return i
    return None


def draw_squares(canvas, board, message):
    
    for i in range(0,3):
        for j in range(0,3):
            
            x1 = SIZE*i+((i+1)*GAP)
            x2 = SIZE*(i+1)+((i+1)*GAP)
            y1 = SIZE*j+((j+1)*GAP)
            y2 = SIZE*(j+1)+((j+1)*GAP)
            
            this_square = board[i][j]

            canvas.create_rectangle(x1, y1, x2, y2, outline = BLACK, fill = WHITE)

            canvas.create_text(
                (x1+x2)/2, (y1+y2)/2, 
                text = this_square, 
                fill = BLACK, 
                font = ("Ariel, {}".format(int(SIZE * (3/4))))
            )
    
    canvas.create_text(
        WIDTH/2, 5*GAP + 3*SIZE,
        text = message,
        fill = BLACK,
        font = ("Ariel, 12")
    )

    canvas.pack(fill = BOTH, expand=1)





draw_game()