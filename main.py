'''
My first working version of a snake game with the turtle module.
Game is very bare and doesn't have a main menu screen or score board.
Apart from that, everything works as it should. 
Collision with boundaries or snake body resets the game.

github.com/justvinny
'''

import turtle
import time
import random
import sys

# Set constants
DELAY = .05 # Time delay for game loop.
WIDTH = 800 # Screen width
HEIGHT = 800 # Screen height

# Other variables.
body = [] # List for snake's body.
run = True # Game loop condition.

# Make screen.
root = turtle.Screen()
root.title('Snake Game')
root.bgcolor('black')
root.setup(WIDTH, HEIGHT)
root.tracer(0)

# Make snake head.
head = turtle.Turtle()
head.shape('square')
head.color('white')
head.speed(0)
head.pu()
head.direction = 'stop'

# Make snake food.
food = turtle.Turtle()
food.shape('square')
food.color('red')
food.speed(0)
food.pu()
food.goto(0, 100)

'''
Functions for key bindings:
    right() = Right Arrow Key
    left() = Left Arrow Key
    up() = Up Arrow Key
    down() = Down Arrow Key
Also, you're not allowed to change direction the opposite way.
e.g. if head.direction = 'right', you're not allowed to go left.
'''
def right():
    if head.direction != 'left':
        head.direction = 'right'
    
def left():
    if head.direction != 'right':
        head.direction = 'left'
    
def down():
    if head.direction != 'up':
        head.direction = 'down'
    
def up():
    if head.direction != 'down':
        head.direction = 'up'
    
def quit():
    global run
    run = False
    sys.exit()
    
# Snake movement.
def movement():
    x,y = head.pos()
    
    if head.direction == 'right':
        head.setx(x+20)
        
    if head.direction == 'left':
        head.setx(x-20)
        
    if head.direction == 'down':
        head.sety(y-20)
        
    if head.direction == 'up':
        head.sety(y+20)

# Key bindings. 
# onkey(function_call, key)
root.onkey(right, 'Right')
root.onkey(left, 'Left')
root.onkey(down, 'Down')
root.onkey(up, 'Up')
root.onkey(quit, 'q')
root.listen() # Listen for events in the root window.

# Collision with food
def collision():
    global run, body
    
    head_x, head_y = head.pos()
    food_x, food_y = food.pos()
    
    # Collision with food.
    if head_x == food_x and head_y == food_y:
        # If snake eats food, move food to random location. 
        food.goto(random.randrange(-380,380,20), random.randrange(-380,380,20))
        
        # Make a new turtle for snake body.
        new_body = turtle.Turtle()
        new_body.color('white')
        new_body.shape('square')
        new_body.speed(0)
        new_body.pu()
        # Append the new body to the list of bodies.
        body.append(new_body)        
    
    # Collision with screen boundaries.
    if head_x > 380 or head_x < (-380) or head_y > 380 or head_y < (-380):
        for each in body:
            each.clear()
            each.ht()
            del each
        body = []
        head.st()
        head.goto(0,0)
        head.direction = 'stop'
        return
   
   # Collision with body.    
    if len(body) > 0:
        for each in body:
            each_x, each_y = each.pos()
            if head_x == each_x and head_y == each_y:
                for each in body:
                    each.clear()
                    each.ht()
                    del each
                body = []
                head.st()
                head.goto(0,0)
                head.direction = 'stop'
                return
        
# Main Game Loop
def main():
    global run
    while run:
        # Get current position for head.
        head_x, head_y = head.pos()
        # Update screen.
        root.update()
        # Check for collision
        collision()
        
        # If body list is not empty.
        if len(body) > 0:
            for each in range(len(body)-1, 0, -1):
            # Set index -1's position to index -2's. -2's to -3's and so on...
                each_x, each_y = body[each-1].pos()
                body[each].goto(each_x, each_y)
            # Set index 0 turtle to head's position.     
            body[0].goto(head_x, head_y) 
        # Move head to new position depending on head.direction.        
        movement()
        # Delay to slow down loop.
        time.sleep(DELAY)
        
    root.mainloop()
    
if __name__ == '__main__':
    main()
