import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")

# Setting the picture as background
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
score = 0

while len(states_list) > 0:
    answer_state = screen.textinput(title=f"Guess the State  (Guessed: {score}/50)",
                                    prompt="What's another state's name: ")

    if answer_state is None:
        break

    answer_state = answer_state.title().strip()

    # Checking if the state is real
    if answer_state in states_list:
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state, font=("Arial", 9, "bold"))
        states_list.remove(answer_state)
        score += 1

result = turtle.Turtle()
result.hideturtle()
result.penup()
result.goto(-75, 250)
result.write(f"Your score is: {score}", font=("Arial", 20, "bold"))

# States to learn
missing_data = pandas.DataFrame(states_list)
missing_data.to_csv("states_to_learn.csv", index=False)

for state in states_list:
    state_data = data[data.state == state]
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.color("red")
    t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
    t.write(state, font=("Arial", 9, "bold"))
