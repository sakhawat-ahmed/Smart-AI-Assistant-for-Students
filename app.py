import streamlit as st
import os
from dotenv import load_dotenv
import time
from datetime import datetime

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="English Practice Partner",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 2rem;
    }
    .practice-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #3498db;
        margin-bottom: 20px;
    }
    .level-badge {
        display: inline-block;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        margin: 5px;
    }
    .feedback-good {
        color: #27ae60;
        background-color: #d5f4e6;
        padding: 10px;
        border-radius: 5px;
    }
    .feedback-needs-work {
        color: #e74c3c;
        background-color: #fadbd8;
        padding: 10px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
def init_session_state():
    if 'user_level' not in st.session_state:
        st.session_state.user_level = "Beginner"
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []
    if 'vocabulary_list' not in st.session_state:
        st.session_state.vocabulary_list = []
    if 'practice_count' not in st.session_state:
        st.session_state.practice_count = 0
    if 'user_name' not in st.session_state:
        st.session_state.user_name = ""

# Main app
def main():
    init_session_state()
    
    # Sidebar
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/1995/1995515.png", width=100)
        st.title("🎓 English Practice Partner")
        
        st.session_state.user_name = st.text_input("Your Name", value=st.session_state.user_name)
        
        st.divider()
        
        # Level selection
        st.subheader("Your Level")
        levels = ["Beginner (A1)", "Elementary (A2)", "Intermediate (B1)", 
                 "Upper Intermediate (B2)", "Advanced (C1)", "Proficient (C2)"]
        selected_level = st.selectbox("Select your level", levels, 
                                    index=levels.index(st.session_state.user_level) 
                                    if st.session_state.user_level in levels else 0)
        st.session_state.user_level = selected_level
        
        st.divider()
        
        # Progress stats
        st.subheader("📊 Your Progress")
        st.metric("Practice Sessions", st.session_state.practice_count)
        st.metric("Vocabulary Words", len(st.session_state.vocabulary_list))
        
        st.divider()
        
        # Navigation
        st.subheader("Practice Areas")
        page = st.radio("Go to:", [
            "🏠 Home",
            "💬 Conversation Practice", 
            "🎤 Pronunciation Trainer",
            "📚 Vocabulary Builder",
            "📝 Grammar Exercises",
            "📈 Progress Dashboard"
        ])
    
    # Main content area
    if page == "🏠 Home":
        show_home_page()
    elif page == "💬 Conversation Practice":
        show_conversation_practice()
    elif page == "🎤 Pronunciation Trainer":
        show_pronunciation_trainer()
    elif page == "📚 Vocabulary Builder":
        show_vocabulary_builder()
    elif page == "📝 Grammar Exercises":
        show_grammar_exercises()
    elif page == "📈 Progress Dashboard":
        show_progress_dashboard()

def show_home_page():
    st.markdown('<h1 class="main-header">Welcome to Your English Practice Partner! 👋</h1>', 
                unsafe_allow_html=True)
    
    if st.session_state.user_name:
        st.markdown(f"### Hello, {st.session_state.user_name}! Ready to practice English?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="practice-card">
            <h3>💬 Conversation</h3>
            <p>Practice real conversations with AI</p>
            <ul>
                <li>Daily topics</li>
                <li>Role plays</li>
                <li>Business English</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="practice-card">
            <h3>🎤 Pronunciation</h3>
            <p>Improve your speaking skills</p>
            <ul>
                <li>Speech analysis</li>
                <li>Accent reduction</li>
                <li>Phoneme practice</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="practice-card">
            <h3>📚 Vocabulary</h3>
            <p>Expand your word bank</p>
            <ul>
                <li>Word of the day</li>
                <li>Context learning</li>
                <li>Flashcards</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick practice button
    if st.button("🎯 Start Quick Practice Session", use_container_width=True):
        st.session_state.practice_count += 1
        st.success(f"Great! You've completed {st.session_state.practice_count} practice sessions!")

def show_conversation_practice():
    st.title("💬 Conversation Practice")
    
    # Topic selection
    topics = {
        "Daily Life": ["Introducing yourself", "At the restaurant", "Shopping", "Travel plans"],
        "Business": ["Job interview", "Business meeting", "Email writing", "Presentation"],
        "Social": ["Making friends", "Hobbies", "Movies & Music", "Current events"]
    }
    
    selected_category = st.selectbox("Choose a category", list(topics.keys()))
    selected_topic = st.selectbox("Choose a topic", topics[selected_category])
    
    # Conversation area
    st.subheader(f"Topic: {selected_topic}")
    
    # Initialize conversation
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Display conversation history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # User input
    if prompt := st.chat_input("Type your message in English..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate AI response (simulated for now)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Simulate AI response
                response = generate_ai_response(prompt, selected_topic)
                st.markdown(response)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Record conversation
        st.session_state.conversation_history.append({
            "timestamp": datetime.now(),
            "topic": selected_topic,
            "user_input": prompt,
            "ai_response": response
        })

def generate_ai_response(prompt, topic):
    """Simulate AI response - Replace with actual API call later"""
    responses = {
        "Introducing yourself": [
            f"Nice to meet you! You said: '{prompt}'. Could you tell me more about your hobbies?",
            "That's a great introduction! How long have you been studying English?",
            f"Thanks for sharing! '{prompt}' - that's interesting. What do you do for work?"
        ],
        "At the restaurant": [
            "Good choice! What would you like to order from the menu?",
            "The special today is grilled salmon. Would you like to hear more about it?",
            "How would you like your steak cooked? Rare, medium, or well-done?"
        ],
        "Shopping": [
            "Are you looking for something specific today?",
            "That item comes in different sizes. Which size would you prefer?",
            "We have a sale on those items! Would you like to try them on?"
        ]
    }
    
    # Simple response generation
    import random
    if topic in responses:
        return random.choice(responses[topic])
    else:
        corrections = {
            "i": "I",
            "im": "I'm",
            "dont": "don't",
            "cant": "can't"
        }
        
        # Simple grammar check
        corrected = prompt
        for wrong, right in corrections.items():
            corrected = corrected.replace(f" {wrong} ", f" {right} ")
        
        follow_ups = [
            "Interesting! Tell me more about that.",
            "Good point! Can you elaborate?",
            "I see. What do you think about this?",
            f"You said: '{corrected}'. That's a good sentence!",
            "Could you rephrase that in a different way?"
        ]
        
        return random.choice(follow_ups)

def show_pronunciation_trainer():
    st.title("🎤 Pronunciation Trainer")
    
    st.info("""
    **Pronunciation Practice** - Speak the phrases below and get feedback on your pronunciation.
    """)
    
    # Practice phrases by difficulty
    phrases = {
        "Beginner": [
            "Hello, how are you?",
            "My name is...",
            "I live in...",
            "Thank you very much",
            "Excuse me, please"
        ],
        "Intermediate": [
            "Could you repeat that, please?",
            "I would like to make a reservation",
            "What do you recommend?",
            "Let's meet tomorrow afternoon",
            "I'm looking forward to it"
        ],
        "Advanced": [
            "The phenomenon of linguistic relativity",
            "Statistical analysis of variance",
            "Extraordinary circumstances require extraordinary measures",
            "Unprecedented technological advancements",
            "Multifaceted approach to problem-solving"
        ]
    }
    
    selected_level = st.selectbox("Select difficulty", list(phrases.keys()))
    
    # Display phrases
    st.subheader("Practice These Phrases:")
    for i, phrase in enumerate(phrases[selected_level], 1):
        st.write(f"{i}. **{phrase}**")
        if st.button(f"Practice #{i}", key=f"phrase_{i}"):
            st.session_state.current_phrase = phrase
    
    # Pronunciation recording area
    if 'current_phrase' in st.session_state:
        st.divider()
        st.subheader("🎤 Record Your Pronunciation")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"### Speak this: **{st.session_state.current_phrase}**")
            
            # Record button
            if st.button("🎤 Start Recording", type="primary"):
                with st.spinner("Recording... Speak now!"):
                    time.sleep(3)  # Simulate recording
                    st.success("Recording complete!")
        
        with col2:
            st.subheader("📊 Pronunciation Feedback")
            
            # Simulated feedback
            feedback = {
                "Clarity": {"score": 85, "comment": "Good enunciation"},
                "Pace": {"score": 75, "comment": "Slightly fast"},
                "Intonation": {"score": 90, "comment": "Natural rhythm"},
                "Accuracy": {"score": 80, "comment": "Minor vowel sounds need work"}
            }
            
            for aspect, data in feedback.items():
                st.progress(data["score"] / 100, text=f"{aspect}: {data['score']}%")
                st.caption(f"💡 {data['comment']}")
    
    # Tips section
    st.divider()
    st.subheader("💡 Pronunciation Tips")
    tips = [
        "🎯 **Slow down** - Speak slowly and clearly",
        "👂 **Listen carefully** to native speakers",
        "🗣️ **Record yourself** and compare",
        "📱 **Use pronunciation apps** for practice",
        "🎵 **Sing along** to English songs"
    ]
    
    for tip in tips:
        st.markdown(f"- {tip}")

def show_vocabulary_builder():
    st.title("📚 Vocabulary Builder")
    
    # Word of the day
    st.subheader("✨ Word of the Day")
    
    word_of_day = {
        "word": "Perseverance",
        "meaning": "Continued effort to achieve something despite difficulties",
        "example": "Her perseverance helped her learn English in just one year.",
        "synonyms": ["persistence", "determination", "tenacity"]
    }
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        ### {word_of_day['word']}
        **Meaning:** {word_of_day['meaning']}
        
        **Example:** *"{word_of_day['example']}"*
        
        **Synonyms:** {', '.join(word_of_day['synonyms'])}
        """)
    
    with col2:
        if st.button("Add to My Vocabulary", key="add_word"):
            if word_of_day not in st.session_state.vocabulary_list:
                st.session_state.vocabulary_list.append(word_of_day)
                st.success(f"'{word_of_day['word']}' added to your vocabulary!")
    
    # User's vocabulary list
    st.divider()
    st.subheader("📖 My Vocabulary List")
    
    if st.session_state.vocabulary_list:
        for i, word in enumerate(st.session_state.vocabulary_list):
            with st.expander(f"{i+1}. {word['word']}"):
                st.write(f"**Meaning:** {word['meaning']}")
                st.write(f"**Example:** {word['example']}")
                st.write(f"**Synonyms:** {', '.join(word['synonyms'])}")
                
                # Mastery level
                mastery = st.slider(
                    f"Mastery level for '{word['word']}'",
                    0, 100, 50,
                    key=f"mastery_{i}"
                )
                st.progress(mastery / 100)
    else:
        st.info("Your vocabulary list is empty. Add some words to get started!")
    
    # Add custom word
    st.divider()
    st.subheader("➕ Add New Word")
    
    with st.form("add_word_form"):
        new_word = st.text_input("Word")
        meaning = st.text_area("Meaning")
        example = st.text_area("Example sentence")
        
        if st.form_submit_button("Add Word"):
            if new_word and meaning:
                new_entry = {
                    "word": new_word,
                    "meaning": meaning,
                    "example": example,
                    "synonyms": []
                }
                st.session_state.vocabulary_list.append(new_entry)
                st.success(f"'{new_word}' added successfully!")

def show_grammar_exercises():
    st.title("📝 Grammar Exercises")
    
    # Grammar topics
    topics = [
        "Present Tense",
        "Past Tense", 
        "Future Tense",
        "Articles (a/an/the)",
        "Prepositions",
        "Modal Verbs",
        "Conditionals",
        "Reported Speech"
    ]
    
    selected_topic = st.selectbox("Select a grammar topic", topics)
    
    # Exercises based on topic
    exercises = {
        "Present Tense": [
            {
                "question": "She ______ (to go) to school every day.",
                "answer": "goes",
                "explanation": "Use 'goes' for third person singular (he/she/it) in present simple"
            },
            {
                "question": "They ______ (to watch) TV right now.",
                "answer": "are watching",
                "explanation": "Use present continuous for actions happening now"
            }
        ],
        "Past Tense": [
            {
                "question": "I ______ (to eat) dinner at 7 PM yesterday.",
                "answer": "ate",
                "explanation": "'ate' is the past tense of 'eat'"
            },
            {
                "question": "She ______ (to be) studying when I called.",
                "answer": "was",
                "explanation": "Use 'was' with singular subjects in past continuous"
            }
        ]
    }
    
    st.subheader(f"Exercises: {selected_topic}")
    
    if selected_topic in exercises:
        for i, exercise in enumerate(exercises[selected_topic], 1):
            with st.expander(f"Exercise {i}"):
                user_answer = st.text_input(f"Complete: {exercise['question']}", key=f"ex_{i}")
                
                if st.button(f"Check Answer {i}", key=f"check_{i}"):
                    if user_answer.lower() == exercise['answer'].lower():
                        st.success("✅ Correct! " + exercise['explanation'])
                    else:
                        st.error(f"❌ Not quite. The correct answer is: **{exercise['answer']}**")
                        st.info(f"💡 {exercise['explanation']}")
    else:
        st.info("More exercises coming soon for this topic!")

def show_progress_dashboard():
    st.title("📈 Progress Dashboard")
    
    # Stats
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Practice Sessions", st.session_state.practice_count)
    
    with col2:
        st.metric("Vocabulary Words", len(st.session_state.vocabulary_list))
    
    with col3:
        avg_mastery = 50  # Calculate average from vocabulary mastery
        st.metric("Average Mastery", f"{avg_mastery}%")
    
    # Progress chart (simulated)
    st.subheader("📊 Weekly Activity")
    
    # Simulated data
    import pandas as pd
    import plotly.express as px
    
    data = pd.DataFrame({
        'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        'Minutes': [20, 35, 15, 45, 30, 25, 40],
        'Exercises': [5, 8, 3, 10, 7, 6, 9]
    })
    
    fig = px.line(data, x='Day', y='Minutes', title='Daily Practice Time (minutes)')
    st.plotly_chart(fig, use_container_width=True)
    
    # Recent activity
    st.subheader("📝 Recent Practice")
    
    if st.session_state.conversation_history:
        for i, conv in enumerate(reversed(st.session_state.conversation_history[-5:])):
            st.markdown(f"""
            **{conv['timestamp'].strftime('%Y-%m-%d %H:%M')}** - *{conv['topic']}*
            - You: {conv['user_input'][:50]}...
            - AI: {conv['ai_response'][:50]}...
            """)
    else:
        st.info("No recent practice sessions. Start practicing to see your activity here!")

if __name__ == "__main__":
    main()