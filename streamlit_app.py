import streamlit as st
from streamlit_survey import Survey


survey = Survey()

st.title("🎈Alina's app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

survey.select_slider(
    "Likert scale:", options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], id="Q2"
)