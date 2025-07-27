import streamlit as st
import prompt_input
import bias_analysis
import cross_exam
import reframe_perspective
import human_override
import report, requests

st.set_page_config(page_title="Unmask AI", layout="wide")

# Backend API configuration
API_BASE_URL = "https://unmask-ai-production.up.railway.app"

# Session management

def load_session_id():
    """Call backend to create and return a new session ID."""
    payload = {"model_used": "gpt-4o", "domain": "fashion"}
    response = requests.post(f"{API_BASE_URL}/sessions", json=payload)
    if response.status_code == 404 and "session" in response.text.lower():
        st.warning("Your session expired or is invalid. Starting a new one...")
        st.session_state.session_id = load_session_id()
        st.rerun()
    if response.status_code == 200:
        return response.json()["id"]
    raise RuntimeError("Failed to create new session.")

if "session_id" not in st.session_state:
    st.session_state.session_id = load_session_id()

# Initialize other session variables
if "prompt_id" not in st.session_state:
    st.session_state.prompt_id = None
if "ai_response" not in st.session_state:
    st.session_state.ai_response = None
if "prompt_text" not in st.session_state:
    st.session_state.prompt_text = None

# Step management
if "step" not in st.session_state:
    st.session_state.step = 1

# Display centered app title
st.markdown("<h1 style='text-align: center;'>🤖 Unmask AI</h1>", unsafe_allow_html=True)

# Step Navigation Logic
if st.session_state.step == 1:
    prompt_input.prompt_input()

elif st.session_state.step == 2:
    bias_analysis.bias_analysis()

elif st.session_state.step == 3:
    cross_exam.cross_exam()

elif st.session_state.step == 4:
    reframe_perspective.reframe_perspective()

elif st.session_state.step == 5:
    human_override.human_override()

elif st.session_state.step == 6:
    report.session_report()

# Function to check if current step is complete
def can_proceed_to_next_step():
    if st.session_state.step == 1:
        # Step 1: Must have prompt and AI response
        return (st.session_state.prompt_id is not None and 
                st.session_state.ai_response is not None and 
                st.session_state.prompt_text is not None)
    elif st.session_state.step == 2:
        # Step 2: Must have completed step 1 first
        return (st.session_state.prompt_id is not None and 
                st.session_state.ai_response is not None)
    elif st.session_state.step == 3:
        # Step 3: Must have completed previous steps
        return (st.session_state.prompt_id is not None and 
                st.session_state.ai_response is not None)
    elif st.session_state.step == 4:
        # Step 4: Must have completed previous steps
        return (st.session_state.prompt_id is not None and 
                st.session_state.ai_response is not None)
    elif st.session_state.step == 5:
        # Step 5: Must have completed previous steps
        return (st.session_state.prompt_id is not None and 
                st.session_state.ai_response is not None)
    return True

# Navigation buttons
col1, col2, col3 = st.columns([2, 2, 0.5])

with col1:
    if st.session_state.step > 1:
        if st.button("🔄 Finish & Restart", type="primary"):
                st.session_state.clear()
                st.rerun()

with col2:
    # Empty column for spacing
    st.write("")

with col3:
    if st.session_state.step < 6:
        # Dynamic button text based on current step
        next_step_names = {
            1: "➡️ Bias Analysis",
            2: "➡️ Cross Exam", 
            3: "➡️ Reframe Perspective",
            4: "➡️ Human Override",
            5: "➡️ Session Report"
        }
        button_text = next_step_names.get(st.session_state.step, "Continue")
        
        if can_proceed_to_next_step():
            if st.button(button_text, type="primary"):
                st.session_state.step += 1
                st.rerun()
        else:
            st.button(button_text, disabled=True, help="Complete current step to proceed", type="primary")


