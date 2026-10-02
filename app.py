import streamlit as st
import datetime

# Page Configuration
st.set_page_config(page_title="Personal Dashboard", page_icon="⚡", layout="wide")

st.title("⚡ Smart Personal Dashboard")
st.write("Apnar daily task, notes ebong aabahoya ek sthane control korar jonno chotto ekti dashboard.")

# Sidebar - Quick Info
st.sidebar.header("📅 Date & Time")
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.sidebar.write(f"Current Time: {current_time}")

st.sidebar.markdown("---")
st.sidebar.header("🌤️ Weather Widget")
city = st.sidebar.selectbox("Select City", ["Doha", "Dhaka", "London", "New York"])
if city == "Doha":
    st.sidebar.info("Doha: 35°C, Sunny & Clear")
elif city == "Dhaka":
    st.sidebar.info("Dhaka: 29°C, Humid & Rainy")
else:
    st.sidebar.info(f"{city}: 22°C, Pleasant")

# Main Content - Two Columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Daily Task List")
    if 'tasks' not in st.session_state:
        st.session_state.tasks = ["Code review kora", "GitHub repository update kora"]
        
    new_task = st.text_input("Notun task jog korun:")
    if st.button("Add Task"):
        if new_task:
            st.session_state.tasks.append(new_task)
            st.success("Task add kora hoyeche!")
            
    st.write("**Apnar Current Tasks:**")
    for index, task in enumerate(st.session_state.tasks):
        st.write(f"{index + 1}. {task}")

with col2:
    st.subheader("📓 Quick Notes / Thoughts")
    if 'notes' not in st.session_state:
        st.session_state.notes = "Ajker dharona: Digital twin ebong telemetry engine niye aro bhalo kaj korte hobe."
        
    user_note = st.text_area("Apnar moner kotha ba notes ekhane likhun:", value=st.session_state.notes)
    if st.button("Save Note"):
        st.session_state.notes = user_note
        st.success("Note save kora hoyeche!")