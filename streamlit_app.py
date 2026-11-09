import streamlit as st
from streamlit_survey import Survey


survey = Survey.StreamlitSurvey()

st.title("Page")
st.write("Hello")

survey.select_slider(
    "Likert scale:", options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], id="Q2"
)


