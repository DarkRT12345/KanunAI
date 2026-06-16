# KanunAI - Nepal Legal Assistant Webapp

Your Flask + HTML/CSS/JS webapp is ready! Here's what's been created:

## Project Structure

```
kanunai/
├── app.py                 # Flask backend (main app logic)
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main web interface
├── static/
│   ├── css/
│   │   └── style.css     # Styling (gradient UI)
│   └── js/
│       └── script.js     # Frontend interactivity
└── data/                 # (Create this folder for PDFs)
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

## What's Next?

### Step 1: Download & Extract PDFs
- Download the 5 acts from: https://lawcommission.gov.np/pages/alphabetical-index-of-acts/
- Save them in a `data/pdfs/` folder

### Step 2: Extract Text from Nepali PDFs
Script needed to:
- Extract text from PDFs using `pdfplumber`
- Parse into sections
- Store in searchable format

### Step 3: Implement Search
- Vector embeddings or keyword search
- Integration with document storage

### Step 4: Integrate Claude API
- Translate Nepali → English
- Generate explanations
- Handle citations

## Current Features

✅ Clean, modern UI with language toggle (English/Nepali)
✅ Search input with animated feedback
✅ Loading states and error handling
✅ Results display (Answer, Section, Citation)
✅ Responsive design (mobile-friendly)
✅ Flask backend scaffold with API ready

## TODO - Document Processing

The `LegalAssistant` class in `app.py` has these methods ready:
- `search_documents(query)` - Find relevant legal sections
- `translate_to_english(nepali_text)` - Use Claude to translate
- `generate_explanation(question, section)` - Create simplified answers
- `answer_question(question)` - Main pipeline

## Free Tier Claude API Notes

For 5 acts (MVP):
- Extract + translate PDFs: ~50-100 API calls (one-time)
- Per user query: 1-2 API calls
- Free tier should handle this easily

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

Ready to integrate your datasets! 🚀
