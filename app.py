import streamlit as st 
st.title("DoItBro")
st.text("Habit-Tracker")
st.sidebar.title("Navigation")

if "habits" not in st.session_state:
    st.session_state.habits=[]

page = st.sidebar.radio(
    "Go To" ,
    [ "Habit Board" , "Dairy", "Water Tracker", "Sleep Tracker", "Study Tracker"]
)
if page =="Habit Board":
    st.header("Habit Board")

    habit=st.text_input("Enter a naw habit")

    if st.button("Add habit"):
        st.session_state.habits.append(habit)

    st.subheader("Your Habit")

    for h in st.session_state.habits:
        st.write("•",h)


elif page =="Dairy":
    st.header("Dairy")
    st.subheader("What's New Today")
elif page =="Water Tracker":
    st.header("How much you Hydrated")
elif page =="Sleep Tracker":
    st.header("Sleep Tracker")
elif page =="Study Tracker":
    st.header("Study Tracker")

