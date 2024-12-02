# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("Enter your username: ")
shape = "circle"
color = "red"
fill_color = "red"
size = int("2") 
font_setup = ("ariel", 35, "normal")
score = 0
timer = 30
time_up = False
counter_interval = 1000


#-----initialize turtle-----
aim = trtl.Turtle()
aim.pencolor(color)
aim.fillcolor(fill_color)
aim.shape(shape)
aim.shapesize(size, size, size)
aim.penup()
aim.speed(0)

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.right(90)
score_writer.hideturtle()
score_writer.goto(-100,200)
score_writer.color("white")

counter = trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(100,200)
counter.color("white")



#-----game functions--------
def spot(x,y):
    global time_up
    if time_up == False:
        change()
        score_change()
        
    else:
        aim.hideturtle()
        aim.goto(999,999)

if time_up == True:
   aim.hideturtle()
   aim.goto(999,999)

def change():
    xcor = rand.randint(-150, 150)
    ycor = rand.randint(-150, 150)
    aim.penup()
    aim.hideturtle()
    aim.goto(xcor,ycor)
    aim.showturtle()

def score_change():
    score_writer.clear()
    global score
    score += 1

    score_writer.write("Score: " + str(score), font=font_setup)

def countdown():
    global timer, time_up, counter_interval
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up ",  font = font_setup)
        time_up = True
        aim.hideturtle()
        aim.goto(999,999)
        manage_leaderboard()
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)

def manage_leaderboard():
  
  global leaderboard_file_name
  global score
  global spot
  global player_name

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, score_writer, score)
  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, score_writer, score)




#-----events----------------
aim.onclick(spot)
wn = trtl.Screen()
wn.bgcolor("black")
wn.ontimer(countdown, counter_interval)
wn.mainloop()