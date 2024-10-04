#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
trtl = trtl.Turtle()
trtl.pensize(40)
trtl.circle(20)
legs = 8
move = 90
angle = 380 / legs
print("angle=", angle)
trtl.pensize(5)
counter = 0
while (counter < legs):
  trtl.goto(0,0)
  trtl.setheading(angle*counter)
  trtl.forward(move)
  print("angle*counter=", angle*counter)
  '''
  trtl.forward(y)
  '''
  counter = counter + 1
trtl.hideturtle()
wn = trtl.screen()
wn.mainloop()

