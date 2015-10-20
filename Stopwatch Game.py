# template for "Stopwatch: The Game"
import simplegui

# define global variables
value = 0
interval = 100
trys = 0
success_trys = 0
position = [150, 150]
game_position = [300, 50]
time = "0:00.0"
    

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D


def format():
    ''' Creates proper stopwatch time formatting'''
    global value
    if value >600:
        s4 = value // 600
    else:
        s4 = "0"
    if value >100:
        s3 = ((value % 600) // 100)
    else:
        s3 = "0"
    if value >9:
        s2 = ((value % 100) // 10)
    else:
        s2 = "0"
    if value >0:
        s1 = str(value)[-1]
    else:
        s1 = "0"   
    return  str(str(s4) + ":" + str(s3) + str(s2) + "." + s1)

   
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    '''Stops Timer and creates game functionality'''
    global value
    global trys
    global success_trys
    if timer.is_running():
        trys += 1
        if value % 10 == 0:
            success_trys += 1
    timer.stop()
    
           
    
def reset():
    '''Resets and stops timer, resets game score'''
    global trys
    global success_trys
    trys = 0
    success_trys = 0
    timer.stop()
    global value
    value =0
    return value

# define event handler for timer with 0.1 sec interval

def tick():
    global value
    value += 1
    return value
    

# define draw handler
def draw(canvas):
    canvas.draw_text(format(), position, 36, "White")
    canvas.draw_text(str(success_trys) + "/" + str(trys), game_position, 22, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 400, 300)

# register event handlers
frame.set_draw_handler(draw)
start_button = frame.add_button("Start", start, 100)
stop_button = frame.add_button("Stop", stop, 100)
reset_button = frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()

