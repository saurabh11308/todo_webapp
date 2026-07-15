import streamlit as st
from backend import get_todos,set_todos

todos = get_todos()

def add_todo():
    todo_new = st.session_state["new_todo"] + "\n"
    todos.append(todo_new)
    set_todos(todos)

st.title("Welcome to TODO app")
st.subheader("This is a todo app which tracks changes")
st.write("The purpose of this app is to improve productivity")

for index,todo in enumerate(todos):
    st.checkbox(todo,key=index)
    if st.session_state[index] == True:
        print("Hadippa")

st.text_input(label="",placeholder="Add a todo here",on_change=add_todo,
              key="new_todo")

print("Hello")

st.session_state
