import streamlit as st
import random
import time
import difflib
from datetime import datetime

# --- Sentences Based on Difficulty ---
sentences_easy = [
    "Hello world.",
    "I love Python.",
    "This is a typing test.",
    "Streamlit is fun to use.",
]

sentences_medium = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed is measured in words per minute.",
    "Practice makes perfect when learning to type fast.",
]

sentences_hard = [
    "Streamlit makes it easy to build powerful web applications using Python.",
    "OpenAI develops cutting-edge AI tools that empower developers globally.",
    "Accuracy and speed are both crucial in effective typing performance.",
]

# --- Functions ---
def get_sentence(difficulty):
    if difficulty == "Easy":
        return random.choice(sentences_easy)
    elif difficulty == "Medium":
        return random.choice(sentences_medium)
    else:
        return random.choice(sentences_hard)

def calculate_wpm(start, end, typed_text):
    total_time = end - start
    words = len(typed_text.strip().split())
    wpm = (words / total_time) * 60 if total_time > 0 else 0
    return round(wpm, 2)

def calculate_accuracy(original, typed):
    matcher = difflib.SequenceMatcher(None, original, typed)
    return round(matcher.ratio() * 100, 2)

def highlight_mismatches(original, typed):
    diff = difflib.ndiff(original, typed)
    result = ""
    for d in diff:
        if d.startswith("  "):
            result += d[2:]
        elif d.startswith("- "):
            result += f"<span style='background-color:#ffcccc;'>{d[2:]}</span>"
    return result

# --- Streamlit UI ---
st.set_page_config("Typing Speed Test", layout="centered")
st.title("⌨️ Typing Speed Test")

tab1, tab2 = st.tabs(["🖋 Typing Test", "📊 History"])

with tab1:
    # Theme selection
    theme = st.selectbox("🎨 Select Theme", ["Light", "Dark"])
    if theme == "Dark":
        st.markdown("""
        <style>
            body { background-color: #1e1e1e; color: white; }
            .stTextArea textarea { background-color: #333; color: white; }
        </style>
        """, unsafe_allow_html=True)

    # Difficulty
    difficulty = st.radio("Select difficulty level:", ["Easy", "Medium", "Hard"], index=1)

    # Set sentence
    if "sentence" not in st.session_state or st.session_state.get("reset", False):
        st.session_state.sentence = get_sentence(difficulty)
        st.session_state.reset = False

    st.markdown("### Type the following sentence:")
    st.code(st.session_state.sentence, language="")

    # Start button
    if "start_time" not in st.session_state:
        if st.button("Start Test"):
            st.session_state.start_time = time.time()
            st.session_state.started = True
            st.session_state.timer = 60

    # Countdown
    if st.session_state.get("started", False):
        time_left = int(st.session_state.timer - (time.time() - st.session_state.start_time))
        if time_left > 0:
            st.warning(f"⏱️ Time Left: {time_left} seconds")
        else:
            st.session_state.started = False
            st.error("⏰ Time's up! Please submit your result manually.")

    # Typing input
    if st.session_state.get("started", False):
        typed_input = st.text_area("📝 Type here:", height=100)

        if st.button("Submit"):
            end_time = time.time()
            original = st.session_state.sentence
            wpm = calculate_wpm(st.session_state.start_time, end_time, typed_input)
            accuracy = calculate_accuracy(original, typed_input)

            st.success("✅ Test Completed!")
            st.metric("Words Per Minute (WPM)", wpm)
            st.metric("Accuracy (%)", f"{accuracy}%")

            # Beep sound
            st.markdown("""
            <audio autoplay>
                <source src="https://www.soundjay.com/button/beep-07.wav" type="audio/wav">
            </audio>
            """, unsafe_allow_html=True)

            # Track best WPM
            if "best_wpm" not in st.session_state or wpm > st.session_state.best_wpm:
                st.session_state.best_wpm = wpm
            st.info(f"🏆 Your Best WPM: {st.session_state.best_wpm}")

            # Track history
            if "history" not in st.session_state:
                st.session_state.history = []

            st.session_state.history.append({
                "Time": datetime.now().strftime("%H:%M:%S"),
                "WPM": wpm,
                "Accuracy": accuracy
            })

            # Show mistakes
            st.markdown("### 🔍 Mistakes Highlight")
            st.markdown(
                highlight_mismatches(original, typed_input),
                unsafe_allow_html=True,
            )

            # Reset
            if st.button("Try Another Sentence"):
                st.session_state.started = False
                st.session_state.reset = True
                del st.session_state.start_time

with tab2:
    st.subheader("📊 Typing History")
    if "history" in st.session_state and st.session_state.history:
        st.dataframe(st.session_state.history)
    else:
        st.info("No typing history yet. Complete a test to see your results here.")
