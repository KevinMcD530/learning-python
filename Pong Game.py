# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_vel = [0,0]
ball_pos = [WIDTH / 2, HEIGHT / 2]
score1 = 0
score2 = 0
paddle1_pos = 160
paddle2_pos = 160
paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists 
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == False:
        ball_vel = [-(random.randrange(120, 240)/60.0), -(random.randrange(60, 180)/60.0)]
        return ball_vel
    elif direction == True:
        ball_vel = [(random.randrange(120, 240)/60.0), -(random.randrange(60, 180)/60.0)]
        return ball_vel        

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    spawn_ball(False)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # bounce balll off of top and bottom of screen
    if ball_pos[1] <= BALL_RADIUS  and ball_vel[1]<0:
        ball_vel[1] = - ball_vel[1]

    if ball_pos[1] >= HEIGHT - BALL_RADIUS and ball_vel[1]>0:
        ball_vel[1] = - ball_vel[1]
        
    # Reset ball if it hits a gutter, check if it hits a paddle
              
    
    if ball_pos[0] + ball_vel[0] <= (PAD_WIDTH + BALL_RADIUS):
        if  paddle1_pos <= ball_pos[1] <= (paddle1_pos + PAD_HEIGHT):
            ball_vel[0] = - (ball_vel[0] * 1.10)
        else:
            spawn_ball(True)
            score2 += 1
        
    if ball_pos[0] + ball_vel[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):
        if paddle2_pos <= ball_pos[1] <= (paddle2_pos + PAD_HEIGHT):
            ball_vel[0] = - (ball_vel[0] * 1.10)
        else:
            spawn_ball(False)
            score1 += 1

    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos + paddle1_vel) <= 0:
        paddle1_vel = 0
    elif ((paddle1_pos + PAD_HEIGHT) + paddle1_vel) >= HEIGHT:
        paddle1_vel = 0
    else:
        paddle1_pos += paddle1_vel
    
    if (paddle2_pos + paddle2_vel) <= 0:
        paddle2_vel = 0
    elif ((paddle2_pos + PAD_HEIGHT) + paddle2_vel) >= HEIGHT:
        paddle2_vel = 0
    else:
        paddle2_pos += paddle2_vel
        
    
    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos), (PAD_WIDTH, paddle1_pos), 
                        (PAD_WIDTH, (paddle1_pos + PAD_HEIGHT)), (0, (paddle1_pos + PAD_HEIGHT))],
                        2, 'Green')
    
    canvas.draw_polygon([(WIDTH, paddle2_pos), ((WIDTH - PAD_WIDTH), paddle2_pos), 
                        ((WIDTH - PAD_WIDTH), (paddle2_pos + PAD_HEIGHT)), (WIDTH, (paddle2_pos + PAD_HEIGHT))],
                        2, 'Green')
    
    # determine whether paddle and ball collide

        
    
    # draw scores
    canvas.draw_text(str(score1), (220, 75), 30, 'Red')
    canvas.draw_text(str(score2), (370, 75), 30, 'Red')
        
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel =4
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel += vel
        
    if key==simplegui.KEY_MAP["S"]:
        paddle1_vel += vel
        
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= vel
        
    if key==simplegui.KEY_MAP["W"]:
        paddle1_vel -= vel    
        
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel        
    paddle1_vel = paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Start New Game', new_game, 50)


# start frame
new_game()
frame.start()

