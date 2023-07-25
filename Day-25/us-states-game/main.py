import turtle
import pandas

# read csv file using pandas
states = pandas.read_csv("50_states.csv")
# create screen
screen = turtle.Screen()
screen.title("U.S Game")
image = "blank_states_img.gif"
# display the image on screeen
screen.addshape(image)
turtle.shape(image)

game_is_on = True
states_list = states.state.to_list()
print(states_list)
guessed_states = []
no_of_state = 0
while game_is_on:
    # ask for input
    answer_state = screen.textinput(title=f"Guess the state{no_of_state}/50",
                                     prompt="What's another states name?").title()
    # check if answer state is in the 50 states
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        missed_states = pandas.DataFrame(missing_states)
        missed_states.to_csv("missed_states.txt")
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        current_state = states[states["state"] == answer_state]
        t.goto(int(current_state.x), int(current_state.y))
        t.write(arg=f"{answer_state}")
        no_of_state += 1
    if no_of_state == 50:
        t.goto(0, 0)
        t.write(arg="You Win")
        game_is_on = False

screen.exitonclick()