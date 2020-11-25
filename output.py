import pygame
import sys

# Global Variables
BLACK = (0,0,0)
WHITE = (200,200,200)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
GOLD = (163, 128, 31)
TURQOISE = (6, 209, 155)
PURPLE = (168, 6, 209)
HEIGHT = 512
WIDTH = 512
OFFSET = 5

# Credit for robot image goes to:
# "Designed by pch.vector / Freepik"

def drawBoard(boardHeight, boardWidth, pathArr, obsticalArr, goal, rob):
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    rectangles = []
    #print(obsticalArr)

    # Get the size of each square
    squareWidth = WIDTH // boardWidth
    squareHeight = HEIGHT // boardHeight

    # Initialize the image
    image = pygame.image.load(r'robot.jpg')
    image = pygame.transform.scale(image, (squareWidth, squareHeight))


    # Draw all the squares
    for i in range(boardWidth):
        for j in range(boardHeight):
            rect = pygame.Rect(i*squareWidth, j*squareHeight, squareWidth, squareHeight)
            # If its an obstical colour the square RED
            if ((i,j) in obsticalArr):
                pygame.draw.rect(SCREEN, RED, rect)
                pygame.draw.rect(SCREEN, WHITE, rect, 1)
                rectangles.append((rect, RED))
            # If its the goal, colour the square GOLD
            elif (i,j) == goal:
                pygame.draw.rect(SCREEN, GOLD, rect)
                pygame.draw.rect(SCREEN, WHITE, rect, 1)
                rectangles.append((rect, GOLD))
            # If its a start point for a robot, draw the ROBOT
            elif (i,j) in rob:
                SCREEN.blit(image, (i*squareWidth, j*squareHeight))
                pygame.draw.rect(SCREEN, WHITE, rect, 1)
                rectangles.append((rect, WHITE))
            # Otherwise draw an outline of a square with a BLACK background
            else:
                pygame.draw.rect(SCREEN, WHITE, rect, 1)
                rectangles.append((rect, WHITE))
    
    # Draw the paths for robots
    drawPath(boardHeight, boardWidth, pathArr, rectangles)
    
    # Handler for when user exits the program
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print("Exiting Output")
                sys.exit()

        pygame.display.update()

# Draw the paths for robots using different colours
def drawPath(boardHeight, boardWidth, pathArr, rectangles):
    cnt = 0
    colours = [GREEN, BLUE, TURQOISE, PURPLE]
    colour = BLUE

    # Loop through each path array
    for i in pathArr:
        colour = colours[cnt % 4]
        last = None
        # Loop through each point in the array and draw it
        for j in i:
            ind = j[0] + j[1] * boardHeight
            square = rectangles[ind]
            # If counter is 4 or below, draw new line to the right and under the old line
            if cnt < 5:
                mid = (square[0][2]/2 + square[0][0] + (cnt*OFFSET), square[0][3]/2 + square[0][1] + (cnt*OFFSET))
            # Otherwise draw it to the right and above the old line
            else:
                temp = cnt % 5
                temp +=1
                mid = (square[0][2]/2 + square[0][0] - (temp*OFFSET), square[0][3]/2 + square[0][1] - (temp*OFFSET))
            # If its the first value, skip
            if last == None:
                last = mid
            # Draw a line from the last value to the current value
            else:
                pygame.draw.line(SCREEN, colour, last, mid, 5)
                last = mid
        cnt+=1

            


