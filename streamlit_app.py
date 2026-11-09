import streamlit as st
import streamlit_survey as Survey


survey = Survey.StreamlitSurvey()

st.title("Page")
st.write("Hello")


survey.radio("Horizontal radio:", options=["Imperial College London", "Queen Mary University of London"], horizontal=True, id="Q1")
survey.text_input("Text input:", placeholder="Enter your answer here", id="Q2")
survey.radio("Vertical radio:", options=["Less than 1 year", "1-3 years", "4-6 years", "More than 6 years"], horizontal=False, id="Q3")
survey.radio("Vertical radio:", options=["Research-active academic", "Research office staff member", "Research office manager"], horizontal=False, id="Q4")
survey.select_slider(
    "How easy is the current submission process?", options=["Very Difficult", "Difficult", "Neutral", "Easy", "Very Easy"], id="Q5"
)



