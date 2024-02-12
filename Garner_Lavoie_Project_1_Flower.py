import turtle 

wn = turtle.Screen()    
wn.bgcolor("black")
turtle.hideturtle()

t=turtle.Turtle()
t.speed(0)

colours =["yellow","red","orange","yellow","red","orange"]

for i in range(50):
   for c in colours:
      t.color(c)
      t.circle(200-i,100)
      t.left(90)
      t.circle(200-i,100)
      t.right(60)
      t.end_fill()

wn.exitonclick()

