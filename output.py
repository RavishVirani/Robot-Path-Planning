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

def keyDown(key,index,max_length):
    if key == pygame.K_LEFT:
        if index>0:
            index = index-1
    elif key == pygame.K_RIGHT:
        if index<max_length-1:
            index = index + 1
    return index

def bigKeyDown(key,index,robot_index,max_length,num_robots):
    if key == pygame.K_LEFT:
        if index > 0:
            index = index - 1
    elif key == pygame.K_RIGHT:
        if index < max_length-1:
            index = index + 1
    elif key == pygame.K_DOWN:
        if robot_index > 0:
            robot_index = robot_index - 1
    elif key == pygame.K_UP:
        if robot_index < num_robots - 1:
            robot_index = robot_index + 1
    return index,robot_index


def drawBigBoard(boardHeight,boardWidth,paths,goal,board):
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    offset = 20            


    squareWidth = WIDTH // (offset*2)
    squareHeight = HEIGHT // (offset*2)

    image = pygame.image.load(r'robot.jpg')
    image = pygame.transform.scale(image, (squareWidth, squareHeight))

    
    robot_index = 0
    index = 0
    max_index = 0
    num_bots = len(paths)
    for path in paths:
        if len(path)>max_index:
            max_index = len(path)
            
    #If the robot has no paths, then make it "stay still"
    for i in range(len(paths)):
        if len(paths[i])==1 and paths[i][0]!=(goal[1],goal[0]):
            paths[i] = paths[i]*max_index

    


    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print("Exiting Output")
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                index, robot_index=bigKeyDown(event.key,index,robot_index,max_index,num_bots)
        if len(paths[robot_index])<=index:
            x = goal[0]
            y = goal[1]
        else:
            x = paths[robot_index][index][1]
            y = paths[robot_index][index][0]
        
        for i in range(-offset,offset,1):
            for n in range(-offset,offset,1):
                rect = pygame.Rect((n+offset)*squareWidth, (i+offset)*squareHeight, squareWidth, squareHeight)
                
                if i == 0  and n == 0:
                    #print("robot")
                    SCREEN.blit(image, (offset*squareWidth, offset*squareHeight))                
                elif y+i<0 or y+i>=boardHeight:
                    pygame.draw.rect(SCREEN, WHITE, rect)
                    
                    #print("y axis balck")
                elif x+n<0 or x+n>=boardWidth:
                    pygame.draw.rect(SCREEN, WHITE, rect)
                    
                    #print("x axis black")
                elif board[y+i][x+n]==-1:
                    pygame.draw.rect(SCREEN, RED, rect)
                    pygame.draw.rect(SCREEN, WHITE, rect, 1)

                    #print("obstacle")
                elif board[y+i][x+n]==0:
                    #print("goal")
                    pygame.draw.rect(SCREEN, GOLD, rect)
                    pygame.draw.rect(SCREEN, WHITE, rect, 1)                
                else:
                    #print("blank")
                    pygame.draw.rect(SCREEN, BLACK, rect)                    
                    pygame.draw.rect(SCREEN, WHITE, rect, 1)
        #Other bots
        for i in range(len(paths)):
            if i == robot_index or len(paths[i])<=index:
                continue
            other_x = paths[i][index][1]
            other_y = paths[i][index][0]
            if abs(x-other_x)<offset and abs(y-other_y)<offset:
                SCREEN.blit(image, ((other_x-x+offset)*squareWidth, (other_y-y+offset)*squareHeight))
                
        pygame.display.update()

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
    
    #Set the index bounds for the paths
    index = 0
    max_index = 0
    for path in pathArr:
        if len(path)>max_index:
            max_index = len(path)
            
    #If the robot has no paths, then make it "stay still"
    for i in range(len(pathArr)):
        if len(pathArr[i])==1 and pathArr[i][0]!=(goal[1],goal[0]):
            pathArr[i] = pathArr[i]*max_index
    
    # Handler for when user exits the program
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print("Exiting Output")
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                index = keyDown(event.key,index,max_index)
        rectangles = []


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
                # Otherwise draw an outline of a square with a BLACK background
                else:
                    pygame.draw.rect(SCREEN, BLACK, rect)                    
                    pygame.draw.rect(SCREEN, WHITE, rect, 1)
                    rectangles.append((rect, WHITE))
        
        # Draw the paths for robots
        drawPath(boardHeight, boardWidth, pathArr, rectangles)
        for path in pathArr:
            # If its a robot, draw the ROBOT            
            if len(path)>index:
                i = path[index][1]
                j = path[index][0]
                SCREEN.blit(image, (i*squareWidth, j*squareHeight))
                pygame.draw.rect(SCREEN, WHITE, rect, 1)
                rectangles.append((rect, WHITE))
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

            


