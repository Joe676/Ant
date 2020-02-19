import pygame, sys

cols = 200
rows = 200

board = []

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
move = ((0, -1), (1, 0), (0, 1), (-1, 0))

antx = int(cols//2)
anty = int(rows//2)
anth = UP

def t(x, y):
    global cols
    global rows
    return int((x+cols) % cols), int((y + rows) % rows)

def boardInit(c, r):
    for i in range(r):
        board.append([])
        for j in range(c):
            board[i].append(0)

def step():
    #1: turn right on OFF(0); turn left on ON(1) 
    #2: change color
    #3: move forward
    global antx
    global anty
    global anth
    #1
    if board[antx][anty] == 0:
        anth = (anth + 3) % 4 #turn right is left 3 times
    else:
        anth = (anth + 1) % 4
    #2
    board[antx][anty] = (board[antx][anty] + 1) % 2
    #3
    antx += move[anth][0]
    anty += move[anth][1]
    antx, anty = t(antx, anty)

pygame.init()

size = width, height = 600, 600
w, h = width/cols, height/rows
black = 0, 0, 0
white = 255, 255, 255
red = 255, 20, 20
screen = pygame.display.set_mode(size)

boardInit(cols, rows)

if __name__ == "__main__":
    while True:
        screen.fill(white)
        for i in range(cols):
            for j in range(rows):
                if(board[i][j] == 1):
                    pygame.draw.rect(screen, black, (i*w, j*h, w, h))

        pygame.draw.rect(screen, red, (antx*w, anty*h, w, h))
        """for i in range(cols):
            pygame.draw.line(screen, black, ((i+1)*w, 0), ((i+1)*w, height), 1)
        for i in range(rows):
            pygame.draw.line(screen, black, (0, (i+1)*h), (width, (i+1)*h), 1)"""
        step()
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


