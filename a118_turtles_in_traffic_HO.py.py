#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "classic", "square", "triangle"]
horiz_colors = ["yellow", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50


# TODO: move turtles across and down screen, stopping for collisions
move = 0
ht.speed(0)
vt.speed(0)
for step in range(50):
   for ht in horiz_turtles:
          ht.forward(move)
          move = move + 1
          for vt in vert_turtles:
            vt.forward(3)
            if (abs(ht.xcor() - vt.xcor()) < 20):
               if (abs(ht.ycor() - vt.ycor()) < 20):
                  #vert_turtles.remove(vt)
                  #horiz_turtles.remove(ht)
                  ht.color("red")
                  vt.color("red")
                  ht.shape("circle")
                  vt.shape("circle")
                  ht.backward(50)
                  vt.backward(50)
                  if (abs(ht.xcor() - vt.xcor()) > 20):
                    if (abs(ht.ycor() - vt.ycor()) > 20):
                      ht.color("red")
                      vt.color("red")
                      new_shape = turtle_shapes.pop()
                      ht.shape(new_shape)
                      vt.shape(new_shape)
                       

                  


   
                  

              
  


wn = trtl.Screen()
wn.mainloop()
