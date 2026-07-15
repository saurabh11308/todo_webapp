import streamlit as st
from backend import get_todos,set_todos

todos = get_todos()

def add_todo():
    todo_new = st.session_state["new_todo"] + "\n"
    todos.append(todo_new)
    set_todos(todos)

st.title("Welcome to todo app")
st.subheader("This is a todo app which tracks changes")
st.write("The purpose of this app is to improve productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=index)
    if checkbox:
        todos.pop(index)
        set_todos(todos)
        del st.session_state[index]
        st.rerun()

st.text_input(label="",placeholder="Add a todo here",on_change=add_todo,
              key="new_todo")
