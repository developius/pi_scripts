import turtle, time, random
import lirc

sockid = lirc.init("myprogram")
print("Ready")

boxsize = 200

def up():
   cur.forward(10)
   checkbound()

def left():
   cur.left(90)
   checkbound()

def right():
   cur.right(90)
   checkbound()

def down():
   cur.backward(10)
   checkbound()

def checkbound():
   global boxsize
   if cur.xcor() > boxsize:
       cur.goto(boxsize, cur.ycor())
   if cur.xcor() < -boxsize:
       cur.goto(-boxsize, cur.ycor())
   if cur.ycor() > boxsize:
       cur.goto(cur.xcor(), boxsize)
   if cur.ycor() < -boxsize:
       cur.goto(cur.xcor(), -boxsize)

cur = turtle.Turtle()
pen_status = True
colors = ["black","blue","red","green","purple","yellow","turquoise","orange"]
color = 5

cur.shape("turtle")
width = 1
cur.width(5)

cur.penup()
cur.color("purple")
turtle.bgcolor("orange")

cur.left(90)
cur.setpos(0,300)
cur.write("Finnian's Magic Wand", False, align="center", font=("Arial",15,"normal"))

cur.left(180)
cur.setpos(0,0)
cur.pendown()
while True:
	incomming = lirc.nextcode()[0]
	if incomming:
#		if incomming == "power": turtle.reset()
		if incomming == "select":
			if pen_status == False: pen_status = True; cur.pendown(); print("Pen down")
			else: pen_status = False; cur.penup(); print("Pen up")

		if incomming == "volumeup":
			color = color + 1
			if color > 7: color = 0
			cur.color(colors[color],colors[color])
			print("Colour: %s" % colors[color])
		if incomming == "volumedown":
			color = color - 1
			if color < 0: color = 7
			cur.color(colors[color],colors[color])
			print("Colour: %s" % colors[color])

		if incomming == "mute":
			if width + 1 <= 5: width = width + 1
			cur.width(width)
			print("Width: %s" % width)

		if incomming == "repeat":
			if width - 1 >= 1: width = width - 1
			cur.width(width)
			print("Width: %s" % width)

		if incomming == "up":
			up()
		if incomming == "left":
			left()
		if incomming == "down":
			down()
		if incomming == "right":
			right()
		time.sleep(1)

