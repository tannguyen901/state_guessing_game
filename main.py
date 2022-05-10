import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(height=491, width=725)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states guessed correctly", prompt= "whats another state's name?").title()
    if answer_state.lower() == "exit":
        not_guessed =[]
        for state in all_states:
            if state not in guessed_state:
                not_guessed.append(state)
        df = pandas.DataFrame(not_guessed)
        df.to_csv("not_guessed.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_and_coords = data[data.state == answer_state]
        t.goto(int(state_and_coords.x),int(state_and_coords.y))
        t.write(answer_state)
        if answer_state not in guessed_state:
            guessed_state.append(answer_state)


