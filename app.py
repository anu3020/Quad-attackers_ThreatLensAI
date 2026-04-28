import streamlit as st
import pandas as pd
import numpy as np
import random
import sqlite3
import hashlib
import psutil
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
from streamlit_autorefresh import st_autorefresh

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ThreatLensAI",
    page_icon="🛡️",
    layout="wide"
)

# =========================================================
# DATABASE SETUP
# =========================================================

conn = sqlite3.connect(
    "users.db",
    check_same_thread=False
)

c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users(
    name TEXT,
    email TEXT UNIQUE,
    password TEXT
)
""")

conn.commit()

# =========================================================
# PASSWORD HASHING
# =========================================================

def make_hash(password):
    return hashlib.sha256(
        str.encode(password)
    ).hexdigest()

# =========================================================
# ADD USER
# =========================================================

def add_user(name, email, password):

    c.execute(
        "INSERT INTO users(name, email, password) VALUES (?, ?, ?)",
        (name, email, password)
    )

    conn.commit()

# =========================================================
# LOGIN USER
# =========================================================

def login_user(email, password):

    c.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, password)
    )

    data = c.fetchall()

    return data

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3 {
    color: #00FFAA;
}

[data-testid="stSidebar"] {
    background-color: #161B22;
}

div.stButton > button {
    background-color: #00FFAA;
    color: black;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = ""

# =========================================================
# LOGIN / REGISTER PAGE
# =========================================================

if not st.session_state.logged_in:

    st.title("🛡️ ThreatLensAI")
    st.subheader("AI-Driven Cyber Defense Platform")

    menu = ["Login", "Register"]

    choice = st.sidebar.selectbox(
        "Authentication",
        menu
    )

    # =====================================================
    # LOGIN
    # =====================================================

    if choice == "Login":

        st.subheader("🔐 Secure Login")

        email = st.text_input(
            "Gmail Address"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            if "@gmail.com" not in email:

                st.error(
                    "Only Gmail accounts allowed"
                )

            else:

                hashed_password = make_hash(password)

                result = login_user(
                    email,
                    hashed_password
                )

                if result:

                    st.session_state.logged_in = True
                    st.session_state.user = email

                    st.success("Login Successful")

                    st.rerun()

                else:

                    st.error(
                        "Invalid Email or Password"
                    )

    # =====================================================
    # REGISTER
    # =====================================================

    elif choice == "Register":

        st.subheader("📝 Create Account")

        new_name = st.text_input(
            "Full Name"
        )

        new_email = st.text_input(
            "Gmail Address"
        )

        new_password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Register"):

            if "@gmail.com" not in new_email:

                st.error(
                    "Only Gmail accounts allowed"
                )

            elif len(new_password) < 4:

                st.error(
                    "Password should contain at least 4 characters"
                )

            else:

                try:

                    add_user(
                        new_name,
                        new_email,
                        make_hash(new_password)
                    )

                    st.success(
                        "Registration Successful"
                    )

                    st.info(
                        "Go to Login Page"
                    )

                except:

                    st.error(
                        "Account already exists"
                    )

# =========================================================
# MAIN APPLICATION
# =========================================================

else:

    st_autorefresh(
        interval=3000,
        key="refresh"
    )

    # =====================================================
    # SIDEBAR
    # =====================================================

    st.sidebar.title("🛡️ ThreatLensAI")

    st.sidebar.success(
        f"Logged in as: {st.session_state.user}"
    )

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Threat Logs",
            "AI Predictions",
            "AI Assistant",
            "System Monitor",
            "Email Threat Scanner"
        ]
    )

    # =====================================================
    # LOGOUT
    # =====================================================

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.user = ""

        st.rerun()

    # =====================================================
    # DASHBOARD
    # =====================================================

    if page == "Dashboard":

        st.title("🛡️ ThreatLensAI Dashboard")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Threats Detected",
            "128",
            "+12"
        )

        col2.metric(
            "Blocked Attacks",
            "97",
            "+8"
        )

        col3.metric(
            "Risk Level",
            "High"
        )

        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=[
                "Malware",
                "Network Traffic",
                "Suspicious Logins"
            ]
        )

        st.line_chart(chart_data)

        severity_data = pd.DataFrame({
            "Severity": ["High", "Medium", "Low"],
            "Count": [15, 30, 10]
        })

        fig = px.pie(
            severity_data,
            names="Severity",
            values="Count",
            title="Threat Severity Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        attacks = [
            "⚠ Malware Detected",
            "⚠ DDoS Attack Attempt",
            "⚠ Phishing Email Found",
            "⚠ SQL Injection Attempt",
            "⚠ Suspicious Login Attempt"
        ]

        st.error(
            random.choice(attacks)
        )

        st.success(
            "✅ AI Firewall Protection Active"
        )

    # =====================================================
    # THREAT LOGS
    # =====================================================

    elif page == "Threat Logs":

        st.title("📜 Threat Logs")

        data = {
            "IP Address": [
                "192.168.1.2",
                "45.33.21.7",
                "10.0.0.8",
                "172.16.0.4"
            ],

            "Attack Type": [
                "Phishing",
                "Malware",
                "Brute Force",
                "SQL Injection"
            ],

            "Severity": [
                "High",
                "Medium",
                "High",
                "Critical"
            ],

            "Status": [
                "Blocked",
                "Monitoring",
                "Blocked",
                "Blocked"
            ]
        }

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            use_container_width=True
        )

    # =====================================================
    # AI PREDICTIONS
    # =====================================================

    elif page == "AI Predictions":

        st.title("🤖 AI Threat Prediction")

        X = np.array([
            [1, 30],
            [5, 80],
            [2, 20],
            [8, 95],
            [3, 40],
            [9, 99],
            [4, 60]
        ])

        y = [0, 1, 0, 1, 0, 1, 0]

        model = RandomForestClassifier()

        model.fit(X, y)

        failed_logins = st.slider(
            "Failed Login Attempts",
            1,
            10
        )

        traffic = st.slider(
            "Network Traffic",
            1,
            100
        )

        prediction = model.predict([
            [failed_logins, traffic]
        ])

        if prediction[0] == 1:

            st.error(
                "⚠ High Risk Attack Predicted"
            )

            st.warning(
                "Recommendation: Enable firewall lockdown"
            )

        else:

            st.success(
                "✅ System Safe"
            )

    # =====================================================
    # AI ASSISTANT
    # =====================================================

    elif page == "AI Assistant":

        st.title("🤖 AI Security Assistant")

        question = st.text_input(
            "Ask a cybersecurity question"
        )

        if question:

            q = question.lower()

            if "phishing" in q:

                st.success(
                    "Phishing attacks use fake emails or websites to steal information."
                )

            elif "malware" in q:

                st.success(
                    "Malware is malicious software that damages systems."
                )

            elif "ddos" in q:

                st.success(
                    "DDoS attacks flood servers with huge traffic."
                )

            else:

                st.info(
                    "AI Assistant could not fully understand the query."
                )

    # =====================================================
    # SYSTEM MONITOR
    # =====================================================

    elif page == "System Monitor":

        st.title("🖥️ Real-Time System Monitor")

        cpu_usage = psutil.cpu_percent(interval=1)

        memory = psutil.virtual_memory()

        disk = psutil.disk_usage('/')

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "CPU Usage",
            f"{cpu_usage}%"
        )

        col2.metric(
            "Memory Usage",
            f"{memory.percent}%"
        )

        col3.metric(
            "Disk Usage",
            f"{disk.percent}%"
        )

        if cpu_usage > 80:

            st.error(
                "⚠ High CPU usage detected"
            )

        else:

            st.success(
                "✅ System stable"
            )

    # =====================================================
    # EMAIL THREAT SCANNER
    # =====================================================

    elif page == "Email Threat Scanner":

        st.title("📧 AI Gmail Threat Detector")

        st.subheader(
            "Analyze suspicious Gmail messages using AI"
        )

        email_content = st.text_area(
            "Paste Email Content Here",
            height=300
        )

        phishing_keywords = [
            "urgent",
            "verify account",
            "click below",
            "winner",
            "bank account",
            "password expired",
            "claim reward",
            "security alert",
            "update payment",
            "limited time",
            "login immediately",
            "account suspended"
        ]

        suspicious_emails = [
            "@fakebank.com",
            "@secure-login.com",
            "@verify-paypal.com"
        ]

        urgent_words = [
            "immediately",
            "urgent",
            "hurry",
            "verify now",
            "account suspended"
        ]

        if st.button("🔍 Scan Email Threat"):

            if email_content:

                score = 0
                reasons = []

                st.info(
                    "Scanning Gmail content using ThreatLensAI..."
                )

                content = email_content.lower()

                # =========================================
                # PHISHING KEYWORDS
                # =========================================

                for keyword in phishing_keywords:

                    if keyword in content:

                        score += 20

                        reasons.append(
                            f"Suspicious keyword detected: {keyword}"
                        )

                # =========================================
                # LINK DETECTION
                # =========================================

                if "http://" in content:

                    score += 40

                    reasons.append(
                        "Unsafe HTTP link detected"
                    )

                if "https://" in content:

                    score += 20

                    reasons.append(
                        "External link detected"
                    )

                # =========================================
                # FAKE EMAIL DETECTION
                # =========================================

                for fake in suspicious_emails:

                    if fake in content:

                        score += 50

                        reasons.append(
                            f"Fake sender detected: {fake}"
                        )

                # =========================================
                # URGENCY DETECTION
                # =========================================

                for word in urgent_words:

                    if word in content:

                        score += 15

                        reasons.append(
                            f"Urgency phrase detected: {word}"
                        )

                # =========================================
                # FINAL RESULT
                # =========================================

                st.markdown("---")

                if score >= 70:

                    st.error(
                        "🚨 PHISHING ATTEMPT DETECTED"
                    )

                    st.metric(
                        "Threat Score",
                        f"{score}/100"
                    )

                    st.warning(
                        "Recommendation: Do NOT click links or download attachments."
                    )

                elif score >= 35:

                    st.warning(
                        "⚠ SUSPICIOUS EMAIL DETECTED"
                    )

                    st.metric(
                        "Threat Score",
                        f"{score}/100"
                    )

                    st.info(
                        "Recommendation: Verify sender identity before responding."
                    )

                else:

                    st.success(
                        "✅ SAFE EMAIL"
                    )

                    st.metric(
                        "Threat Score",
                        f"{score}/100"
                    )

                    st.info(
                        "No phishing indicators detected."
                    )

                # =========================================
                # ANALYSIS REPORT
                # =========================================

                st.subheader("📋 AI Threat Analysis")

                if reasons:

                    for reason in reasons:

                        st.write(f"• {reason}")

                else:

                    st.write(
                        "No suspicious activity found."
                    )

            else:

                st.error(
                    "Please paste email content."
                )

    # =====================================================
    # FOOTER
    # =====================================================

    st.markdown("---")

    st.caption(
        "ThreatLensAI © 2026 | AI-Driven Cyber Defense Platform"
    )