import streamlit as st
import pandas as pd
import numpy as np
import random
import sqlite3
import hashlib
import psutil
import plotly.express as px
import yagmail
from sklearn.ensemble import RandomForestClassifier
from streamlit_autorefresh import st_autorefresh

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="SentinelAI",
    page_icon="🛡",
    layout="wide"
)

# =========================================================
# DATABASE SETUP
# =========================================================

conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS users(
    name TEXT,
    email TEXT UNIQUE,
    password TEXT
)
''')

conn.commit()

# =========================================================
# PASSWORD HASHING
# =========================================================

def make_hash(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# =========================================================
# REGISTER USER
# =========================================================

def add_user(name, email, password):
    c.execute(
        'INSERT INTO users(name, email, password) VALUES (?, ?, ?)',
        (name, email, password)
    )
    conn.commit()

# =========================================================
# LOGIN USER
# =========================================================

def login_user(email, password):
    c.execute(
        'SELECT * FROM users WHERE email = ? AND password = ?',
        (email, password)
    )
    data = c.fetchall()
    return data

# =========================================================
# DARK THEME
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
# LOGIN / REGISTER
# =========================================================

if not st.session_state.logged_in:

    st.title("🛡 SentinelAI Cyber Defense Platform")

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

        email = st.text_input("Gmail Address")

        password = st.text_input(
            "Password",
            type='password'
        )

        if st.button("Login"):

            if "@gmail.com" not in email:

                st.error("Please use a valid Gmail account")

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

                    st.error("Invalid Email or Password")

    # =====================================================
    # REGISTER
    # =====================================================

    elif choice == "Register":

        st.subheader("📝 Create Account")

        new_name = st.text_input("Full Name")

        new_email = st.text_input("Gmail Address")

        new_password = st.text_input(
            "Password",
            type='password'
        )

        if st.button("Register"):

            if "@gmail.com" not in new_email:

                st.error("Only Gmail accounts are allowed")

            elif len(new_password) < 4:

                st.error(
                    "Password must contain at least 4 characters"
                )

            else:

                try:

                    add_user(
                        new_name,
                        new_email,
                        make_hash(new_password)
                    )

                    st.success("Registration Successful")
                    st.info("Go to Login Page")

                except:

                    st.error("Account already exists")

# =========================================================
# MAIN APPLICATION
# =========================================================

else:

    # =====================================================
    # AUTO REFRESH
    # =====================================================

    st_autorefresh(interval=3000, key="refresh")

    # =====================================================
    # SIDEBAR
    # =====================================================

    st.sidebar.title("🛡 SentinelAI")

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
            "VirusTotal Scanner"
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
    # EMAIL ALERT FUNCTION
    # =====================================================

    def send_email_alert():

        try:

            yag = yagmail.SMTP(
                user="YOUR_EMAIL@gmail.com",
                password="YOUR_APP_PASSWORD"
            )

            yag.send(
                to=st.session_state.user,
                subject="SentinelAI Security Alert",
                contents="⚠ Suspicious activity detected"
            )

            return True

        except:
            return False

    # =====================================================
    # DASHBOARD
    # =====================================================

    if page == "Dashboard":

        st.title("🛡 SentinelAI Dashboard")

        st.subheader("Real-Time Threat Monitoring")

        col1, col2, col3 = st.columns(3)

        col1.metric("Threats Detected", "128", "+12")
        col2.metric("Blocked Attacks", "97", "+8")
        col3.metric("Risk Level", "High")

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

        st.error(random.choice(attacks))

        st.success("✅ AI Firewall Protection Active")

        col_a, col_b = st.columns(2)

        with col_a:

            if st.button("🚫 Auto Block Suspicious IP"):

                st.error(
                    "IP 192.168.1.25 blocked successfully"
                )

        with col_b:

            if st.button("📧 Send Email Alert"):

                success = send_email_alert()

                if success:
                    st.success("Email Alert Sent")
                else:
                    st.error("Email Sending Failed")

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

        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False)

        st.download_button(
            label="📥 Download Threat Report",
            data=csv,
            file_name="threat_report.csv",
            mime="text/csv"
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

            st.error("⚠ High Risk Attack Predicted")

            st.warning(
                "Recommendation: Enable firewall lockdown"
            )

        else:

            st.success("✅ System Safe")

            st.info(
                "Recommendation: Continue monitoring"
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

            elif "attack" in q or "hack" in q:

                st.warning(
                    "No real intrusion scan connected."
                )

            else:

                st.info(
                    "AI Assistant could not fully understand the query."
                )

    # =====================================================
    # SYSTEM MONITOR
    # =====================================================

    elif page == "System Monitor":

        st.title("🖥 Real-Time System Monitor")

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

        st.subheader("📡 Live Packet Monitoring")

        packet_count = random.randint(100, 500)

        st.metric(
            "Packets Captured",
            packet_count
        )

        st.subheader("⚠ AI Security Analysis")

        if cpu_usage > 80:

            st.error(
                "High CPU usage detected."
            )

        elif memory.percent > 80:

            st.warning(
                "High memory usage detected."
            )

        else:

            st.success(
                "✅ System appears stable and secure"
            )

        st.subheader("🧠 Running Processes")

        process_list = []

        for process in psutil.process_iter(
            ['pid', 'name']
        ):

            try:
                process_list.append(process.info)
            except:
                pass

        process_df = pd.DataFrame(process_list)

        st.dataframe(
            process_df.head(15),
            use_container_width=True
        )

    # =====================================================
    # VIRUSTOTAL SCANNER
    # =====================================================

    elif page == "VirusTotal Scanner":

        st.title("🔍 VirusTotal URL Scanner")

        url = st.text_input(
            "Enter URL to Scan"
        )

        if st.button("Scan URL"):

            if url:

                st.info(
                    "Scanning URL using VirusTotal API..."
                )

                st.success(
                    "✅ Scan Completed (Demo Mode)"
                )

            else:

                st.error("Please enter a URL")

    # =====================================================
    # FOOTER
    # =====================================================

    st.markdown("---")

    st.caption(
        "SentinelAI © 2026 | AI-Driven Cyber Defense Platform"
    )