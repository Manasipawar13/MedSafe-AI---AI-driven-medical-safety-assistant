import streamlit as st
from ocr_utils import extract_text_from_image
from med_db import find_medicines
from risk_engine import check_interactions

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="MedSafe AI",
    page_icon="💊",
    layout="wide"
)

st.title("💊 MedSafe AI")
st.markdown("### AI-Driven Prescription Safety Assistant")

st.divider()

# -------------------------------
# Session State Initialization
# -------------------------------

if "medicines" not in st.session_state:
    st.session_state.medicines = []

if "interactions" not in st.session_state:
    st.session_state.interactions = []

if "ocr_text" not in st.session_state:
    st.session_state.ocr_text = ""

# -------------------------------
# Tabs Layout
# -------------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💊 Medicine Interaction Checker",
    "📄 Prescription OCR",
    "💬 Symptom & Doubt Solver",
    "⚠ Side-Effect Monitor",
    "🚑 Emergency Risk Predictor"
])

# =========================================================
# TAB 1 — MEDICINE INTERACTION CHECKER
# =========================================================

with tab1:

    st.header("Medicine Interaction Checker")

    user_input = st.text_area(
        "Enter medicine names separated by commas",
        placeholder="Example: paracetamol, ibuprofen"
    )

    if st.button("Check Interactions"):

        if not user_input:
            st.error("Please enter at least one medicine.")
        else:

            meds = [m.strip().lower() for m in user_input.split(",")]

            interactions = check_interactions(meds)

            st.session_state.medicines = meds
            st.session_state.interactions = interactions

            st.subheader("Detected Medicines")

            for m in meds:
                st.success(m.capitalize())

            st.metric("Total Medicines", len(meds))

            st.subheader("Interaction Results")

            if interactions:
                for i in interactions:
                    st.error(i)
            else:
                st.success("No dangerous interactions detected")

# =========================================================
# TAB 2 — PRESCRIPTION OCR
# =========================================================

with tab2:

    st.header("Prescription OCR Scanner")

    uploaded_file = st.file_uploader(
        "Upload prescription image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:

        st.image(uploaded_file, caption="Uploaded Prescription")

        text = extract_text_from_image(uploaded_file)

        st.session_state.ocr_text = text

        st.subheader("Raw OCR Text")

        st.text_area("Extracted Text", text, height=200)

        meds = find_medicines(text)

        st.subheader("Detected Medicines")

        if meds:

            for m in meds:
                st.success(m.capitalize())

            interactions = check_interactions(meds)

            st.subheader("Interaction Analysis")

            if interactions:
                for i in interactions:
                    st.error(i)
            else:
                st.success("No interactions detected")

        else:
            st.warning("No medicines detected in prescription.")

# =========================================================
# TAB 3 — SYMPTOM & DOUBT SOLVER
# =========================================================

with tab3:

    st.header("Symptom & Doubt Solver")

    symptom = st.text_input("Enter your symptom")

    if st.button("Analyze Symptom"):

        if not symptom:
            st.error("Please enter a symptom.")
        else:

            st.success("Basic Advice")

            st.info(
                "For minor symptoms consider common OTC medicines. "
                "Always consult a doctor for proper diagnosis."
            )

            with st.expander("AI Explanation"):
                st.write(
                    "This module provides guidance based on general "
                    "medical knowledge but does not replace professional advice."
                )

# =========================================================
# TAB 4 — SIDE EFFECT MONITOR
# =========================================================

with tab4:

    st.header("Side Effect Monitor")

    medicine_name = st.text_input("Medicine Name")

    side_effect = st.text_area("Describe Side Effect")

    severity = st.selectbox(
        "Severity Level",
        ["Low", "Moderate", "High"]
    )

    if st.button("Log Side Effect"):

        if not medicine_name or not side_effect:
            st.error("Please fill all fields.")
        else:

            st.success("Side effect recorded.")

            st.metric("Severity Level", severity)

            st.warning(
                "If symptoms worsen seek immediate medical help."
            )

# =========================================================
# TAB 5 — EMERGENCY RISK PREDICTOR
# =========================================================

with tab5:

    st.header("Emergency Risk Predictor")

    age = st.number_input("Patient Age", min_value=0, max_value=120)

    heart_rate = st.number_input("Heart Rate")

    blood_pressure = st.number_input("Blood Pressure")

    if st.button("Predict Risk"):

        risk_score = 0

        if heart_rate > 120:
            risk_score += 2

        if blood_pressure > 150:
            risk_score += 2

        if age > 65:
            risk_score += 1

        st.subheader("Risk Assessment")

        if risk_score >= 4:
            st.error("HIGH RISK — Seek emergency care immediately")
        elif risk_score >= 2:
            st.warning("MODERATE RISK — Medical consultation recommended")
        else:
            st.success("LOW RISK")

        st.metric("Risk Score", risk_score)

st.divider()

st.caption("MedSafe AI • AI-Assisted Medical Safety System")