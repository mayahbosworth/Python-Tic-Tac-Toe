
from tkinter.constants import YES
from graphics import *


# Create the graphics window.
# win = GraphWin('Tic-Tac-Toe', 500, 666)
win = GraphWin('Tic-Tac-Toe', 500, 550)

# draw board
class TicTacToeBoard(object):
    def __init__(self):
        self.draw_left_line()
        self.draw_right_line()
        self.draw_top_line()
        self.draw_bottom_line()
        self.draw_reset_box()
        self.draw_reset_text()

    def draw_left_line(self):
        leftline = Line(Point(166,35), Point(166,465))
        leftline.setWidth(5)
        leftline.draw(win)

    def draw_right_line(self):
        rightline = Line(Point(333,35), Point(333,465))
        rightline.setWidth(5)
        rightline.draw(win)

    def draw_top_line(self):
        topline = Line(Point(35,166), Point(465,166))
        topline.setWidth(5)
        topline.draw(win)

    def draw_bottom_line(self):
        bottomline = Line(Point(35,333), Point(466,333))
        bottomline.setWidth(5)
        bottomline.draw(win)

    def draw_reset_box(self):
        resetbox = Rectangle(Point(166,475), Point(333,520))
        resetbox.setFill('blue')
        resetbox.draw(win)

    def draw_reset_text(self):
        reset_text = Text(Point(249,497), 'Reset Game')
        reset_text.setSize(20)
        reset_text.draw(win)


#below is each X/O drawing
def draw_1(marker):
    draw_1 = Text(Point(100,100), marker)
    draw_1.setSize(36)
    draw_1.setFill('orange')
    draw_1.draw(win)

def draw_2(marker):
    draw_2 = Text(Point(250,100), marker)
    draw_2.setSize(36)
    draw_2.setFill('orange')
    draw_2.draw(win)

def draw_3(marker):
    draw_3 = Text(Point(400,100), marker)
    draw_3.setSize(36)
    draw_3.setFill('orange')
    draw_3.draw(win)

def draw_4(marker):
    draw_4 = Text(Point(100,250), marker)
    draw_4.setSize(36)
    draw_4.setFill('orange')
    draw_4.draw(win)

def draw_5(marker):
    draw_5 = Text(Point(250,250), marker)
    draw_5.setSize(36)
    draw_5.setFill('orange')
    draw_5.draw(win)

def draw_6(marker):
    draw_6 = Text(Point(400,250), marker)
    draw_6.setSize(36)
    draw_6.setFill('orange')
    draw_6.draw(win)

def draw_7(marker):
    draw_7 = Text(Point(100,400), marker)
    draw_7.setSize(36)
    draw_7.setFill('orange')
    draw_7.draw(win)

def draw_8(marker):
    draw_8 = Text(Point(250,400), marker)
    draw_8.setSize(36)
    draw_8.setFill('orange')
    draw_8.draw(win)

def draw_9(marker):
    draw_9 = Text(Point(400,400), marker)
    draw_9.setSize(36)
    draw_9.setFill('orange')
    draw_9.draw(win)


#below is the graphics code for 'win lines'
def drawline_147():
    drawline_147 = Line(Point(100,65), Point(100,435))
    drawline_147.setWidth(6)
    drawline_147.setFill('orange')
    drawline_147.draw(win)

def drawline_258():
    drawline_258 = Line(Point(250,65), Point(250,435))
    drawline_258.setWidth(6)
    drawline_258.setFill('orange')
    drawline_258.draw(win)

def drawline_369():
    drawline_369 = Line(Point(400,65), Point(400,435))
    drawline_369.setWidth(6)
    drawline_369.setFill('orange')
    drawline_369.draw(win)

def drawline_123():
    drawline_123 = Line(Point(65,100), Point(435,100))
    drawline_123.setWidth(6)
    drawline_123.setFill('orange')
    drawline_123.draw(win)

def drawline_456():
    drawline_456 = Line(Point(65,250), Point(435,250))
    drawline_456.setWidth(6)
    drawline_456.setFill('orange')
    drawline_456.draw(win)

def drawline_789():
    drawline_789 = Line(Point(45,400), Point(435,400))
    drawline_789.setWidth(6)
    drawline_789.setFill('orange')
    drawline_789.draw(win)

def drawline_159():
    drawline_159 = Line(Point(68,68), Point(432,432))
    drawline_159.setWidth(6)
    drawline_159.setFill('orange')
    drawline_159.draw(win)

def drawline_753():
    drawline_753 = Line(Point(68,432), Point(432,68))
    drawline_753.setWidth(6)
    drawline_753.setFill('orange')
    drawline_753.draw(win)

#graphics for Cat aka 'draw'
def drawTie():
    draw_tie_points_label = Text(Point(250,20), 'TIE (lame)') 
    draw_tie_points_label.setSize(36)
    draw_tie_points_label.setFill('black')
    draw_tie_points_label.draw(win)


#below is to make turn alternate between X and O
def getMarker(turn):
    if(turn % 2 == 0):
        return "X"
    else:
        return "O"


# User's move


#whipe the board
def wipe_board():
    wipe_board = Rectangle(Point(0,0), Point(600,600))
    wipe_board.setFill('white')
    wipe_board.draw(win)


