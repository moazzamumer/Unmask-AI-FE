import streamlit as st
import requests

# Backend API configuration
API_BASE_URL = "https://unmask-ai-production.up.railway.app"


def cross_exam():
    """Chat-based follow-up questions interface."""

    print("session id:", st.session_state.session_id)
    print("prompt id:", st.session_state.prompt_id)
    
    prompt_id = st.session_state.get("prompt_id")
    
    if not prompt_id:
        st.warning("⚠️ Please complete the initial prompt first to start asking follow-up questions.")
        st.info("💡 The chat feature requires an initial AI response to be generated.")
        return

    st.write(" ### 💬 **Chat with AI** — Ask follow-up questions for clarification or deeper insights.")

    # Initialize chat history
    if "cross_exam_messages" not in st.session_state:
        st.session_state.cross_exam_messages = []

    # Load previous chat from backend (once)
    if not st.session_state.cross_exam_messages:
        res = requests.get(
            f"{API_BASE_URL}/prompts/get-cross-exams-qa", 
            json={"prompt_id": prompt_id}
        )
        if res.status_code == 200:
            for item in res.json():
                st.session_state.cross_exam_messages.extend([
                    {"role": "user", "content": item["user_question"]},
                    {"role": "assistant", "content": item["ai_response"]}
                ])

    # Display existing messages
    with st.container():
        for msg in st.session_state.cross_exam_messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

    # Chat input box
    if prompt := st.chat_input("Ask a follow-up question..."):
        st.session_state.cross_exam_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Assistant thinking...
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                payload = {"prompt_id": prompt_id, "user_question": prompt}
                response = requests.post(f"{API_BASE_URL}/cross-exams", json=payload)

                if response.status_code == 200:
                    ai_response = response.json().get("ai_response")
                else:
                    ai_response = "❌ Sorry, I couldn't process your question right now. Please try again."
                    st.error(ai_response)

                st.write(ai_response)
                st.session_state.cross_exam_messages.append({"role": "assistant", "content": ai_response})

    # Clear chat button
    if st.session_state.cross_exam_messages:
        if st.button("🗑️ Clear Chat History", type="secondary"):
            st.session_state.cross_exam_messages = []
            st.rerun()
