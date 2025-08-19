# Reddit User Persona Generator

This is a 100% free and open-source tool that scrapes Reddit user activity and uses a local LLM (like `phi-2`) to generate a detailed user persona.

---

## 📌 Features

* 🔍 Scrape Reddit posts & comments via **Reddit API (PRAW)**
* 🤖 Run **LLM-based analysis** using Hugging Face Transformers (`microsoft/phi-2`)
* 📝 Output detailed **user persona** (age group, personality traits, interests, tone, etc.)
* 🧾 Cites the Reddit posts/comments used for each trait
* ✅ Works offline if model is preloaded (no API keys required)

---

## ✨ Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/reddit_persona_generator.git
cd reddit_persona_generator
```

### 2. Set up the environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
pip install -r requirements.txt
```

### 3. Configure Reddit API

```bash
# Copy the example configuration file
copy praw.ini.example praw.ini

# Edit praw.ini with your Reddit API credentials
# Get credentials from: https://www.reddit.com/prefs/apps
```

### 4. Run the script

```bash
python main.py https://www.reddit.com/user/kojied/
```

---

## 🛠 Folder Structure

```
reddit_persona_generator/
├── main.py
├── reddit/
│   ├── reddit_scraper.py
│   └── utils.py
├── llm/
│   ├── model_loader.py
│   ├── prompt_builder.py
│   └── persona_generator.py
├── data/                  # Raw scraped Reddit data
├── outputs/               # Final generated persona .txt files
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧠 Models Used

By default, uses:

* **[`microsoft/phi-2`](https://huggingface.co/microsoft/phi-2)** – Free, reliable, and small enough for local use.

---

## 📃 Requirements

```
requests
transformers
accelerate
tqdm
torch
praw
```

---

## 🙋‍♀️ Author

**Thasniem Fathima J**
[LinkedIn](https://www.linkedin.com/in/thasniem-fathima-engineering-student)
[GitHub](https://github.com/Thasniem)

---

## ⚠️ Disclaimer

* This tool uses public Reddit data. Be respectful of privacy.
* Use for educational and internship purposes only.

---

## 📃 License

MIT License – Free to use, modify, and share.
