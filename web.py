import streamlit as st
from backend import get_todos,set_todos

st.title("Welcome to TODO app")
st.subheader("This is a todo app which tracks changes")
st.write("The purpose of this app is to improve productivity")

todos = get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add a todo here")

print("Hello")