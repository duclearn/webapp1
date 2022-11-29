import streamlit as st
import function

data = function.get_data()

def add_todo():
    todo = st.session_state["to_do"]
    data.append(todo + "\n")
    function.write_data(data)


st.title("My Web App")
st.subheader("This is my first Web Application")
st.write("This is improve my activities")

for index, item in enumerate(data):
    checkbox = st.checkbox(item, key=item)
    if checkbox is True:
        data.pop(index)
        function.write_data(data)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label="Type your todo list",
              placeholder="Add todo.....",
              key="to_do", on_change=add_todo)