#spots for wins


def resetreset():
    wipe_board()
    play_game()

    
def game_over():
    while True:
        p = win.getMouse()
        x = p.getX()
        y = p.getY()
        #draw
        if (x > 166 and x < 333) and (y > 475 and y < 520):
            resetreset()

def play_game():
    TicTacToeBoard()
    turn = 0
    spot1 = 'a'
    spot2 = 'b'
    spot3 = 'c'
    spot4 = 'd'
    spot5 = 'e'
    spot6 = 'f'
    spot7 = 'g'
    spot8 = 'h'
    spot9 = 'i'
    empty_1 = 0
    empty_2 = 0
    empty_3 = 0
    empty_4 = 0
    empty_5 = 0
    empty_6 = 0
    empty_7 = 0
    empty_8 = 0
    empty_9 = 0
    reset = True
    x=0
    y=0
    while reset:
        # logic for wins
        if spot1 == spot2 and spot1 == spot3 and spot2 == spot3:
            drawline_123()
            game_over()
        elif spot4 == spot5 and spot4 == spot6 and spot5 == spot6:
            drawline_456()
            game_over()
        elif spot7 == spot8 and spot7 == spot9 and spot8 == spot9:
            drawline_789()
            game_over()
        elif spot1 == spot4 and spot1 == spot7 and spot4 == spot7:
            drawline_147()
            game_over()
        elif spot2 == spot5 and spot2 == spot8 and spot5 == spot8:
            drawline_258()
            game_over()
        elif spot3 == spot6 and spot3 == spot9 and spot6 == spot9:
            drawline_369()
            game_over()
        elif spot1 == spot5 and spot1 == spot9 and spot5 == spot9:
            drawline_159()
            game_over()
        elif spot7 == spot5 and spot7 == spot3 and spot5 == spot3:
            drawline_753()
            game_over()
        if turn is 9:
            drawTie()
            game_over()
        marker = getMarker(turn)
        p = win.getMouse()
        x = p.getX()
        y = p.getY()
        #draw
        if (x > 166 and x < 333) and (y > 475 and y < 520):
            resetreset()


        inside_1 = (x > 0 and x < 166) and (y > 0 and y < 166)
        if (x > 0 and x < 166) and (y > 0 and y < 166):
            inside_1 == True
            if inside_1 == True:
                if empty_1 == 0: #if square is empty
                    draw_1(marker)
                    turn += 1
                    empty_1 = 1
                    spot1 = marker
                continue
        
        inside_2 = (x > 166 and x < 333) and (y > 0 and y < 166)
        if (x > 166 and x < 333) and (y > 0 and y < 166):
            if inside_2:
                if empty_2 == 0: #if square is empty
                    draw_2(marker)
                    turn += 1
                    empty_2 = 1
                    spot2 = marker
                continue
                
        inside_3 = (x > 333 and x < 500) and (y > 0 and y < 166)
        if (x > 333 and x < 500) and (y > 0 and y < 166):
            if inside_3:
                if empty_3 == 0: #if square is empty
                    draw_3(marker)
                    turn += 1
                    empty_3 = 1
                    spot3 = marker
                continue

        inside_4 = (x > 0 and x < 166) and (y > 166 and y < 333)
        if (x > 0 and x < 166) and (y > 166 and y < 333):
            if inside_4:
                if empty_4 == 0: #if square is empty
                    draw_4(marker)
                    turn += 1
                    empty_4 = 1
                    spot4 = marker
                continue


        inside_5 = (x > 166 and x < 333) and (y > 166 and y < 333)
        if (x > 166 and x < 333) and (y > 166 and y < 333):
            if inside_5:
                if empty_5 == 0: #if square is empty
                    draw_5(marker)
                    turn += 1
                    empty_5 = 1
                    spot5 = marker
                continue

        inside_6 = (x > 333 and x < 500) and (y > 166 and y < 333)
        if (x > 333 and x < 500) and (y > 166 and y < 333):
            if inside_6:
                if empty_6 == 0: #if square is empty
                    draw_6(marker)
                    turn += 1
                    empty_6 = 1
                    spot6 = marker
                continue

        inside_7 = (x > 0 and x < 166) and (y > 333 and y < 500)
        if (x > 0 and x < 166) and (y > 333 and y < 500):
            if inside_7:
                if empty_7 == 0: #if square is empty
                    draw_7(marker)
                    turn += 1
                    empty_7 = 1
                    spot7 = marker
                continue

        inside_8 = (x > 166 and x < 333) and (y > 333 and y < 500)
        if (x > 166 and x < 333) and (y > 333 and y < 500):
            if inside_8:
                if empty_8 == 0: #if square is empty
                    draw_8(marker)
                    turn += 1
                    empty_8 = 1
                    spot8 = marker
                continue
        
        inside_9 = (x > 333 and x < 500) and (y > 333 and y < 500)
        if (x > 333 and x < 500) and (y > 333 and y < 500):
            if inside_9:
                if empty_9 == 0: #if square is empty
                    draw_9(marker)
                    turn += 1
                    empty_9 = 1
                    spot9 = marker
                continue

        else:
            inside_1 == False
            continue


play_game()