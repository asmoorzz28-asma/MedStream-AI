# MedStream AI — Interactive Healthcare Support and FAQ Chatbot

A beginner-friendly Python + Streamlit project for a college mini-project/demo.

## Features
- Chat-style interface
- Built-in healthcare FAQ section
- Rule-based answers for common health information topics
- Emergency keyword handling with a reminder to contact emergency services
- Sidebar navigation and clear-chat button
- Project overview, objectives, limitations, and future enhancements

## Requirements
- Python 3.10 or newer
- Internet connection only for installing Streamlit

## Run on Windows
1. Extract the ZIP file.
2. Open Command Prompt or the VS Code terminal inside the `medstream_ai` folder.
3. Create a virtual environment (recommended):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

4. Install packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the app:

   ```bash
   streamlit run app.py
   ```

6. Streamlit will show a local URL, usually `http://localhost:8501`. Open it in your browser.

## Project structure
```text
medstream_ai/
├── app.py
├── requirements.txt
└── README.md
```

## Important safety note
This is an educational prototype, not a medical device or clinical decision-support system. It does not diagnose, prescribe, or replace a qualified healthcare professional. Emergency handling is keyword-based and can miss urgent situations. Never rely on this demo for emergencies; contact local emergency services. In India, 112 is the national emergency number.

## Academic extension ideas
- Replace keyword rules with a curated, clinician-reviewed FAQ dataset.
- Add source links for each FAQ answer.
- Add multilingual support.
- Add privacy review and consent before collecting any user information.
- If connecting an AI model, add retrieval from reviewed sources, safety evaluation, and clear limitations.
