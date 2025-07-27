# 🎭 Unmask AI – Frontend

**Unmask AI** is an interactive bias analysis lab that allows users to explore, interrogate, and reframe AI-generated content. This frontend is built using **Streamlit** and provides a clean, step-by-step interface for analyzing outputs from large language models (LLMs).

> 💡 Powered by GPT-4o and designed for human-first insight, Unmask AI puts you back in control of the narrative.

---

## 📁 Directory Structure

moazzamumer-unmask-ai-fe/
├── README.md # Project documentation
├── main.py # Streamlit app entry point
├── prompt_input.py # Step 1: Prompt input + AI response
├── bias_analysis.py # Step 2: Detect biases in AI response
├── cross_exam.py # Step 3: Cross-examine the AI
├── reframe_perspective.py # Step 4: Generate alternative perspectives
├── human_override.py # Step 5: Submit human-corrected responses
├── report.py # Step 6: Generate PDF session report
└── session_id.txt # Local session tracking (optional)
└── requirementstxt # 

---

## 🚀 Features

- 🔍 Bias detection with category, score, and summary
- 💬 Cross-examination Q&A against AI responses
- 🔁 Reframe outputs through cultural, social, or ideological lenses
- ✍️ Submit human override with justification
- 📄 One-click PDF report of the full session

---

## 🛠️ Installation & Setup

### ✅ Requirements

- Python 3.9+
- [Streamlit](https://streamlit.io)
- `requests` for backend communication

### 📦 Install dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run the app

```bash
streamlit run main.py
```
By default, the frontend communicates with the hosted backend at:


https://unmask-ai-production.up.railway.app
Update the API_BASE_URL in each script if needed.

---

## 💡 How It Works

Each module represents a **step in the investigation**:

1. **prompt_input.py** – Submit a prompt and get AI output  
2. **bias_analysis.py** – Detect and score biases  
3. **cross_exam.py** – Ask follow-up questions  
4. **reframe_perspective.py** – View alternate perspectives  
5. **human_override.py** – Correct or improve the AI's answer  
6. **report.py** – Export your full session to PDF  

---

## ✨ Created for "AI vs H.I." Hackathon by CS Girlies
Unmask AI blurs the line between human instinct and machine reasoning — and makes that line visible to everyone.