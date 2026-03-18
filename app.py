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
        if habit !="":
            st.session_state.habits.append({
                "name": habit,
                "done": False
            })
        
    st.subheader("Your Habit")

    for i, h in enumerate (st.session_state.habits):
        col1, col2 = st.columns([6,2])
                    
                           # Checkbox 
        with col1:
            done = st.checkbox(h["name"], value=h["done"], key=f"habit{i}")
            h["done"]=done
                        # Delete button
        with col2:
            if st.button("Delete" , key=f"del{i}"):
                st.session_state.habits.pop(i)
                st.rerun()
        

    # 👇 LOOP KE BAAD GRAPH (IMPORTANT 🔥)
    done_count = sum(1 for h in st.session_state.habits if h["done"])
    pending_count = len(st.session_state.habits) - done_count

    st.subheader("Overall Progress")

    st.bar_chart({
        "Done": done_count,
        "Pending": pending_count
    })

elif page =="Dairy":
    st.header("Dairy")
    st.subheader("What's New Today")
elif page =="Water Tracker":
    st.header("How much you Hydrated")
elif page =="Sleep Tracker":
    st.header("Sleep Tracker")
elif page =="Study Tracker":
    st.header("Study Tracker")

