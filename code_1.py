from turtle import Turtle, Screen
import random

def create_turtles(colors, y_axis):
    turtles = []
    for turtle_number in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtle_number])
        new_turtle.goto(x=-230, y=y_axis[turtle_number])
        turtles.append(new_turtle)
    return turtles

def race_turtles(turtles, user_bet):
    is_race_on = True
    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"Tu as gagné ! La tortue {winning_color} a gagné !")
                else:
                    print(f"Tu as perdu ! La tortue {winning_color} a gagné !")
                is_race_on = False
                break  # Sortir de la loop apres qu'une tortue gagne
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

def main():
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Fait ton choix", prompt="""
    Quelle tortue va gagner 
    (black, red, brown, tomato, rosybrown, or silver)?
    Entrez la couleur: """)

    if user_bet is None:
        screen.bye()  # Sortire si l'utilisateur ne rentre rien
        return

    user_bet = user_bet.lower()
    colors = ["black", "red", "brown", "tomato", "rosybrown", "silver"]
    y_axis = [-100, -60, -20, 20, 60, 100]
    all_turtles = create_turtles(colors, y_axis)

    if user_bet:
        race_turtles(all_turtles, user_bet)

    screen.exitonclick()

if __name__ == "__main__":
    main()
