import streamlit as st
import requests

# Backend API configuration
API_BASE_URL = "https://unmask-ai-production.up.railway.app"


def session_report():
    """Download the session bias report as a PDF from the backend."""
    
    st.write("📄 **Generate Session Bias Report**")
    st.caption(" ### Download a comprehensive PDF of all prompts, biases, perspectives, and overrides from this session.")
    
    # Validate session
    session_id = st.session_state.get("session_id")
    if not session_id:
        st.warning("⚠️ No active session found. Please start from Step 1.")
        return

    if not st.session_state.get("prompt_id"):
        st.info("ℹ️ You must complete at least Step 1 (Prompt Input) to generate a report.")
        return

    # Generate report
    if st.button("📥 Download Session PDF Report", type="primary"):
        with st.spinner("Generating your PDF report..."):
            try:
                report_url = f"{API_BASE_URL}/sessions/report?session_id={session_id}&format=pdf"
                response = requests.get(report_url)

                if response.status_code == 200:
                    st.download_button(
                        label="⬇️ Click here to download your report",
                        data=response.content,
                        file_name=f"unmaskai_bias_report_{session_id[:8]}.pdf",
                        mime="application/pdf"
                    )
                    st.success("✅ Report generated successfully!")

                elif response.status_code == 404:
                    st.error("⚠️ No report data found for this session.")
                else:
                    st.error("❌ Failed to generate report. Please try again.")

            except Exception as e:
                st.error(f"🚨 An error occurred while downloading the report:\n\n{str(e)}")

    # Expandable report contents section
    with st.expander("📚 What's included in the report?", expanded=False):
        st.markdown("""
        **Your report includes:**
        - ✅ All prompts and AI responses
        - 🧠 Bias categories, scores, and summaries
        - 💬 Cross-examination Q&A
        - 🌐 Reframed perspectives
        - ✍️ Human overrides and justifications
        - 🕒 Session metadata (model, timestamps, etc.)

        **Format:**  
        - 📄 PDF – professionally formatted and shareable
        """)
