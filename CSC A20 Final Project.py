#This project was inspired by a person named "teclado" on Youtube. The project is named: "Snake game with python pygame. The youtube video link to is: https://www.youtube.com/watch?v=BPyGdbo8xxk&t=1218s
#This part of the program, I am importing the pygame module on replit, my colours python file in the same directory, random integer module for randomizing the spawn point of the food (yellow square), and importing the "Quit" module for the game to force-quit when it reaches a certain parameter.
#FOR USE IN REPLIT.COM, WE IMPORT THE MODULES IN THE FOLLOWING WAY:
#-import pygame, sys | import colours | from random import randint | from pygame.locals import QUIT | import curses
#FOR USE IN OTHER PYTHON APPS, WE IMPORT THE MODULES IN THE FOLLOWING WAY:
#-import pygame | import colours | from random import randint
#PLEASE USE REPLIT FOR THE BEST AND MOST SMOOTH EXPERIENCE. PROJECT WAS MADE ON REPLIT ORIGINALLY.
import pygame, sys
import colours
from random import randint
from pygame.locals import QUIT
import curses
#Initializing the height and width of the game-window, and initializing the (square) size which is used to create the snake and food to 20, so its easier to reference to later.
window_height = 1100
window_width = 1100
window_dimensions = window_width , window_height
segment_size = 20
#need to initialize the arrow key-pads by
screen = curses.initscr()
screen.keypad(1)
#Initializing a dictionary called (KEY MAP), which will contain the up,down,right,left arrow keys as reference to be used later.
#This part will need to initialize the pygame function and call it.
pygame.init()
#Setting the display message at the top of the application to be "Snake", and not some random text/word.
pygame.display.set_caption("Snake")
#Will need to initialize the clock builtin module in pygame, which will be used for managing the speed of the game (i.e. how fast/slow your snake moves).
clock=pygame.time.Clock()
screen=pygame.display.set_mode(window_dimensions)
#Will need to draw the snake and food with different square blocks. The snake will be multiple square blocks attached to each other, and the food will be 1 square block. Different colours. the draw_objects function will allow this to happen, by using the "segment_size" variable which was set to 20 to make it easier to reference to the pixel size.
def draw_objects(snake_positions, food_position):
  pygame.draw.rect(screen, colours.Food, [food_position, (segment_size,segment_size)])
  for x, y in snake_positions:
    pygame.draw.rect(screen, colours.Snake, [x,y,segment_size,segment_size])
#Will need to write a function which spawns a random pixel of food on the game map, which is NOT ON the snake, by using the imported "randint" module to randomize the x and y position of the food from x = (0,50) and y = (2,48) multiplied by the segment size to adjust to the size of the game window.
def set_new_food_position(snake_positions):
  while True:
    x_position = randint(0,10) * segment_size
    y_position = randint(2,8) * segment_size
    food_position = (x_position,y_position)

    if food_position not in snake_positions:
      return food_position
#Will need to make a function which will "move" the snake, basically it will "move" by (adding) and (subtracting) square blocks from the tail and body, to make it a (in-motion) snake, if that makes sense. when the food gets eaten, it will add/subtract from a higher value, which will make it a percieved (longer) snake, and hence harder to control the bigger you become.
def move_snake(snake_positions, direction):
  arrow_key = curses.initscr().getch()
  head_x_position, head_y_position = snake_positions[0]
  if arrow_key == curses.KEY_UP:
    print("Up")
    new_head_position = (head_x_position, head_y_position - segment_size)
  elif arrow_key == curses.KEY_DOWN:
    print("Down")
    new_head_position = (head_x_position, head_y_position + segment_size)
  elif arrow_key == curses.KEY_RIGHT:
    print("Right")
    new_head_position = (head_x_position + segment_size, head_y_position)
  elif arrow_key == curses.KEY_LEFT:
    print("Left")
    new_head_position = (head_x_position - segment_size, head_y_position)
  else:
    print("Not an arrow key")
  snake_positions.insert(0, new_head_position)
  del snake_positions[-1]
#the check_collision function will basically be the main game function, and how the game will progress and be played. I explained how this function works in the last text paragraph above ^.
def check_collisions(snake_positions):
  head_x_position,head_y_position = snake_positions[0]
  return(head_x_position in (-20, window_width) or
         head_y_position in (20,window_height) or
        (head_x_position,head_y_position) in snake_positions[1:])
#the check_food_collision will basically check if the "snake" is hitting/colliding with the food pixel square, and if it does, it adds another pixel to the snake from the tail, making it longer and progressing in the game.
def check_food_collision(snake_positions, food_position):
  if snake_positions[0]==food_position:
    snake_positions.append(snake_positions[-1])

    return True
 
#The "play_game" function will be our holistic and main function which will make the game run, count the score, set the font and colours for the game, and also terminate/quit the game whenever a certain parameter/error is reached.
def play_game():
  score=0
  current_direction="Right"
  snake_positions = [(100,100), (80,100), (60,100)]
  food_position = set_new_food_position(snake_positions)
#initialize a nested while/for loop which will make sure the game executes on run and starts, while the user is pressing a key from the initialized key dictionary.
  while True:
      for event in pygame.event.get():
          if event.type == QUIT:
              return
          elif event.type == pygame.KEYDOWN:
            current_direction=on_key_press(event,current_direction)
#Need to set the colour for the game app background, font size and colour for font, and positioning of the text "Score" counter.    
      screen.fill(colours.Background)
      draw_objects(snake_positions, food_position)

      font = pygame.font.Font(None, 28)
      text = font.render(f"Score: {score}", True, colours.Text)
      screen.blit(text,(10,10))
      #need to continuously keep updating the background of the game, pygame.display.update command will do the following.
      pygame.display.update()
      move_snake(snake_positions, current_direction)
      if check_collisions(snake_positions):
        return
      if check_food_collision(snake_positions, food_position):
        food_position = set_new_food_position(snake_positions)
        score+=1
      #the clock.tick command will set the pace of the game and the movement speed of the snake. can be readjusted to any number. higher = more challenging.
      clock.tick(10)
#need to call the play_game function so the game executes on "Run"
play_game()