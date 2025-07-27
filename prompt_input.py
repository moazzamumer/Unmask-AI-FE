import streamlit as st
import requests

# Backend API configuration
API_BASE_URL = "https://unmask-ai-production.up.railway.app"


def prompt_input():
    """Allow the user to enter a prompt and fetch the AI response."""
    
    # Input area for user prompt
    user_prompt = st.text_area(
        "Enter your prompt:", 
        height=100, 
        placeholder="Type your question or prompt here..."
    )
    
    print("session id:", st.session_state.session_id)

    # Trigger on submit
    if st.button("Submit Question", type="primary") and user_prompt:
        with st.spinner("Getting AI response..."):
            # Prepare payload
            payload = {
                "session_id": st.session_state.session_id,
                "prompt_text": user_prompt
            }

            # Make request to backend
            response = requests.post(
                f"{API_BASE_URL}/prompts/get-ai-response", 
                json=payload
            )
            
            if response.status_code != 200:
                st.error("❌ Failed to get AI response.")
                return

            # Parse and store response
            response_data = response.json()
            st.session_state.prompt_id = response_data.get("id")
            st.session_state.ai_response = response_data.get("ai_response")
            st.session_state.prompt_text = user_prompt

            print("prompt id:", st.session_state.prompt_id)

            # Display output
            # st.markdown("---")
            # st.markdown("### Your Prompt")
            # st.write(user_prompt)

            st.markdown("### AI Response")
            st.write(st.session_state.ai_response)
            
            st.success("✅ Response generated successfully! You can now proceed to the next step.")
    
    # If previous response exists, show it
    elif st.session_state.get("prompt_text") and st.session_state.get("ai_response"):
        # st.markdown("---")
        # st.markdown("### Your Prompt")
        # st.write(st.session_state.prompt_text)

        st.markdown("### AI Response")
        st.write(st.session_state.ai_response)

        st.success("✅ Response generated successfully!")
