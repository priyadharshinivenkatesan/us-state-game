import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_state=[]
data=pandas.read_csv("50_states.csv")
all_states= data.state.to_list()
while len(guessed_state) <50:
    answer_state=screen.textinput(title=f"{len(guessed_state)}/50 states correct" ,prompt="What's another States name? ").title()
    guessed_state.append(answer_state)
    if answer_state=="Exit":
        missed_state =[state for state in all_states if state not in guessed_state]
        new_data=pandas.DataFrame(missed_state)
        new_data.to_csv("states_to_learn.csv")
        break


    if answer_state in all_states:
        tim=turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data= data[data.state==answer_state]
        tim.goto(int(state_data.x),int(state_data.y))
        tim.write(state_data.state.item())
    # if answer_state!=data.state:
    #     missed_state.append(data.state)
    #     print(missed_state)

screen.exitonclick()