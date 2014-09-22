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
#   cur.forward(10)
   checkbound()

def right():
   cur.right(90)
#   cur.forward(10)
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
cur.penup()
cur.goto(100,100)
cur.pendown()
pen_status = True
colors = ["black","blue","red","green","purple","yellow","turquoise","orange"]
color = 5

while True:
	code = lirc.nextcode()
	incomming = code[0]
	if incomming == "KEY_SELECT":
		if pen_status == False: pen_status = True; cur.pendown(); print("Pen down")
		else: pen_status = False; cur.penup(); print("Pen up")
	if incomming == "KEY_VOLUMEUP":
		color = color + 1
		if color > 7: color = 0
		cur.color(colors[color],colors[color])
		print("Colour: %s" % colors[color])

	if incomming == "KEY_VOLUMEDOWN":
		color = color - 1
		if color < 0: color = 7
		cur.color(colors[color],colors[color])
		print("Colour: %s" % colors[color])

	if incomming == "KEY_UP":
		up()
	if incomming == "KEY_LEFT":
		left()
	if incomming == "KEY_DOWN":
		down()
	if incomming == "KEY_RIGHT":
		right()
	time.sleep(1)
