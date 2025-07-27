import streamlit as st
import requests

# Backend API configuration
API_BASE_URL = "https://unmask-ai-production.up.railway.app"


def reframe_perspective():
    """Allow users to request a reframed perspective from the AI."""
    
    prompt_id = st.session_state.get("prompt_id")
    
    if not prompt_id:
        st.warning("⚠️ Please complete Step 1 (Prompt Input) before reframing perspectives.")
        st.info("This feature requires an initial AI response to be generated.")
        return

    st.write("🧭 **Explore Alternative Perspectives**")
    st.caption(" ### Request the AI to rephrase its response through a different lens or worldview.")
    
    # Input field for perspective
    perspective_input = st.text_input(
        "Enter a new perspective (e.g., political, neutral, conservative, scientific):",
        placeholder="e.g., neutral, progressive, historical"
    )

    # Generate reframed perspective
    if st.button("🎯 Generate Perspective", type="primary") and perspective_input:
        with st.spinner("Generating reframed perspective..."):
            payload = {
                "prompt_id": prompt_id,
                "perspective": perspective_input
            }
            response = requests.post(f"{API_BASE_URL}/perspectives", json=payload)

            if response.status_code == 200:
                data = response.json()
                st.markdown(f"#### Reframed Perspective: *{perspective_input.title()}*")
                st.write(data.get("ai_rephrased_output"))
                st.success(f"✅ Perspective reframed as '{perspective_input}'.")
            else:
                st.error("❌ Failed to fetch reframed perspective. Please try again.")

    # Examples and guidance
    with st.expander("🧠 Perspective Examples", expanded=False):
        st.markdown("""
        **Common types you can try:**

        - **Neutral** – Objective and balanced tone  
        - **Conservative** – Traditional, cautious view  
        - **Progressive** – Reform-oriented, inclusive lens  
        - **Scientific** – Evidence-based and data-driven  
        - **Economic** – Finance, markets, business implications  
        - **Social** – Community impact and cultural lens  
        - **Historical** – Contextualized by past events  
        """)
