import streamlit as st
from streamlit_survey import Survey


survey = Survey("Alina's survey")

# Add questions
name = survey.text_input("What is your name?")
rating = survey.radio("How would you rate our service?", options=["Excellent", "Good", "Average", "Poor"])
comments = survey.text_area("Any additional comments?")


