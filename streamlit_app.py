import streamlit as st
import streamlit_survey as Survey


survey = Survey.StreamlitSurvey()

st.title("Improving how research compliance information is collected")
st.write("This survey is part of a university module project. We are exploring how an online system could replace the current form-and-email process for collecting government-required research compliance information. It takes about 10 minutes. Participation is voluntary and your answers are confidential. There are no right or wrong answers. Data will be stored securely, used only for this project and reported in summary form. Where applicable, questions will have an 'Other' option. You will also have the opportunity to add additional comments at the end.When you submit this form, it will not automatically collect your details like name and email address unless you provide it yourself.")


Q1 = survey.radio("1. Which institution do you work at?", options=["Imperial College London", "Queen Mary University of London", "Other"], horizontal=True, id="Q1")
if Q1 == "Other":
    Q1_other = survey.text_input("Please specify your institution:", placeholder="Enter your institution here", id="Q1_other")
Q2 = survey.text_input("2. What is your email address?", placeholder="Enter your email here", id="Q2")

Q3 = survey.radio("3. How long have you been involved with the compliance process?", options=["Less than 1 year", "1-3 years", "4-6 years", "More than 6 years"], horizontal=False, id="Q3")

Q4 = survey.radio("4. Which best describes your role?", options=["Research-active academic", "Research office staff member", "Research office manager"], horizontal=False, id="Q4")
if Q4 == "Research-active academic":
    Q5 = survey.select_slider(
        "5. How easy is the current submission process?", options=["Very Difficult", "Difficult", "Neutral", "Easy", "Very Easy"], id="Q5"
    )
else:
    Q6 = survey.radio("6. What activities currently consume the most time?", options=["Sending reminders", "Tracking submissions", "Following up missing information", "Validating submissions", "Producing reports", "Managing spreadsheets", "Other"], horizontal=False, id="Q6")   
    if Q6 == "Other":
        Q6_other = survey.text_input("Please specify other activities:", placeholder="Enter other activities here", id="Q6_other")

