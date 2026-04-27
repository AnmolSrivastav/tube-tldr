import streamlit as st
from dotenv import load_dotenv
import os
from youtube_transcript_api import YouTubeTranscriptApi
from huggingface_hub import InferenceClient
import traceback

# Load environment variables from .env
load_dotenv()

# Fetch token
hf_token = os.getenv("HF_TOKEN")

# Initialize Hugging Face Client
client = InferenceClient(model="meta-llama/Llama-3.1-8B-Instruct", provider="cerebras", api_key=hf_token)

prompt = """Please summarize this video transcript in 250 words or less, highlighting key points and insights:"""

# Function to extract transcript details from YouTube video URL
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("v=")[-1].split("&")[0]
        
        # MINIMAL FIX: Added () to initialize the API, and .to_raw_data() to get the text list
        fetched_data = YouTubeTranscriptApi().fetch(video_id)
        transcript_items = fetched_data.to_raw_data()
        
        transcript = " ".join([item["text"] for item in transcript_items])
        return transcript
    except Exception as e:
        raise e

# Function to generate summary using Hugging Face
def generate_summary(transcript_text, prompt_text):
    safe_text = transcript_text[:3000]
    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt_text + "\n\n" + safe_text}],
        max_tokens=500
    )
    return response.choices[0].message.content

# --- REARRANGED UI SECTION ---

# 1. Header for the app (Moved to the top)
st.title("YouTube Video Transcript Summarizer")
st.write("Enter a YouTube video URL to fetch its transcript and generate a summary using Hugging Face BART.")

# 2. Text Input (Moved OUTSIDE the button so it shows when the page opens)
youtube_video_url = st.text_input("Enter YouTube Video URL:", placeholder="https://www.youtube.com/watch?v=...")

# 3. Button to fetch and display summary (Placed directly below the input)
# 3. Button to fetch and display summary (Placed directly below the input)
if st.button("Fetch and Display Summary"):
    if youtube_video_url:
        # ADD THIS LINE: It shows a loading wheel while the code runs
        with st.spinner("Summarizing (this might take 1-2 minutes)..."):
            try:
                transcript_text = extract_transcript_details(youtube_video_url)
                summary = generate_summary(transcript_text, prompt)
                st.subheader("Summary:")
                st.write(summary)
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.code(traceback.format_exc())
            
# 4. Footer for the app (Stays at the bottom)
st.markdown("---")  
st.markdown("Created by Anmol Srivastava. Powered by Hugging Face and YouTube Transcript API.")