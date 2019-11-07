# a122_catch_a_turtle.py
#-----import statements-----
import turtle as trtl 
import random
import leaderboard as lb



#-----game configuration----
shape = "turtle"
size = 5
color = "blue"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False




#leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter your name: ")



#-----initialize turtle-----
color_list = ("red", "green", "yellow", "blue")
turtle = trtl.Turtle(shape = shape)
turtle.color(color)
turtle.shapesize(size)

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-370, 270)
font_setup=("Arial", 30, "bold")
score_writer.ht()
score_writer.write(score , font=font_setup)
counter =  trtl.Turtle()
counter.penup()
counter.goto(270,270)
counter.hideturtle()



#-----game functions--------
def turtle_clicked(x,y):
    print ("turtle was clicked")
    change_position()
    score_counter()
    change_color()


def change_position():
    turtle.penup()
    turtle.ht()
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(-300,300)
    turtle.goto(new_xpos, new_ypos)
    turtle.st()


def score_counter():
    global score
    score += 1
    print(score)
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    game_over()
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
    
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def game_over():
    turtle.ht()
    counter.goto(200,200)
    wn.bgcolor("red")

def change_color():
    color = random.choice(color_list)
    turtle.color(color)
    

    # manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global turtle

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, turtle, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, turtle, score)


#-----events----------------

turtle.onclick(turtle_clicked)

wn = trtl.Screen()

wn.ontimer(countdown, counter_interval) 
wn.mainloop()
