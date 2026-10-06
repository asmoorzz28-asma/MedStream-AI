import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="MedStream AI | Healthcare Support",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------- Styling ---------------------------------------
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #f5fbff 0%, #eefaf7 100%); }
    .main-title { font-size: 2.45rem; font-weight: 800; color: #123b55; margin-bottom: 0; }
    .subtitle { color: #587184; font-size: 1rem; margin-top: .25rem; }
    .info-card {
        padding: 1rem 1.1rem; border-radius: 16px; background: white;
        border: 1px solid #d9e9ef; box-shadow: 0 4px 16px rgba(22, 76, 99, .05);
        min-height: 115px;
    }
    .info-card h4 { margin: 0 0 .45rem 0; color: #126e75; }
    .info-card p { margin: 0; color: #466171; font-size: .95rem; }
    .warning-box {
        background: #fff4e5; border-left: 5px solid #e59b28;
        padding: .9rem 1rem; border-radius: 8px; color: #68430a;
    }
    .emergency-box {
        background: #fff0f0; border-left: 5px solid #d93636;
        padding: .9rem 1rem; border-radius: 8px; color: #7b1717;
    }
    [data-testid="stChatMessage"] { border-radius: 14px; }
</style>
""", unsafe_allow_html=True)

# ----------------------------- FAQ data --------------------------------------
FAQS = {
    "What is dehydration?": (
        "Dehydration happens when the body loses more fluid than it takes in. "
        "Thirst, dry mouth, and darker-than-usual urine can be signs. Drinking fluids "
        "may help mild dehydration. Seek medical advice for persistent symptoms, and "
        "urgent care for confusion, fainting, or inability to keep fluids down."
    ),
    "How can I maintain good sleep?": (
        "Try keeping a regular sleep and wake time, reducing bright screens before bed, "
        "keeping your room comfortable, and avoiding caffeine late in the day. If sleep "
        "problems continue or affect daily life, speak with a healthcare professional."
    ),
    "What is blood pressure?": (
        "Blood pressure is the force of blood pushing against artery walls. A reading "
        "has two numbers, systolic over diastolic. One reading alone does not always "
        "tell the full story; a healthcare professional can interpret readings in context."
    ),
    "How can I prevent the spread of infections?": (
        "Wash hands regularly, cover coughs and sneezes, improve indoor ventilation, "
        "stay home when unwell when possible, and follow current vaccination and public "
        "health guidance relevant to you."
    ),
    "When should I contact a doctor for a fever?": (
        "The right response depends on age, temperature, duration, and other symptoms. "
        "Contact a clinician if a fever persists, worsens, or comes with concerning "
        "symptoms. For infants, severe weakness, confusion, breathing difficulty, or "
        "other urgent symptoms, seek prompt medical care."
    ),
    "What should I keep in a first-aid kit?": (
        "A basic kit can include adhesive bandages, sterile gauze, medical tape, gloves, "
        "a digital thermometer, saline wound wash, and a small first-aid guide. Check "
        "expiry dates and tailor the kit with a healthcare professional's advice."
    ),
}

EMERGENCY_TERMS = [
    "chest pain", "can't breathe", "cannot breathe", "difficulty breathing",
    "severe bleeding", "unconscious", "stroke", "face drooping",
    "suicidal", "overdose", "seizure", "not breathing"
]

def answer_question(question: str) -> str:
    """Provide cautious general information; this is not a diagnostic system."""
    q = question.lower().strip()

    if any(term in q for term in EMERGENCY_TERMS):
        return (
            "⚠️ **This may be an emergency.** Please contact your local emergency "
            "service now or go to the nearest emergency department. In India, call "
            "**112** for emergency assistance. Do not wait for a chatbot response. "
            "If possible, ask someone nearby to help."
        )

    if any(word in q for word in ["hello", "hi", "hey", "good morning", "good evening"]):
        return (
            "Hello! 👋 I'm MedStream AI, a healthcare information assistant. "
            "I can help with general health FAQs and explain common healthcare terms. "
            "What would you like to know?"
        )

    if any(word in q for word in ["appointment", "book a doctor", "schedule a doctor"]):
        return (
            "I can't book appointments in this demo. Please contact your clinic or use "
            "its official booking service. If your concern is urgent, seek prompt medical care."
        )

    if any(word in q for word in ["medicine", "medication", "tablet", "dosage", "dose"]):
        return (
            "For medicine choice or dosage, please follow the prescription or product label "
            "and confirm with a licensed doctor or pharmacist. I can't recommend a personal "
            "dose or tell you to start, stop, or change a medicine."
        )

    if any(word in q for word in ["diagnose", "do i have", "what disease", "symptoms of"]):
        return (
            "I can't diagnose a condition from a chat. Symptoms can have many causes. "
            "Please describe your concern to a qualified healthcare professional, especially "
            "if symptoms are severe, new, worsening, or persistent."
        )

    if any(word in q for word in ["fever", "temperature"]):
        return FAQS["When should I contact a doctor for a fever?"]

    if any(word in q for word in ["sleep", "insomnia", "tired"]):
        return FAQS["How can I maintain good sleep?"]

    if any(word in q for word in ["blood pressure", "bp"]):
        return FAQS["What is blood pressure?"]

    if any(word in q for word in ["dehydrat", "thirst", "dry mouth"]):
        return FAQS["What is dehydration?"]

    if any(word in q for word in ["infection", "wash hands", "contagious"]):
        return FAQS["How can I prevent the spread of infections?"]

    if any(word in q for word in ["first aid", "first-aid", "bandage"]):
        return FAQS["What should I keep in a first-aid kit?"]

    return (
        "I can share general healthcare information, but I may not have an answer to that "
        "specific question. Try asking about dehydration, sleep, blood pressure, infection "
        "prevention, fever, or first-aid kits. For personal medical advice, contact a "
        "qualified healthcare professional."
    )

# ----------------------------- Sidebar ----------------------------------------
with st.sidebar:
    st.markdown("## 🩺 MedStream AI")
    st.caption("Interactive healthcare support & FAQ chatbot")
    page = st.radio("Navigate", ["Chat Assistant", "Healthcare FAQs", "About Project"])
    st.divider()
    st.markdown("### Quick safety note")
    st.warning(
        "This educational demo does not diagnose, prescribe, or replace a clinician."
    )
    st.markdown("**Emergency in India:** 112")
    if st.button("Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ----------------------------- Main header ------------------------------------
st.markdown('<p class="main-title">MedStream AI</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">A friendly starting point for general healthcare information.</p>',
    unsafe_allow_html=True
)

if page == "Chat Assistant":
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="info-card"><h4>💬 Ask a question</h4><p>Type a general healthcare FAQ in everyday language.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="info-card"><h4>📚 Explore FAQs</h4><p>Use common questions to learn basic health concepts.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="info-card"><h4>🛡️ Stay safe</h4><p>Get clear reminders to seek professional help when needed.</p></div>', unsafe_allow_html=True)

    st.markdown("### Chat with the assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = [{
            "role": "assistant",
            "content": "Hi! I'm MedStream AI. Ask me a general healthcare question, or choose a suggested prompt below."
        }]

    suggested = st.columns(3)
    suggestions = [
        "How can I maintain good sleep?",
        "What is blood pressure?",
        "What should I keep in a first-aid kit?"
    ]
    for col, prompt in zip(suggested, suggestions):
        with col:
            if st.button(prompt, use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": prompt})
                st.session_state.messages.append({"role": "assistant", "content": answer_question(prompt)})
                st.rerun()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_prompt = st.chat_input("Type your healthcare question...")
    if user_prompt:
        st.session_state.messages.append({"role": "user", "content": user_prompt})
        reply = answer_question(user_prompt)
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()

    st.markdown("---")
    st.markdown(
        '<div class="warning-box"><strong>Important:</strong> MedStream AI provides '
        'general educational information only. It is not a medical professional and cannot '
        'diagnose conditions or recommend personal treatment.</div>',
        unsafe_allow_html=True
    )

elif page == "Healthcare FAQs":
    st.markdown("### Frequently Asked Questions")
    st.write("Select a question to view a general educational answer.")
    for question, answer in FAQS.items():
        with st.expander(question):
            st.write(answer)
    st.info("For personal advice, contact a qualified healthcare professional.")

else:
    st.markdown("### Project overview")
    st.write(
        "**MedStream AI** is a student-friendly healthcare support chatbot prototype. "
        "It uses a small rule-based FAQ knowledge base to respond to common questions and "
        "offers safety-oriented guidance for emergency-related keywords."
    )
    st.markdown("#### Objectives")
    st.markdown(
        "- Provide quick access to common healthcare FAQs.\n"
        "- Demonstrate a simple conversational user interface.\n"
        "- Encourage users to seek professional help when appropriate.\n"
        "- Show how Python can be used to build a healthcare information prototype."
    )
    st.markdown("#### Technologies")
    st.markdown("- Python\n- Streamlit\n- Rule-based keyword matching\n- Session state for chat history")
    st.markdown("#### Current limitations")
    st.markdown(
        "- The chatbot does not use a medical database or a trained AI model.\n"
        "- Responses are limited to the built-in FAQ and keyword rules.\n"
        "- It does not store patient records or provide clinical decisions."
    )
    st.markdown("#### Future enhancements")
    st.markdown(
        "- Add a reviewed and sourced healthcare FAQ database.\n"
        "- Add multilingual support and accessibility features.\n"
        "- Connect to a vetted language model with strong safety controls.\n"
        "- Add secure appointment links and privacy-conscious feedback."
    )

st.caption(f"MedStream AI • Student project prototype • {datetime.now().year}")
