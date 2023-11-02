import streamlit as st
import random

def main(participants, res):
    return f"{res} {participants}"

def game():
    participants = random.choice(["Abhishek", "Srinidhi", "Lucky", "Vinnu"])
    res = "The best fit person you are searching for: "
    return participants, res

st.set_page_config(
    page_title="Random Participant Picker",
    page_icon="🎉",
    layout="centered",
)

st.title("Random Participant Picker")

selected_participant, response = game()
result = main(selected_participant, response)

st.subheader("Who is the lucky one today?")
st.markdown(result)

prompt = st.text_input("Enter your prompt:")
if st.button("Get Result"):
    st.write(result)

