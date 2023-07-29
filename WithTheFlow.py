import PySimpleGUI as sg
from main import *
import time
import todo_functions
import os

## If todos.txt file does not exist

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

## Defining the elements of the GUI ##

city = sg.Text(current_city)
temp_c = sg.Text(temp_cel)
temp_f = sg.Text(temp_fer)
nature = sg.Text(weather_condition)
hum = sg.Text(f"HUM: {humidity}", key="hum")
clock = sg.Text(key="clock")
todo_title = sg.Text("Enter TODO")
pomo_time = sg.Text("00:00", font=(40))

input_box = sg.InputText(tooltip="Enter TODO", key="todo", size=(33, 2), pad=((10, 0), (0, 20)), font=("Bahnschrift", 15))
list_box = sg.Listbox(values=todo_functions.get_todos(), key="todos",
                      enable_events=True, size=(47, 10))
# input_box_pomo = sg.InputText(tooltip="Enter Work time", key="pomo_time", size=(5), pad=((0, 0), (0, 200)))
# input_box_pomo_break = sg.InputText(tooltip="Enter Break time", key="pomo_break", size=(5), pad=((0, 0), (0, 200)))

add_button = sg.Button("Add", size=(7), pad=((5, 0), (0, 20)))
edit_button = sg.Button("Edit", size=(10), pad=((10, 0), (20, 0)))
complete_button = sg.Button("Complete", size=(10), pad=((5, 0), (20, 0)))
exit_button = sg.Button("EXIT")
pomo_start_button = sg.Button("Start", size=(10), pad=((10, 0), (0, 30)))
pomo_break_button = sg.Button("Break", size=(10), pad=((10, 0), (0, 30)))

top_row = ["TASK", "START TIME", "END TIME"]
rows = [["Easting", "10PM", "10:30PM"],
        ["Praying", "10:45", "11:15PM"],
        ["Sleeping with all the emotion and remembering Almighty", "12AM", "4:25AM"]]
task_table = sg.Table(values=rows, headings=top_row, max_col_width=40, auto_size_columns=True, display_row_numbers=False, justification="center",
                      pad=((10, 0), (0, 15)), expand_x=True, expand_y=True)

gap_element = sg.Text("     ")

## Layout of the GUI ##

temp_section = [[city, sg.Push(), clock],
                [temp_c, temp_f, nature, hum]]

todo = [[todo_title],
        [input_box, add_button],
        [list_box],
        [edit_button, complete_button]]

pomodoro = [[pomo_start_button, pomo_break_button],
            [task_table],
            ]

layout = [[temp_section],
          [sg.HSeparator()],
          [sg.Column(todo), sg.VSeparator(), sg.Column(pomodoro)],
          [sg.HSeparator(pad=((0,0),(20,0)))],
          [sg.Push(), exit_button]]

## WINDOW object to run the app ##

window = sg.Window("WITH THE FLOW", layout=layout, size=(1200, 700), element_padding=((10, 10), (5, 0)),
                   font=("Bahnschrift", 12), icon=r"icon.ico")

while True:
    event, values = window.read(timeout=200)
    clock_now = time.strftime("%b %d, %Y    %H:%M:%S")
    window["clock"].update(clock_now)

    if event == "EXIT" or event == sg.WIN_CLOSED:
        break
    elif event == "Add":
        todos = todo_functions.get_todos()
        new_todo = values["todo"].upper() + "\n"
        todos.append(new_todo)
        todo_functions.write_todos(todos)

        window["todos"].update(values=todos)
        window["todo"].update(value="")

    elif event == "Edit":
        try:
            todo_to_edit= values["todos"][0]
            new_todo = values["todo"] + "\n"

            todos = todo_functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo.upper()
            todo_functions.write_todos(todos)

            window["todos"].update(values=todos)
        except IndexError:
            sg.popup("Please select any TODO", font=("Bahnschrift", 14), title="Warning")

    elif event == "Complete":
        try:
            todo_to_complete = values["todos"][0]
            todos = todo_functions.get_todos()
            todos.remove(todo_to_complete)

            todo_functions.write_todos(todos)

            window["todos"].update(values=todos)
            window["todo"].update(value="")
        except IndexError:
            sg.popup("Please select any TODO", font=("Bahnschrift", 14), title="Warning")

    elif event == "Exit":
        break

    elif event == "todos":
        try:
            window["todo"].update(value=values["todos"][0])
        except IndexError:
            sg.popup("Nothing to select", font=("Bahnschrift", 14), title="Warning")