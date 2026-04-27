# tube-tldr — YouTube Video Summarizer using AI

Ever wanted to understand a YouTube video without watching the whole thing?
tube-tldr does exactly that — paste a YouTube link, and AI gives you a clean 
summary in seconds.

Built with Python, Streamlit, and LLaMA 3.1 (via Hugging Face).

---

## How It Works

1. You paste a YouTube video URL into the app
2. The app fetches the video's transcript (auto-generated captions)
3. The transcript is sent to LLaMA 3.1 (a powerful AI language model)
4. The AI reads it and returns a clean 250-word summary
5. You read the summary instead of watching a 30-minute video

---

## Tech Stack

| Tool                  | Purpose                                      |
|-----------------------|----------------------------------------------|
| Python 3.11           | Core programming language                    |
| Streamlit             | Web interface (no HTML/CSS needed)           |
| Hugging Face          | Access to AI models via free API             |
| LLaMA 3.1 8B Instruct | AI model that reads and summarizes text      |
| YouTube Transcript API| Fetches captions from any YouTube video      |
| python-dotenv         | Securely loads secret API keys               |
| Conda                 | Manages isolated Python environment          |

---

## How to Run This Project Locally

### Step 1 — Clone the repository
git clone https://github.com/your-username/tube-tldr.git
cd tube-tldr

### Step 2 — Create the virtual environment
conda create -p ./venv python=3.11 -y

### Step 3 — Activate the environment
conda activate ./venv

### Step 4 — Install all dependencies
pip install -r requirements.txt

### Step 5 — Create your .env file
Create a file called .env in the project folder and add your 
Hugging Face token inside it like this:

HF_TOKEN=your_huggingface_token_here

Get your free token here: https://huggingface.co/settings/tokens
(Click "New Token" → select "Read" → copy and paste it)

### Step 6 — Run the app
python -m streamlit run helper.py

### Step 7 — Use the app
Open your browser, paste any YouTube URL, and click the button.

---

## Project Structure

tube-tldr/
│
├── helper.py          # Main app — all the logic and UI lives here
├── requirements.txt   # All Python packages needed to run the app
├── readme.txt         # You are reading this right now
└── .env               # YOUR secret token (never shared, never uploaded)

---

## Security Note

The .env file contains your private API token.
It is listed in .gitignore and will NEVER be uploaded to GitHub.
Anyone who clones this repo must create their own .env file 
with their own Hugging Face token.

---

## Why I Built This

As part of exploring real-world LLM applications, I wanted to build 
something genuinely useful — not just a tutorial project. 

This app solves a real problem: saving time by letting AI summarize 
long YouTube videos instantly. It combines transcript extraction, 
LLM inference, and a clean web UI — all in under 100 lines of Python.

---

##  Author

Anmol Srivastava
Powered by Hugging Face and YouTube Transcript API
