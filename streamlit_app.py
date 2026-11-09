import streamlit as st
import streamlit_survey as ss

survey = ss.StreamlitSurvey()

st.title("🎈 Alina's App")

st.markdown(
    "[Streamlit Documentation](https://docs.streamlit.io/)"
)

survey.select_slider(
    "Likert scale:",
    options=[
        "Strongly Disagree",
        "Disagree",
        "Neutral",
        "Agree",
        "Strongly Agree"
    ],
    id="Q2"
)

st.write("Hello, world!")