from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        self.score=0
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.write(arg=f"Score: {self.score}",move=False,align="center",font=("Arial", 24, "normal"))


    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(arg=f"Score: {self.score}",move=False,align="center",font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align="center",font=("Arial", 24, "normal"))

