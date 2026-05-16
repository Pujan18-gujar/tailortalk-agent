Copy🤖 TailorTalk Drive Agent — Conversational AI File Search

A conversational AI agent that searches Google Drive files using natural language queries.


🚀 Live Demo
🔗 Try it Live on Streamlit
(Replace this with your actual Streamlit Cloud URL)

📸 Screenshots

(Add a screenshot of the Streamlit app here)


✨ Features

💬 Natural Language Search — Ask questions like "Find my project report from last month"
📁 Google Drive Integration — Search files by name, type, and content
🔐 Service Account Auth — Secure Google Drive API authentication
⚡ Real-time Results — Instant Drive file search results
🌐 Live Deployed — Fully functional on Streamlit Cloud


🛠️ Tech Stack
LayerTechnologiesLanguagePythonAPI FrameworkFastAPIAI / LLMLangChain, Gemini AIFrontendStreamlitIntegrationGoogle Drive APIAuthGoogle Service AccountDeploymentStreamlit Cloud

📁 Project Structure
tailortalk-agent/
├── app.py              # Main Streamlit app
├── agent.py            # LangChain AI agent logic
├── drive_search.py     # Google Drive API integration
├── requirements.txt    # Python dependencies
└── README.md

⚙️ How to Run Locally
Prerequisites

Python 3.x
Google Cloud Console project with Drive API enabled
Service Account credentials JSON file

Setup
bash# Clone the repo
git clone https://github.com/Pujan18-gujar/tailortalk-agent
cd tailortalk-agent

# Install dependencies
pip install -r requirements.txt

# Add your credentials
# Place your service_account.json in the root folder

# Run the app
streamlit run app.py

🔑 Environment Variables
Create a .env file:
GOOGLE_APPLICATION_CREDENTIALS=service_account.json
GEMINI_API_KEY=your_gemini_api_key

👨‍💻 Developer
Pujan Ajit Gujar

🎓 Diploma in Computer Engineering — Vidyavardhini's Bhausaheb Vartak Polytechnic, Vasai
📧 pujangujar18@gmail.com
🔗 LinkedIn
🌐 Portfolio


📌 Note
This project was built as an assignment for TailorTalk Backend Development Internship.

⭐ If you like this project, please give it a star!
