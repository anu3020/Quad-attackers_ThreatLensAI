# ThreatLensAI

AI-Powered Cyber Defense & Email Threat Detection System

---

Overview:

ThreatLensAI is an AI-driven cybersecurity platform designed to detect, analyze, and predict cyber threats in real time. The system combines phishing email detection, machine learning threat prediction, OTP-based authentication, and live system monitoring in a single cybersecurity dashboard.

The project demonstrates how Artificial Intelligence can improve modern cyber defense systems and cybersecurity awareness.

---
Key Features:

Secure Authentication System:

* Firebase Firestore cloud database integration
* Gmail-based registration and login
* Secure password hashing using SHA-256
* OTP-based multi-factor authentication


AI Email Threat Detection:

* AI-powered phishing email analysis
* Suspicious keyword detection
* Suspicious link analysis
* Fake sender detection
* Threat scoring and classification

Threat Categories:

* Safe
* Suspicious
* Phishing Attack

Detection Process:

Users can copy email content from Gmail and paste it into the ThreatLensAI scanner for AI-based threat analysis.

---

AI Threat Prediction:

Machine Learning-based cyber threat prediction using RandomForestClassifier.

Prediction Parameters:

* Failed login attempts
* Network traffic behavior
* Suspicious activity analysis

Output:

* Risk prediction
* Security recommendations
* Threat alerts



System Monitoring Dashboard:

* CPU usage monitoring
* RAM usage tracking
* Disk usage analysis
* Live system health dashboard
* Threat analytics visualization



Cybersecurity Dashboard:

* Threat statistics visualization
* Attack severity distribution
* Real-time monitoring updates
* SOC-style cyber defense interface


Tech Stack:

| Layer            | Technology         |
| ---------------- | ------------------ |
| Frontend         | Streamlit          |
| Backend          | Python             |
| Database         | Firebase Firestore |
| Machine Learning | Scikit-learn       |
| Visualization    | Plotly             |
| Monitoring       | Psutil             |
| Email Service    | Yagmail            |
| Authentication   | SHA-256 + OTP      |


System Architecture:

User
↓
Streamlit Dashboard
↓
Authentication Layer
↓
AI Threat Detection Engine
↓
Machine Learning Prediction Model
↓
Security Dashboard & Reports


Installation & Setup:

Clone Repository
Clone the ThreatLensAI repository from GitHub.
Install Dependencies
Install all required Python libraries from the requirements file.


Configure Firebase:

* Create a Firebase project
* Enable Firestore Database
* Download the Firebase Admin SDK JSON file
* Place the file inside the project folder


Configure Gmail OTP Service

* Enable Gmail App Password
* Add your Gmail credentials inside the application configuration


Run Application

Start the Streamlit application to launch the cybersecurity dashboard.
Streamlit run app.py

OTP Authentication Flow

User Login
↓
Credential Verification
↓
OTP Sent to Gmail
↓
OTP Verification
↓
Access Granted



AI Email Threat Detection Flow

Copy Email Content
↓
Paste into ThreatLensAI
↓
AI Threat Scanner
↓
Keyword & Link Analysis
↓
Threat Score Calculation
↓
Threat Classification



Threat Levels:

Threat Score and Status:

0 – 34       : Safe            
35 – 69      : Suspicious      
70 – 100     : Phishing Attack 


Sample Phishing Email

URGENT!

Your bank account has been suspended.
Click below immediately to verify:
[http://fake-login.com](http://fake-login.com)

Failure to act will result in permanent suspension.



Hackathon Highlights

* AI-powered cyber defense platform
* AI phishing email detection
* OTP-based authentication
* Firebase cloud integration
* Machine learning threat prediction
* Real-time monitoring dashboard
* Cyber threat analytics

Future Improvements

* Real-time Gmail API integration
* Automatic inbox monitoring
* Deep learning phishing detection
* Browser extension integration
* AI security chatbot assistant
* Multi-user admin dashboard
* Automated threat quarantine system


Author

ThreatLensAI Team
Built for AI Cybersecurity Hackathon

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