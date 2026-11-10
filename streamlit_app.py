import streamlit as st
import streamlit_survey as Survey

if "page" not in st.session_state:
    st.session_state.page = 1


survey = Survey.StreamlitSurvey()

if st.session_state.page == 1:


        st.title("Informal Interactions Survey")
            
        st.markdown("""

        Help us understand how research compliance information is currently collected and managed:

        • Takes around 10 minutes.

        • Responses are confidential.

        • Participation is voluntary.

        Your feedback will help inform the design of a future digital solution.

        """)

        st.success("Ready to begin?")    

        col1, col2, col3 = st.columns([2, 1, 2])

        with col2:
            if st.button("Start Survey"):
                st.session_state.page = 2
                st.rerun()

       

elif st.session_state.page == 2:
    st.header("About you")        
    Q1 = survey.radio("1. Which institution do you work at?", options=["Imperial College London", "Queen Mary University of London", "Other"], horizontal=True, id="Q1", index=None)
    if Q1 == "Other":
        Q1_other = survey.text_input("Please specify your institution:", placeholder="Enter your institution here", id="Q1_other")
    Q2 = survey.text_input("2. What is your email address?", placeholder="Enter your email here", id="Q2")

    Q3 = survey.radio("3. How long have you been involved with the compliance process?", options=["Less than 1 year", "1-3 years", "4-6 years", "More than 6 years"], horizontal=False, id="Q3", index=None)

    Q4 = survey.radio("4. Which best describes your role?", options=["Research-active academic", "Research office staff member", "Research office manager"], horizontal=False, id="Q4", index=None)
    if Q4 is not None:
        if st.button("Next"):
            st.session_state.page = 3
            st.rerun() 


elif st.session_state.page == 3:

     role = st.session_state.role

     if role == "Research-active academic":
        st.header("Research-active academic")
        st.write("You have selected the role of Research-active academic. Please answer the following questions based on your experience in this role.")
        survey.select_slider(
            "5. How easy is the current submission process?",
            options=[
                "Very Difficult",
                "Difficult",
                "Neutral",
                "Easy",
                "Very Easy"
            ],
            id="Q5"
        )

else:

        st.header("Research office staff member / Research office manager")

        Q6 = survey.radio(
            "6. What activities currently consume the most time?",
            options=[
                "Sending reminders",
                "Tracking submissions",
                "Following up missing information",
                "Validating submissions",
                "Producing reports",
                "Managing spreadsheets",
                "Other"
            ],
            id="Q6",
            index=None
        )

        if Q6 == "Other":
            survey.text_input(
                "Please specify other activities:",
                id="Q6_other"
            )

        col1, col2 = st.columns(2)

        with col1:
                if st.button("Back"):
                    st.session_state.page = 2
                    st.rerun()

        with col2:
                if st.button("Next"):
                    st.session_state.page = 4
                    st.rerun()# Add questions specific to Research-active academic here       
