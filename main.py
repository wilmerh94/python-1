"""Learning."""
from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S", time.gmtime())
print(now)
todos = []


while True:
    # Get user input and strip space chars from it
    user_Action = input("Type add, show, edit, complete or exit: ")
    user_Action = user_Action.strip()

    if user_Action.startswith("add"):
        todo = user_Action[4:]  # Getting the value starting from index 4
        todos = get_todos()  # Reading the file
        todos.append(todo + "\n")  # Adding todo to the list
        write_todos(todos, "todos.txt")  # Writing the file

    elif user_Action.startswith("show"):
        todos = get_todos()
        if todos is None:
            print("Todo list is empty")
        else:
            # 3rd Option to remove something from list
            for index, item in enumerate(todos):  # enumerate help to have a count from 0 for the index
                item = item.strip("\n")
                print(f"{index+1}-{item}")

        """Learning more
            1st Option to remove something from list
            new_todos=[]
            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)

                2nd Option to remove something from list
                It wil iterate over for in first and then every item will be without '\n'
                List comprehension
                new_todos =[item.strip('\n') for item in todos]
                for index, item in enumerate(new_todos):
                """
    elif user_Action.startswith("edit"):
        try:
            number = int(user_Action[5:]) - 1

            todos = get_todos()  # Reading the file
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"  # Over writing the value of the key by new value

            write_todos(todos, "todos.txt")  # Writing the file

            for index, item in enumerate(todos):  # New options updated
                item = item.strip("\n")  # Strip will remove things
                print(f"{index+1}-{item}")

        except ValueError:  # In case of try failed getting number
            print("Your command is not valid")
            continue  # Continue will send me back to the beginning

    elif user_Action.startswith("complete"):
        try:
            number_index = int(user_Action[9:]) - 1

            todos = get_todos()
            todo_to_remove = todos[number_index].strip("\n")  # Strip will remove things
            todos.pop(number_index)  # Delete from the list by index number

            write_todos(todos, "todos.txt")  # Writing the file
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        except IndexError:  # Case the index number is not valid
            print("There is not item with that number")
            continue

    elif user_Action.startswith("exit"):
        break  # Get out of the loop

    else:  # None of the above conditions match
        print("Command is not valid")

print("Bye!")
