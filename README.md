# KanunAI - Nepal Legal Assistant Webapp

## Project Structure

```
kanunai/
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main web interface
├── static/
│   ├── css/
│   │   └── style.css     # Styling (gradient UI)
│   └── js/
│       └── script.js     # Frontend interactivity
└── data/                 
```

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Environment
Create a `.env` file in the root directory:
```
ANTHROPIC_API_KEY=your_api_key_here
FLASK_ENV=development
```

Get your API key from: https://console.anthropic.com/

### 3. Run the App
```bash
python app.py
```

Visit: `http://localhost:5000`


## Currently working on Features

-Clean, modern UI with language toggle (English/Nepali)
-Search input with animated feedback
-Loading states and error handling
-Results display (Answer, Section, Citation)
-Responsive design (mobile-friendly)
-Flask backend scaffold with API ready


## Architecture

```
User Question
    ↓
Frontend (HTML/CSS/JS)
    ↓
Flask API (/api/ask)
    ↓
LegalAssistant.answer_question()
    ├─ Search documents
    ├─ Translate if needed
    └─ Generate explanation
    ↓
Claude API
    ↓
Response back to UI
```

