#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
trtl = trtl.Turtle()

# Creating spider body
trtl.pensize(40)
trtl.circle(20)

# Configure spider legs
legs = 8
move = 90
angle = 90 / legs
angle2 = 360 / legs
print("angle=", angle)
trtl.pensize(5)
counter = 0

# Draw legs
while (counter < legs):
  trtl.goto(0,20)
  trtl.setheading(angle*counter)
  if counter >= 4:
    trtl.setheading(angle*counter + 90 )
  trtl.forward(move)
  print("angle*counter=", angle*counter)
  '''
  trtl.forward(y)
  '''
  counter = counter + 1
trtl.hideturtle()
wn = trtl.screen()
wn.mainloop()


