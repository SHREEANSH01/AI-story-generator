import streamlit as st
import openai
import os

# Set your OpenAI API key (correct way for openai>=1.0.0)
openai.api_key = os.getenv("OPENAI_API_KEY")

# --- UI Setup ---
st.set_page_config(page_title="AI Story Generator", page_icon="📖", layout="centered")
st.title("📖 AI Story Generator")
st.markdown("Let your imagination run wild! Enter a prompt, choose a genre and length, and let the AI spin a tale.")

# --- User Inputs ---
prompt = st.text_input("📝 Enter your story prompt:", placeholder="e.g., A time traveler visits ancient Egypt")

genre = st.selectbox("🎭 Choose a genre:", [
    "Fantasy", "Science Fiction", "Mystery", "Romance", "Adventure", "Horror", "Historical Fiction", "Comedy"
])

length = st.radio("📏 Select story length:", ["Short (100-200 words)", "Medium (200-400 words)", "Long (400-600 words)"])

length_map = {
    "Short (100-200 words)": 300,
    "Medium (200-400 words)": 500,
    "Long (400-600 words)": 700
}

temperature = st.slider("🎨 Creativity level (temperature)", 0.5, 1.0, 0.9)

# --- Generate Story ---
if st.button("✨ Generate Story") and prompt:
    with st.spinner("Crafting your story..."):
        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"You are a creative storyteller who writes {genre.lower()} stories."},
                    {"role": "user", "content": f"Write a {genre.lower()} story based on this prompt: '{prompt}'. Make it {length.lower()}."}
                ],
                max_tokens=length_map[length],
                temperature=temperature
            )
            story = response.choices[0].message.content
            st.markdown("### 🌟 Your AI-Generated Story")
            st.write(story)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
