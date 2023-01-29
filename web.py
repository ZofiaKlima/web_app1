import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    if todo != "\n":
        todos.append(todo)
        functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("It was created for fun.")

for todo in todos:
    complete = st.checkbox(todo, key=todo)

    if complete:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new todo...",
              key="new_todo", on_change=add_todo)