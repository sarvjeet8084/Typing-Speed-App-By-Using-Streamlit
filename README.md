# Typing-Speed-App-By-Using-Streamlit

:

🌟 Overview:

This project is a Typing Speed Test Web App built with Python and Streamlit. It allows users to:

Select a difficulty level.

Type a given sentence.

Measure their typing speed (WPM) and accuracy.

View highlighted mistakes.

Track their best WPM and typing history.

🧠 Code Breakdown

1. Sentence Bank
You’ve grouped predefined sentences into 3 difficulty levels:

python
Copy
Edit
sentences_easy, sentences_medium, sentences_hard
These are used to generate random typing prompts based on user choice.

2. Functions
get_sentence(difficulty)
Returns a random sentence from the chosen difficulty.

calculate_wpm(start, end, typed_text)
Calculates Words Per Minute:

python
Copy
Edit
WPM = (words / time_in_seconds) * 60
calculate_accuracy(original, typed)
Uses difflib.SequenceMatcher to compute percentage similarity between original and typed sentence.

highlight_mismatches(original, typed)
Uses difflib.ndiff() to visually highlight characters in the original sentence that were deleted or mistyped, using red background via HTML <span> tags.

3. Streamlit UI
st.set_page_config(...)
Sets page title and layout.

st.title(...)
Displays the app’s title.

4. Tab Layout
You have 2 tabs:

python
Copy
Edit
tab1, tab2 = st.tabs(["Typing Test", "History"])
📌 tab1: Typing Test

Features in this tab:

🎨 Theme Toggle (Light/Dark):

When "Dark" is selected, custom CSS is injected to change background and font colors.

🧩 Difficulty Selector:

Radio buttons let users select “Easy”, “Medium”, or “Hard”.

📋 Sentence Prompt:

Shows the random sentence based on difficulty using st.code().

⏱️ Start Button + Timer:

When pressed, records start_time and begins a 60-second countdown.

📝 Typing Area:

Text input field for typing the sentence.

📤 Submit Button:

Calculates and shows:

✅ Completion message

📈 Words Per Minute

🎯 Accuracy

🔔 Beep sound using an embedded <audio> HTML tag

🏆 Best WPM across sessions

🧠 Mistake highlights

🔁 Try Another Sentence:

Resets the test and lets user retry with a new sentence.

📌 tab2: Typing History

Displays all completed tests in a table.

Columns: Time, WPM, Accuracy.

5. Session State Management
Streamlit’s st.session_state is used to persist:

start_time – when the test began

started – whether the test is active

sentence – the current prompt

best_wpm – best WPM so far

history – list of past results (time, WPM, accuracy)

This helps maintain values across reruns without losing state.

🎯 What Makes This App Great?
✅ Real-time timer with countdown
✅ Tracks typing accuracy and WPM
✅ Highlights mistakes using HTML
✅ Supports theme toggle (light/dark)
✅ Stores and shows user performance history

🛠️ Potential Improvements
Add leaderboard for multi-user support

Store data permanently using SQLite or Google Sheets

Add typing sound effects

Use custom fonts for the sentence area

Track keystrokes per second or typing rhythm

🚀 How to Run

Save as typing_speed_app.py

Install Streamlit:

pip install streamlit

Run:

streamlit run typing_speed_app.py

OUTPUT:
<img width="1439" height="824" alt="image" src="https://github.com/user-attachments/assets/93482b21-1e8b-455c-a5c3-05c31fda848d" />
<img width="1423" height="823" alt="image" src="https://github.com/user-attachments/assets/42c28bdd-d5b2-45e0-8f2f-c0ca5ff49c94" />
<img width="1398" height="276" alt="image" src="https://github.com/user-attachments/assets/cf8c84ff-c4f8-4125-8175-1abb3dc67223" />
<img width="1280" height="621" alt="image" src="https://github.com/user-attachments/assets/fe8406c2-d56a-4b4c-b27b-288ab7eb1165" />
