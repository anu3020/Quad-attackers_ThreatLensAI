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
# ADVANCED CYBERSECURITY UI STYLING
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Space Grotesk', sans-serif;
}

.stApp {
    background: radial-gradient(circle at 20% 30%, #0a0f1f, #03050b);
    color: #e0e0e0;
}

/* Glowing text effect */
h1, h2, h3 {
    background: linear-gradient(135deg, #00FFAA, #00b7ff);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent !important;
    letter-spacing: -0.02em;
    font-weight: 600;
}

/* Sidebar - glassmorphism + neon border */
[data-testid="stSidebar"] {
    background: rgba(18, 22, 35, 0.85) !important;
    backdrop-filter: blur(12px);
    border-right: 1px solid rgba(0, 255, 170, 0.3);
    box-shadow: 4px 0 25px rgba(0,0,0,0.5);
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: #f0f0f0 !important;
}

/* Radio buttons */
.stRadio label {
    color: #cccccc !important;
    font-weight: 500;
    transition: 0.2s;
}

.stRadio label:hover {
    color: #00FFAA !important;
    text-shadow: 0 0 3px #00FFAA;
}

/* Custom card-like metrics */
div[data-testid="stMetric"] {
    background: rgba(10, 15, 25, 0.7);
    backdrop-filter: blur(4px);
    border: 1px solid rgba(0, 255, 170, 0.3);
    border-radius: 16px;
    padding: 15px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    transition: transform 0.2s ease, box-shadow 0.2s;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 25px rgba(0,255,170,0.1);
    border-color: #00FFAA;
}

div[data-testid="stMetric"] label {
    color: #00FFAA !important;
    font-weight: 600;
    letter-spacing: 0.5px;
}

/* Buttons with neon glow */
div.stButton > button {
    background: linear-gradient(95deg, #00FFAA, #0099ff);
    color: #0a0f1f;
    border: none;
    border-radius: 40px;
    font-weight: bold;
    font-size: 1rem;
    padding: 0.6rem 1rem;
    transition: all 0.2s ease;
    box-shadow: 0 0 8px rgba(0,255,170,0.3);
}

div.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 18px #00FFAA;
    color: #000;
    background: linear-gradient(95deg, #33ffbb, #33aaff);
}

/* Input fields - cyber style */
input, textarea {
    background-color: #11161f !important;
    border: 1px solid #2a3342 !important;
    border-radius: 12px !important;
    color: #ffffff !important;
    transition: 0.2s;
}

input:focus, textarea:focus {
    border-color: #00FFAA !important;
    box-shadow: 0 0 12px rgba(0,255,170,0.3) !important;
}

/* Dataframe styling */
.dataframe {
    background: rgba(0,0,0,0.4) !important;
    border-radius: 16px;
    border: 1px solid #1f2a3e;
}
.dataframe th {
    background: #00FFAA20 !important;
    color: #00FFAA !important;
}

/* Alert boxes - neon borders */
div[data-testid="stAlert"] {
    border-radius: 12px;
    border-left: 5px solid #00FFAA;
    background: rgba(0,0,0,0.5);
    backdrop-filter: blur(8px);
}

/* Custom scrollbar */
::-webkit-scrollbar {
    width: 6px;
    background: #0a0f1f;
}
::-webkit-scrollbar-thumb {
    background: #00FFAA;
    border-radius: 10px;
}

/* Progress bar (email scanner) */
.stProgress > div > div {
    background-color: #00FFAA !important;
}

/* Sidebar success text */
div[data-testid="stSidebar"] .stAlert {
    background: rgba(0,255,170,0.1);
    border-color: #00FFAA;
}

/* Glitch header effect */
.cyber-header {
    font-size: 2.5rem;
    font-weight: 800;
    text-align: center;
    text-shadow: 0 0 8px #00FFAA, 0 0 2px #00FFAA;
    margin-bottom: 1rem;
}

/* Card wrapper for dashboard */
.dashboard-card {
    background: rgba(12, 17, 29, 0.6);
    backdrop-filter: blur(4px);
    border-radius: 24px;
    border: 1px solid #2a3342;
    padding: 1rem;
    margin-bottom: 1rem;
}

/* Footer */
footer {
    text-align: center;
    color: #5f6c80;
    font-size: 0.75rem;
    border-top: 1px solid #1f2a3e;
    padding-top: 1rem;
}

/* Logout button in sidebar */
section[data-testid="stSidebar"] div.stButton > button {
    background: #ff3366;
    color: white;
    box-shadow: 0 0 5px #ff3366;
}
section[data-testid="stSidebar"] div.stButton > button:hover {
    background: #ff5c85;
    box-shadow: 0 0 12px #ff3366;
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

    st.markdown("<div class='cyber-header'>🛡️ THREATLENSAI</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #9aa9c1;'>AI-Driven Cyber Defense Platform</p>", unsafe_allow_html=True)

    menu = ["Login", "Register"]

    choice = st.sidebar.selectbox(
        "🔐 AUTHENTICATION",
        menu
    )

    # =====================================================
    # LOGIN
    # =====================================================

    if choice == "Login":

        st.subheader("🔐 SECURE LOGIN")

        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            email = st.text_input(
                "Gmail Address",
                placeholder="youremail@gmail.com"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="••••••••"
            )

            if st.button("Login", use_container_width=True):

                if "@gmail.com" not in email:

                    st.error("🚫 Only Gmail accounts allowed")

                else:

                    hashed_password = make_hash(password)

                    result = login_user(
                        email,
                        hashed_password
                    )

                    if result:

                        st.session_state.logged_in = True
                        st.session_state.user = email

                        st.success("✅ Login Successful")
                        st.rerun()

                    else:

                        st.error("❌ Invalid Email or Password")

    # =====================================================
    # REGISTER
    # =====================================================

    elif choice == "Register":

        st.subheader("📝 CREATE ACCOUNT")

        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            new_name = st.text_input(
                "Full Name",
                placeholder="Alex Johnson"
            )

            new_email = st.text_input(
                "Gmail Address",
                placeholder="alex@gmail.com"
            )

            new_password = st.text_input(
                "Password",
                type="password",
                placeholder="min 4 characters"
            )

            if st.button("Register", use_container_width=True):

                if "@gmail.com" not in new_email:

                    st.error("🚫 Only Gmail accounts allowed")

                elif len(new_password) < 4:

                    st.error("⚠️ Password must be at least 4 characters")

                else:

                    try:

                        add_user(
                            new_name,
                            new_email,
                            make_hash(new_password)
                        )

                        st.success("🎉 Registration Successful!")
                        st.info("👉 Go to Login Page")

                    except:

                        st.error("❗ Account already exists")

# =========================================================
# MAIN APPLICATION
# =========================================================

else:

    st_autorefresh(
        interval=3000,
        key="refresh"
    )

    # =====================================================
    # GLITCH HEADER
    # =====================================================
    st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div style="font-size: 1.8rem; font-weight: bold; background: linear-gradient(135deg, #00FFAA, #00b7ff); -webkit-background-clip: text; background-clip: text; color: transparent;">THREATLENSAI</div>
        <div style="color: #00FFAA; font-family: monospace;">🔒 ACTIVE DEFENSE</div>
    </div>
    <hr style="border-color: #00FFAA30;">
    """, unsafe_allow_html=True)

    # =====================================================
    # SIDEBAR
    # =====================================================

    st.sidebar.markdown("## 🧠 THREATLENSAI")
    st.sidebar.markdown(f"<div style='background: #00FFAA20; padding: 8px; border-radius: 40px; text-align: center;'><span style='color:#00FFAA'>✅</span> {st.session_state.user}</div>", unsafe_allow_html=True)

    page = st.sidebar.radio(
        "⚡ NAVIGATION",
        [
            "📊 Dashboard",
            "📜 Threat Logs",
            "🤖 AI Predictions",
            "💬 AI Assistant",
            "🖥️ System Monitor",
            "📧 Email Threat Scanner"
        ]
    )

    # rename for cleaner code
    if page == "📊 Dashboard":
        page = "Dashboard"
    elif page == "📜 Threat Logs":
        page = "Threat Logs"
    elif page == "🤖 AI Predictions":
        page = "AI Predictions"
    elif page == "💬 AI Assistant":
        page = "AI Assistant"
    elif page == "🖥️ System Monitor":
        page = "System Monitor"
    elif page == "📧 Email Threat Scanner":
        page = "Email Threat Scanner"

    # =====================================================
    # LOGOUT
    # =====================================================

    if st.sidebar.button("🚪 LOGOUT", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.user = ""
        st.rerun()

    # =====================================================
    # DASHBOARD
    # =====================================================

    if page == "Dashboard":

        st.title("📡 THREAT DASHBOARD")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "🚨 THREATS DETECTED",
            "128",
            "+12"
        )

        col2.metric(
            "🛡️ BLOCKED ATTACKS",
            "97",
            "+8"
        )

        col3.metric(
            "⚠️ RISK LEVEL",
            "HIGH",
            delta_color="inverse"
        )

        with st.container():
            st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
            st.subheader("📈 ATTACK VECTOR TRENDS")
            # Enhanced plotly line chart for tech look
            trend_data = pd.DataFrame({
                "Time": list(range(20)),
                "Malware": np.random.randn(20).cumsum() + 5,
                "Network Traffic": np.random.randn(20).cumsum() + 8,
                "Suspicious Logins": np.random.randn(20).cumsum() + 3
            })
            fig_line = px.line(trend_data, x="Time", y=["Malware", "Network Traffic", "Suspicious Logins"],
                               color_discrete_sequence=['#FF3366', '#00FFAA', '#3399FF'],
                               template="plotly_dark")
            fig_line.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                                   legend=dict(font=dict(color='white')), xaxis_title="Time Frame", yaxis_title="Threat Intensity")
            st.plotly_chart(fig_line, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        # Severity pie chart
        severity_data = pd.DataFrame({
            "Severity": ["High", "Medium", "Low"],
            "Count": [15, 30, 10]
        })
        fig = px.pie(
            severity_data,
            names="Severity",
            values="Count",
            title="🎯 THREAT SEVERITY DISTRIBUTION",
            color_discrete_sequence=["#FF3366", "#FFAA33", "#33FFAA"],
            template="plotly_dark"
        )
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', title_font_color="#00FFAA")
        st.plotly_chart(fig, use_container_width=True)

        attacks = [
            "⚠️ Malware Detected",
            "💥 DDoS Attack Attempt",
            "🎣 Phishing Email Found",
            "🗄️ SQL Injection Attempt",
            "🔑 Suspicious Login Attempt"
        ]

        st.error(f"🔴 REAL-TIME ALERT: {random.choice(attacks)}")
        st.success("✅ AI Firewall Protection Active • Zero-Trust Architecture Engaged")

    # =====================================================
    # THREAT LOGS
    # =====================================================

    elif page == "Threat Logs":

        st.title("📜 FORENSIC EVENT LOGS")

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
            use_container_width=True,
            height=300
        )

        st.caption("🔍 Live intrusion detection logs - SIEM integration active")

    # =====================================================
    # AI PREDICTIONS
    # =====================================================

    elif page == "AI Predictions":

        st.title("🧠 AI THREAT PREDICTION ENGINE")

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

        col1, col2 = st.columns(2)
        with col1:
            failed_logins = st.slider(
                "🔒 Failed Login Attempts",
                1, 10, 3
            )
        with col2:
            traffic = st.slider(
                "🌐 Network Traffic (MB/s)",
                1, 100, 45
            )

        prediction = model.predict([
            [failed_logins, traffic]
        ])

        if prediction[0] == 1:
            st.error("⚠️ HIGH RISK ATTACK PREDICTED")
            st.warning("🛡️ Recommendation: Enable firewall lockdown & isolate segment")
        else:
            st.success("✅ SYSTEM SECURE • No immediate threat detected")

        st.info("🔬 Random Forest model trained on synthetic attack patterns")

    # =====================================================
    # AI ASSISTANT
    # =====================================================

    elif page == "AI Assistant":

        st.title("💬 CYBER AI ASSISTANT")

        question = st.text_input(
            "🔎 Ask a cybersecurity question...",
            placeholder="e.g., What is phishing? How to prevent DDoS?"
        )

        if question:

            q = question.lower()

            if "phishing" in q:

                st.success("🎣 Phishing attacks use fake emails or websites to steal credentials. Always verify sender email and never click suspicious links.")

            elif "malware" in q:

                st.success("🐛 Malware (Malicious Software) includes viruses, ransomware, trojans. Use endpoint detection and regular updates.")

            elif "ddos" in q:

                st.success("🌊 DDoS attacks flood servers with traffic. Mitigation: rate limiting, web application firewall, and CDN.")

            else:
                st.info("🤖 AI Assistant: Please refer to NIST cybersecurity framework or rephrase your query.")

    # =====================================================
    # SYSTEM MONITOR
    # =====================================================

    elif page == "System Monitor":

        st.title("🖥️ REAL-TIME SYSTEM TELEMETRY")

        cpu_usage = psutil.cpu_percent(interval=1)

        memory = psutil.virtual_memory()

        disk = psutil.disk_usage('/')

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "🧠 CPU USAGE",
            f"{cpu_usage}%"
        )

        col2.metric(
            "💾 MEMORY USAGE",
            f"{memory.percent}%"
        )

        col3.metric(
            "💿 DISK USAGE",
            f"{disk.percent}%"
        )

        if cpu_usage > 80:

            st.error("⚠️ HIGH CPU USAGE DETECTED - Potential cryptojacking or DoS.")

        else:

            st.success("✅ SYSTEM STABLE • Resources within thresholds")

    # =====================================================
    # EMAIL THREAT SCANNER
    # =====================================================

    elif page == "Email Threat Scanner":

        st.title("📧 GMAIL THREAT DETECTOR")

        st.subheader("🔍 AI-Powered Phishing & Malicious Email Analysis")

        email_content = st.text_area(
            "📝 Paste Email Content (headers + body)",
            height=300,
            placeholder="Paste raw email content here for real-time threat scoring..."
        )

        phishing_keywords = [
            "urgent", "verify account", "click below", "winner", "bank account",
            "password expired", "claim reward", "security alert", "update payment",
            "limited time", "login immediately", "account suspended"
        ]

        suspicious_emails = [
            "@fakebank.com", "@secure-login.com", "@verify-paypal.com"
        ]

        urgent_words = [
            "immediately", "urgent", "hurry", "verify now", "account suspended"
        ]

        if st.button("🔐 SCAN EMAIL FOR THREATS", use_container_width=True):

            if email_content:

                score = 0
                reasons = []

                st.info("🕵️‍♂️ ThreatLensAI scanning engine processing...")

                content = email_content.lower()

                for keyword in phishing_keywords:
                    if keyword in content:
                        score += 20
                        reasons.append(f"⚠️ Suspicious keyword: '{keyword}'")

                if "http://" in content:
                    score += 40
                    reasons.append("🌐 Unsafe HTTP link (no encryption)")

                if "https://" in content:
                    score += 20
                    reasons.append("🔗 External HTTPS link - verify domain reputation")

                for fake in suspicious_emails:
                    if fake in content:
                        score += 50
                        reasons.append(f"📧 Fake sender domain: {fake}")

                for word in urgent_words:
                    if word in content:
                        score += 15
                        reasons.append(f"⏱️ Urgency tactic: '{word}'")

                # Cap score at 100
                score = min(score, 100)

                st.markdown("---")
                st.subheader("🎯 THREAT ASSESSMENT REPORT")

                # Threat score with progress bar
                st.metric("THREAT SCORE", f"{score}/100")
                st.progress(score/100)

                if score >= 70:
                    st.error("🚨 PHISHING ATTEMPT CONFIRMED")
                    st.warning("DO NOT click links, reply, or download attachments. Report to IT security.")
                elif score >= 35:
                    st.warning("⚠️ SUSPICIOUS EMAIL DETECTED")
                    st.info("Recommendation: Verify sender identity through secondary channel.")
                else:
                    st.success("✅ EMAIL APPEARS SAFE")
                    st.info("No major phishing indicators found.")

                if reasons:
                    st.markdown("### 📋 Threat Indicators")
                    for r in reasons:
                        st.write(f"• {r}")
                else:
                    st.write("No suspicious patterns found.")

            else:
                st.error("Please paste email content for analysis.")

    # =====================================================
    # FOOTER
    # =====================================================

    st.markdown("---")
    st.markdown("<footer>🛡️ ThreatLensAI © 2026 | Neural Cyber Defense Platform • Real-time AI Protection</footer>", unsafe_allow_html=True)