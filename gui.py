import functions
import PySimpleGUI as sg
import time
import os
from rich import print
from rich.console import Console

if not os.path.exists("todos.txt"):
    # Creating a file
    with open("todos.txt", "w") as file:
        pass


sg.theme("Black")

console = Console(color_system="truecolor", force_terminal=True, force_interactive=True)
print(console.is_terminal)

"""This is where I define my layout contents"""
clock = sg.Text("", key="clock")
label = sg.Text("Add to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", size=10)
# add_button = sg.Button(size=2, image_source="add.png", mouseover_colors="LightBlue2", tooltip="Add Todo", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# For dynamic layout
layout = [  # Each line represent a row in the screen
    [clock],
    [label],
    [input_box, add_button],
    [list_box, edit_button, complete_button],
    [exit_button],
]


"""This is where I call my function to create the screen """
window = sg.Window(
    "My To-Do App",
    layout=layout,
    font=("Helvetica", 15),
)

while True:
    # Display and interact with the Window
    event, values = window.read(timeout=2000)
    window["clock"].update(value=time.strftime(time.strftime("%b %d, %Y %H:%M:%S")))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)  # updating the screen with new values

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]  # looking for the value in the key in this case is from list box
                new_todo = values["todo"] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)  # updating the screen with new values
            except IndexError:
                sg.popup("Please select an item", font=("Helvetica", 15))
                console.print("Please select an item")
        case "Complete":
            try:

                todos_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todos_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item")
                console.print("Please select an item", font=("Helvetica", 15))

        case "Exit":
            break
        case "todos":  # When i click in list box Im calling the event todos and this case will run

            window["todo"].update(value=values["todos"][0])  # adding the value from todos in the input box
            # Using the index number to get just the string inside of the index number
        case sg.WIN_CLOSED:
            break

# Finish up by removing from the screen
window.close()
