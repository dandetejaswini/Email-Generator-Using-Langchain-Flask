# Email Generator using LangChain & Flask ✉️🤖

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.0%2B-lightgrey)](https://flask.palletsprojects.com/)
[![LangChain](https://img.shields.io/badge/langchain-0.1%2B-orange)](https://python.langchain.com/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## 📖 Table of Contents
- [✨ Features](#-features)
- [📂 Project Structure](#-project-structure)
- [🚀 Installation](#-installation)
- [⚡ Usage](#-usage)
- [⚙️ Configuration](#️-configuration)
- [🔒 Security](#-security)
- [📄 License](#-license)

## ✨ Features
- AI-powered professional email generation
- Two alternative versions for each request
- Clean, responsive web interface
- Secure API key management
- Easy copy-paste functionality

## 📂 Project Structure
```
EMAIL-GENERATOR-USING-LANGCHAIN/
├── static/
│   └── styles.css        # CSS stylesheet
├── templates/
│   └── index.html        # HTML template
├── app.py               # Main application 
├── demolangchain.py     # LangChain demonstration
└── README.md            # Documentation
```

## 🚀 Installation
1. **Clone repository**
   ```bash
   git clone https://github.com/yourusername/EMAIL-GENERATOR-USING-LANGCHAIN.git
   cd EMAIL-GENERATOR-USING-LANGCHAIN
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install flask langchain-together python-dotenv
   ```

4. **Configure API key**
   - Create `.env` file:
     ```
     TOGETHER_API_KEY=your_api_key_here
     ```

## ⚡ Usage
1. **Run the application**
   ```bash
   python app.py
   ```

2. **Access the web interface**
   Open `http://localhost:5000` in your browser

3. **Generate emails**
   - Enter email purpose
   - Click "Generate Email"
   - Copy responses with the buttons

## ⚙️ Configuration
Modify in `app.py`:
```python
llm = Together(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    temperature=0.7,  # 0-1 (creative to factual)
    max_tokens=1000   # Response length
)
```

## 🔒 Security
- Never commit `.env` file
- Rotate exposed API keys immediately
- Use environment variables for all secrets

## 📄 License
MIT License - See [LICENSE](LICENSE) for details.


