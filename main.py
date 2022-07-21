import turtle

#Fenetre du jeu
fenetre = turtle.Screen()
fenetre.bgcolor("black")
fenetre.setup(width=800,height=600)
fenetre.tracer(0)

#Barre joueur 1
barre1 = turtle.Turtle()
barre1.shape("square")
barre1.shapesize(stretch_len=1,stretch_wid=5)
barre1.color("blue")
barre1.penup()
barre1.goto(-350,0)

#Barre joueur 2
barre2 = turtle.Turtle()
barre2.shape("square")
barre2.shapesize(stretch_len=1,stretch_wid=5)
barre2.color("blue")
barre2.penup()
barre2.goto(350,0)

#Balle
balle = turtle.Turtle()
balle.speed(1)
balle.shape("circle")
balle.color("red")
balle.penup()
balle.goto(0,0)
balle.dx = 1
balle.dy = 1

#Score
score1 = 0
score2 = 0
score  = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write(f"Joueur 1: {score1} Joueur 2: {score2}",align="center",font=("Courier",25,"normal"))


#Deplacement de la barre1
def barre1_haut():
    y=barre1.ycor()
    y += 25
    barre1.sety(y)

def barre1_bas():
    y=barre1.ycor()
    y -= 25
    barre1.sety(y)

#Deplacement de la barre2
def barre2_haut():
    y=barre2.ycor()
    y += 25
    barre2.sety(y)

def barre2_bas():
    y=barre2.ycor()
    y -= 25
    barre2.sety(y)
        
#evenements
fenetre.listen()
fenetre.onkeypress(barre1_haut,"z")
fenetre.onkeypress(barre1_bas,"s")
fenetre.onkeypress(barre2_haut,"Up")
fenetre.onkeypress(barre2_bas,"Down")


#Main game loop
while True:
    fenetre.update()

    #Mouvement de la balle
    balle.sety(balle.ycor() +balle.dy)
    balle.setx(balle.xcor() +balle.dx)
    
    #rebond sur les bords de la fenetre
    if balle.ycor() > 290:
        balle.sety(290)
        balle.dy *= -1

    elif balle.ycor() < -290:
        balle.sety(-290)
        balle.dy *= -1
        
    if balle.xcor() > 390:
        balle.goto(0,0)
        balle.dx *= -1
        score1 += 1
        score.clear()
        score.write(f"Joueur 1: {score1} Joueur 2: {score2}",align="center",font=("Courier",25,"normal"))
              
    elif balle.xcor() < -390:
        balle.goto(0,0)
        balle.dx *= -1
        score2 += 1
        score.clear()
        score.write(f"Joueur 1: {score1} Joueur 2: {score2}",align="center",font=("Courier",25,"normal"))
        
    if (balle.xcor() > 340 and balle.xcor() <350) and (balle.ycor() < barre1.ycor() + 40 and  balle.ycor() > barre1.ycor() - 40):
        balle.setx(340)
        balle.dx *= -1
        
    if (balle.xcor() < -340 and balle.xcor() > -350) and (balle.ycor() < barre2.ycor() + 40 and  balle.ycor() > barre2.ycor() - 40):
        balle.setx(-340)
        balle.dx *= -1