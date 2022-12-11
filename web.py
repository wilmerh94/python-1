"""Creating a web"""
#  Frontend for website
import streamlit as st

# Backend
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"  # session_state give me an Object with key and values
    todos.append(todo)  # Updating todo list
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label=" ", placeholder="Add new todo...", on_change=add_todo, key="new_todo")

st.session_state
