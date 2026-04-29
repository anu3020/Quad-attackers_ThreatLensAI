🛡 ThreatLensAI
AI-Powered Cyber Defense & Gmail Threat Detection System


🚀 Overview

ThreatLensAI is an AI-driven cybersecurity platform that detects, analyzes, and predicts cyber threats in real time.
It provides Gmail phishing detection, system monitoring, AI threat prediction, and cloud-based authentication with OTP security.

Designed for hackathons, it simulates a real-world Security Operations Center (SOC) powered by AI.

🎯 Key Features
🔐 Authentication System
Firebase Cloud Database integration
Gmail-only registration/login
SHA-256 password hashing
OTP-based email verification (2FA security)
📧 AI Gmail Threat Detection
Detects phishing emails
Keyword-based threat scoring
Suspicious link detection
Fake sender detection
Threat classification:
✅ Safe
⚠ Suspicious
🚨 Phishing Attack
🤖 AI Threat Prediction
Machine learning model (RandomForest)
Predicts attack risk based on:
Failed login attempts
Network traffic
Real-time security recommendations
🖥 System Monitoring
CPU usage monitoring (psutil)
Memory usage tracking
Disk usage analysis
Live system health dashboard
📊 Security Dashboard
Threat statistics visualization
Attack severity distribution
Real-time updates
Cyber defense metrics
🧠 Tech Stack
Layer	Technology
Frontend	Streamlit
Backend	Python
Database	Firebase Firestore
ML Model	Scikit-learn (RandomForest)
Visualization	Plotly
System Monitoring	Psutil
Email Service	Yagmail
Auth Security	SHA-256 + OTP



🏗 System Architecture
User
 ↓
Streamlit UI
 ↓
Authentication Layer (Firebase + OTP)
 ↓
AI Threat Detection Engine
 ↓
ML Prediction Model
 ↓
Dashboard & Security Reports

⚙ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/ThreatLensAI.git
cd ThreatLensAI
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Setup Firebase
Create Firebase project
Enable Firestore Database
Download firebase_key.json
Place it in project folder
4️⃣ Configure Email OTP

Edit in app.py:

user="YOUR_GMAIL@gmail.com"
password="YOUR_GMAIL_APP_PASSWORD"

👉 Enable Gmail App Password from Google Security settings.

5️⃣ Run Application
streamlit run app.py
🔐 OTP Login Flow
User Login → Validate Credentials → OTP Sent to Gmail → Verify OTP → Access Granted
📧 Email Threat Detection Flow
Paste Email → AI Scan → Keyword Detection → Link Analysis → Risk Score → Final Verdict
📊 Threat Levels
Score	Status
0 - 34	✅ Safe
35 - 69	⚠ Suspicious
70 - 100	🚨 Phishing Attack
🧪 Sample Phishing Email
URGENT!

Your bank account has been suspended.
Click below immediately to verify:
http://fake-login.com

Failure to act will result in permanent suspension.
🏆 Hackathon Highlights

✔ Real-time AI cybersecurity system
✔ Gmail phishing detection
✔ OTP-based authentication (MFA)
✔ Cloud database (Firebase)
✔ Machine learning threat prediction
✔ Live system monitoring dashboard
✔ SOC-style security simulation

🔮 Future Improvements
Gmail API integration (auto email scanning)
Deep learning phishing detection
Browser extension version
Dark web threat intelligence feed
AI chatbot security assistant (LLM-based)
Multi-user admin dashboard
👨‍💻 Author

ThreatLensAI Project
Built for AI Cybersecurity Hackathon 🚀



Application Screenshots:

Login Page
![Login Page](screenshots/login.png)

---

Dashboard
![Dashboard](screenshots/dashboard.png)

---

AI Assistant
![AI Assistant](screenshots/AiAssistant.png)


Threat Prediction
![Threat Prediction](screenshots/ThreatPridition.png)