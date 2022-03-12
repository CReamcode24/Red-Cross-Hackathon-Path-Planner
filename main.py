"""Path Planner Program"""
#Created by Brenden Zacek and Celina Rodriguez

from turtle import *
from Acode import *
from time import sleep

#Initializes list of blocked-off spaces
nogos = []

#Initializes graphics
t = Turtle()
t.ht()
t.penup()
screen = t.getscreen()
screen.title("Path Program")
t.showturtle()

#Defines function on left click to draw dot and add obstacle to path program
def blockoff(x, y):
  t.penup()
  t.goto(x, y)
  x = int(x) + 200
  y = 150 - int(y)
  t.pendown()
  for i in range(x - 10, x):
    if (i < 400):
      for j in range(y, y + 10):
        if (j >= 0 and j < 300):
          temp = (i, j)
          if temp not in nogos:
            nogos.append(temp)
  #fills identified area
  t.begin_fill()
  t.begin_poly()
  t.goto(x - 200, 150 - y)
  t.goto(x - 200, 140 - y)
  t.goto(x - 190, 140 - y)
  t.goto(x - 190, 150 - y)
  t.goto(x - 200, 150 - y)
  t.end_fill()
  t.end_poly()
  t.goto(x - 195, 145 - y)
  t.penup()
screen.onclick(blockoff)

#Defines the function that solves the maze upon right click
def solveMaze(x, y):

  #Disables left click function.

  screen.onclick(None, 1, add=False)
  
  # Start and end points.
  start = (0, 0)
  end = (399, 299)
  
  # Initializes empty maze.
  emptyrow = []
  for i in range(0, 300):
    emptyrow.append(0)
  maze = []
  for i in range(0, 400):
    maze.append(emptyrow[:])

  # Adds all obstacles to pathfinder.
  for i in nogos:
    maze[i[0]][i[1]] = 1
  # The actual A* algorithm.
  result = astar(maze, start, end)
  
  # Draws the path.
  t.pencolor("red")
  t.penup()
  t.goto(result[0][0] - 200, 150 - result[0][1])
  t.pendown()
  for i in result:
    print(str(i[0]) + " " + str(i[1]), end="")
    t.goto(i[0] - 200, 150 - i[1])
screen.onclick(solveMaze, 3)