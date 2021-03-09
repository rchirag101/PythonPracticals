import turtle,math

#set bg color
screen = turtle.Screen()
screen.bgcolor("skyblue")

#create our turtle
tt = turtle.Turtle()
tt.color("black")
tt.shape("turtle")
tt.speed(5)

#draw and fill rectangle
def drawRect(t,width,height,color):
	t.fillcolor(color)
	t.begin_fill()
	t.forward(width);	t.left(90)
	t.forward(height);	t.left(90)
	t.forward(width);	t.left(90)
	t.forward(height);	t.left(90)
	t.end_fill()

def drawTri(t,length,color):
	t.fillcolor(color)
	t.begin_fill()
	t.forward(length);				t.left(135)
	t.forward(length/math.sqrt(2));	t.left(90)
	t.forward(length/math.sqrt(2));	t.left(135)
	t.end_fill()

def drawParalleogram(t,width,height,color):
	t.fillcolor(color)
	t.begin_fill()
	t.left(30);		t.forward(width)
	t.left(60);		t.forward(height)
	t.left(120);	t.forward(width)
	t.left(60);		t.forward(height)
	t.left(90)
	t.end_fill()

#draw and fill front of house
tt.penup()
tt.goto(-150,-120)
tt.pendown()
drawRect(tt,100,110,"blue")

#front door
tt.penup()
tt.goto(-120,-120)
tt.pendown()
drawRect(tt,40,60,"lightgreen")

#front roof
tt.penup()
tt.goto(-150,-10)
tt.pendown()
drawTri(tt,100,"magenta")

#side of house
tt.penup()
tt.goto(-50,-120)
tt.pendown()
drawParalleogram(tt,60,110,"yellow")

#window
tt.penup()
tt.goto(-30,-60)
tt.pendown()
drawRect(tt,20,20,"red")

#side roof
tt.penup()
tt.goto(-50,-10)
tt.pendown()
tt.fillcolor("orange")
tt.begin_fill()
tt.left(30);	tt.forward(60)
tt.left(105);	tt.forward(100/math.sqrt(2))
tt.left(75);	tt.forward(60)
tt.left(105);	tt.forward(100/math.sqrt(2))
tt.left(45)
tt.end_fill()


#bring turtle down to front door
tt.penup()
tt.goto(-100,-150)
tt.left(90)
input()