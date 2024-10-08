#   a116_ladybug.py
import turtle as trtl

legs = 6
move = 60
angle = 90 / legs
print("angle=", angle)
trtl.pensize(5)
counter = 0

# Draw legs
while (counter < legs):
  trtl.goto(0,-30)
  trtl.setheading(angle*counter - 10)
  if counter >= 3:
    trtl.setheading(angle*counter + 115 )
  trtl.forward(move)
  print("angle*counter=", angle*counter)
  counter = counter + 1
trtl.hideturtle()







# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)




# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)


# config dots
num_dots = 0
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots < 2):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1
  
  


ladybug.hideturtle()
ladybug.hideturtle()

wn = ladybug.Screen()
wn.mainloop()

