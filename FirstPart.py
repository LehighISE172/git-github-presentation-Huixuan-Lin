'''
Created on Apr 1, 2022

@author: HuixuanLin
'''
import random

import pygame
import time

pygame.init()
width = 1000
height = 700
win = pygame.display.set_mode((width, height))
white = (255, 255, 255)  # define colors
black = (0, 0, 0)
orange = (255, 140, 0)
blue = (0, 0, 255)

FPS = 30  # set the number of frames per second 
fpsClock = pygame.time.Clock()
gameExit = False

nodePos = []
for i in range(3):  # random 3 nodes on the graph
    nodePos.append([random.randint(5, width - 5), random.randint(5, height - 5)])
print(nodePos)


def move(x, x_change, y, y_change):
    x += x_change
    y += y_change
    return x, y


def speed(xpos1, ypos1, xpos2, ypos2):
    x_change = (xpos2 - xpos1) / 100
    y_change = (ypos2 - ypos1) / 100
    return x_change, y_change


def main():
    x_change, y_change = 0, 0  # set initial direction and speed
    x = nodePos[0][0]  # set initial position
    y = nodePos[0][1]
    step = 0
    path = 1
    gameExit = False
    FPS = 50  # set the number of frames per second 
    fpsClock = pygame.time.Clock()
    while not gameExit:  # main loop of the game 
        for event in pygame.event.get():  # loop over events
            if event.type == pygame.QUIT:  # set gameExlt to True if quit game
                gameExit = True
        win.fill(white)
        pygame.draw.circle(win, orange, (nodePos[0][0], nodePos[0][1]), 10)
        pygame.draw.circle(win, orange, (nodePos[1][0], nodePos[1][1]), 10)
        pygame.draw.circle(win, orange, (nodePos[2][0], nodePos[2][1]), 10)
        pygame.draw.lines(win, orange, False, nodePos)
        xCarPos = x - 20  # make the car at the center of the path
        yCarPos = y - 10
        pygame.draw.rect(win, blue, (xCarPos, yCarPos, 50, 20))
        pygame.draw.rect(win, blue, (xCarPos + 15, yCarPos - 10, 20, 10))
        pygame.draw.circle(win, black, (xCarPos + 10, yCarPos + 20), 8)
        pygame.draw.circle(win, black, (xCarPos + 40, yCarPos + 20), 8)
        pygame.display.update() 
        step += 1  # after 100 times, change direction and speed
        if path == 1:  # from node 1 to node 2
            x_change = speed(nodePos[0][0], nodePos[0][1], nodePos[1][0], nodePos[1][1])[0]
            y_change = speed(nodePos[0][0], nodePos[0][1], nodePos[1][0], nodePos[1][1])[1]
            step = 0
            path = 2
            
        elif step == 100 and path == 2:  # from node 2 to node 3
            x_change = speed(nodePos[1][0], nodePos[1][1], nodePos[2][0], nodePos[2][1])[0]
            y_change = speed(nodePos[1][0], nodePos[1][1], nodePos[2][0], nodePos[2][1])[1]
            step = 0
            path = 3
            
        elif step == 100 and path == 3:  # from node 3 to node 2
            x_change = speed(nodePos[2][0], nodePos[2][1], nodePos[1][0], nodePos[1][1])[0]
            y_change = speed(nodePos[2][0], nodePos[2][1], nodePos[1][0], nodePos[1][1])[1]
            step = 0
            path = 4
            
        elif step == 100 and path == 4:  # from node 2 to node 1
            x_change = speed(nodePos[1][0], nodePos[1][1], nodePos[0][0], nodePos[0][1])[0]
            y_change = speed(nodePos[1][0], nodePos[1][1], nodePos[0][0], nodePos[0][1])[1]
            step = 0
            path = 5
        
        elif step == 100 and path == 5:  # from node 2 to node 1
            x_change = speed(nodePos[1][0], nodePos[1][1], nodePos[0][0], nodePos[0][1])[0]
            y_change = speed(nodePos[1][0], nodePos[1][1], nodePos[0][0], nodePos[0][1])[1]
            step = 0
            path = 1
            
        x = move(x, x_change, y, y_change)[0]
        y = move(x, x_change, y, y_change)[1]
        
        fpsClock.tick(FPS)  # update the screen
    pygame.quit()

            
if __name__ == '__main__':
    main()
