# Concierge: AI-Powered Meeting Summarization & Action Item Tracker

![Project Logo](https://img.shields.io/badge/AI-Powered_Meeting_Summarizer-blueviolet)

---

## 🚀 Live Frontend UI (Demo Link)

🔗 [Open MOM Generator UI](https://your-deployment-link.com) *(replace with real link once hosted)*

---

## 📋 About the Project

**Concierge** is an AI-enabled meeting summarization and action item tracker.
It automatically:

- Summarizes messy RAG outputs into professional Minutes of Meeting (MOM)
- Highlights key discussion points, action items, owners, and deadlines
- Saves time, reduces manual effort, and improves meeting productivity

> _"Less time in meetings, more time for impact."_

---

## 🛠️ Tech Stack Used

| Layer | Technology |
|:---|:---|
| Frontend | HTML5, CSS3, JavaScript (Vanilla) |
| Backend | Python 3, FastAPI |
| LLM | Gemini 2.0 Flash API (Google Generative Language API) |
| Server | Uvicorn ASGI server |

---

## 📦 Folder Structure

```
MOM_Generator_Project/
├── frontend/
│   └── index.html
├── backend/
│   ├── backend.py
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
```

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/anjalipandey21/MOM_Generator_Project.git
cd MOM_Generator_Project/backend
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

- Create a `.env` file in `/backend`.
- Add your Gemini API key:

```bash
GEMINI_API_KEY=your-gemini-api-key-here
```

(You can get it from [Google Makersuite](https://makersuite.google.com/app/apikey))

### 4. Start the Backend Server

```bash
uvicorn backend:app --reload
```

Server will start at:
```
http://localhost:8000
```

### 5. Open the Frontend

Navigate to `/frontend` folder and open `index.html` manually in your browser.

✅ Paste RAG output ➔ Generate MOM ➔ Download .txt if needed.

---

## 🎯 Key Features

- ✨ AI-generated professional MOM (Minutes of Meeting)
- 📋 Highlighted action items and owners
- 📂 Custom summaries for technical, management, and C-suite teams (future extension)
- 📄 Downloadable MOM text file
- 🔒 Secure handling of API keys via `.env`

---

## 📈 Future Enhancements

- Upload meeting videos for automatic speech-to-text. ➔ MOM
- Real-time meeting summarization.
- DOCX export format.
- Slack/Teams integration for action item notifications.
- Hosting frontend and backend publicly.

---
