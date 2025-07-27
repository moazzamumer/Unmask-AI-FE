import streamlit as st
import requests

# Backend API configuration
API_BASE_URL = "https://unmask-ai-production.up.railway.app"


def human_override():
    """Allow users to provide their own human-corrected response."""
    
    prompt_id = st.session_state.get("prompt_id")
    ai_response = st.session_state.get("ai_response")

    if not prompt_id:
        st.warning("⚠️ Please complete Step 1 (Prompt Input) before submitting a human override.")
        st.info("An AI response is required to offer corrections or improvements.")
        return

    st.write("✍️ **Submit Your Human Override**")
    st.caption(" ### Improve or correct the AI's response using your own words and reasoning.")

    # Show AI response as context
    if ai_response:
        with st.expander("📄 Original AI Response (for reference)", expanded=False):
            st.write(ai_response)

    # Human override input
    human_text = st.text_area(
        label="Your human-corrected version:",
        height=150,
        placeholder="Write your improved or corrected version of the AI response here..."
    )

    # Optional justification
    justification = st.text_input(
        label="Justification (optional):",
        placeholder="Explain why your version is better..."
    )

    # Submit override
    if st.button("✅ Submit Correction", type="primary") and human_text:
        with st.spinner("Submitting your override..."):
            payload = {
                "prompt_id": prompt_id,
                "human_response": human_text,
                "justification": justification or ""
            }

            response = requests.post(f"{API_BASE_URL}/human-overrides", json=payload)

            if response.status_code == 200:
                st.success("🎉 Human override submitted successfully!")
                st.info("Thank you for contributing to making AI more fair and accurate.")
            else:
                st.error("❌ Failed to submit your override. Please try again.")

    # Guidance for users
    with st.expander("📚 Guidelines for Writing Good Overrides", expanded=False):
        st.markdown("""
        **When should you override the AI?**
        - The response contains **factual errors**
        - It's **biased**, incomplete, or unclear
        - The tone is inappropriate or dismissive
        - Important **perspectives or facts** are missing

        **Tips for writing great corrections:**
        - Be clear and specific
        - Use respectful tone and accurate information
        - Explain your reasoning if possible
        """)
