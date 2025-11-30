import turtle

# screen
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

player1_score = 0
player2_score = 0
game_ended = False

# plaer 1 paddle
player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color("white")
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.penup()
player_1.goto(-350, 0)

# player 2 paddle
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("white")
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.penup()
player_2.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

#score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Arial", 18, "normal"))

#movement for apddle
def player_1_up():
    y = player_1.ycor()
    if y < 250:  
        player_1.sety(y + 30)

def player_1_down():
    y = player_1.ycor()
    if y > -250:
        player_1.sety(y - 30)

def player_2_up():
    y = player_2.ycor()
    if y < 250:
        player_2.sety(y + 30)

def player_2_down():
    y = player_2.ycor()
    if y > -250:
        player_2.sety(y - 30)

#keyboard 
screen.listen()
screen.onkeypress(player_1_up, "w")
screen.onkeypress(player_1_down, "s")
screen.onkeypress(player_2_up, "Up")
screen.onkeypress(player_2_down, "Down")

# Update score
def update_score():
    pen.clear()
    pen.goto(0, 260)
    pen.write(f"Player A: {player1_score}  Player B: {player2_score}", align="center", font=("Arial", 18, "normal"))

def move_ball():
    global player1_score, player2_score, game_ended

    if game_ended:
        return

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (player_1.ycor() - 50 < ball.ycor() < player_1.ycor() + 50): # paddle collission
        ball.setx(-340)
        ball.dx *= -1

    if (ball.xcor() > 340 and ball.xcor() < 350) and (player_2.ycor() - 50 < ball.ycor() < player_2.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() > 390: #score player 1
        player1_score += 1
        update_score()
        if player1_score == 10: 
            screen.clear()
            screen.bgcolor('black')
            pen.goto(0, 0)
            pen.color('white')
            pen.write("Player 1 wins", align="center", font=("Arial", 30, "normal"))
            game_ended = True
            return
        
        ball.goto(0, 0)
        ball.dx = -4
        player_1.goto(-350, 0)
        player_2.goto(350, 0)
        screen.update()
        screen.ontimer(move_ball, 1000) # 1000ms delay per round so its fair
        return

    if ball.xcor() < -390: # score player 2
        player2_score += 1
        update_score()
        if player2_score == 10:
            screen.clear()
            screen.bgcolor('black')
            pen.goto(0, 0)
            pen.color('white')
            pen.write("Player 2 wins", align="center", font=("Arial", 30, "normal"))
            game_ended = True
            return
        
        ball.goto(0, 0)
        ball.dx = 4
        player_1.goto(-350, 0)
        player_2.goto(350, 0)
        screen.update()
        screen.ontimer(move_ball, 1000) 
        return
    
    screen.update()
    screen.ontimer(move_ball, 10) # 4 pixel every 10ms


move_ball()
screen.mainloop()
