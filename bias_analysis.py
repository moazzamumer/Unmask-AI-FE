import streamlit as st
import requests

st.set_page_config(layout="wide")

# Backend API configuration
API_BASE_URL = "https://unmask-ai-production.up.railway.app"


def bias_analysis():
    """Perform bias analysis based on the AI response."""
    
    # Load required values from session state
    prompt_id = st.session_state.get("prompt_id")
    ai_response = st.session_state.get("ai_response")
    
    # Ensure we have data to analyze
    if not prompt_id or not ai_response:
        st.warning("⚠️ Please complete Step 1 (Prompt Input) first to analyze bias.")
        st.info("Bias analysis requires an AI response to be generated first.")
        return

    # Prepare payload for API
    payload = {
        "prompt_id": prompt_id,
        "ai_response": ai_response
    }

    # Send request to bias-insights endpoint
    response = requests.post(f"{API_BASE_URL}/bias-insights", json=payload)
    
    if response.status_code != 200:
        st.error("❌ Failed to perform bias analysis. Please try again.")
        return

    bias_data = response.json()
    
    # Display results
    if bias_data:
        st.success("✅ The following biases were detected in the AI response:")
        for bias in bias_data:
            st.markdown(f"**{bias['category']} Bias** — Score: `{bias['score']}`")
            st.write(bias["insight_summary"])
            st.markdown("---")
    else:
        st.info("🎯 No significant biases detected in the AI response.")
