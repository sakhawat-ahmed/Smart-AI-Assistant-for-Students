import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header
import json
import time
from datetime import datetime, timedelta
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import random
import os
from pathlib import Path

# Set page config with premium look
st.set_page_config(
    page_title="English Practice Partner | AI Tutor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Import custom CSS
def load_css():
    with open('style.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session state
def init_session_state():
    defaults = {
        'user_name': '',
        'user_level': 'B1 Intermediate',
        'streak_days': 7,
        'total_points': 1250,
        'practice_time': 45,
        'conversation_history': [],
        'vocabulary': [],
        'achievements': [],
        'daily_goal': 30,
        'theme': 'light',
        'ai_model': 'gpt-3.5-turbo',
        'voice_gender': 'female',
        'accent': 'american'
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

# Custom CSS for premium design
st.markdown("""
<style>
    /* Main background gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    /* Main content area */
    .main-content {
        background: white;
        border-radius: 20px;
        padding: 30px;
        margin: 20px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.15);
        min-height: 90vh;
    }
    
    /* Premium card design */
    .premium-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        padding: 25px;
        border: none;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        transition: transform 0.3s ease;
        height: 100%;
    }
    
    .premium-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.12);
    }
    
    /* Gradient buttons */
    .gradient-btn {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 50px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .gradient-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Animated progress bars */
    @keyframes progressAnimation {
        from { width: 0%; }
    }
    
    .animated-progress {
        animation: progressAnimation 1.5s ease-in-out;
    }
    
    /* Chat bubbles */
    .user-bubble {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 15px 20px;
        border-radius: 20px 20px 5px 20px;
        margin: 10px 0;
        max-width: 70%;
        margin-left: auto;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .ai-bubble {
        background: #f0f2f6;
        color: #333;
        padding: 15px 20px;
        border-radius: 20px 20px 20px 5px;
        margin: 10px 0;
        max-width: 70%;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    /* Badges */
    .badge {
        display: inline-flex;
        align-items: center;
        padding: 5px 15px;
        border-radius: 50px;
        font-size: 12px;
        font-weight: 600;
        margin: 2px;
    }
    
    .level-badge {
        background: linear-gradient(45deg, #4facfe, #00f2fe);
        color: white;
    }
    
    .achievement-badge {
        background: linear-gradient(45deg, #ff9a9e, #fad0c4);
        color: white;
    }
    
    /* Floating animation */
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    .floating {
        animation: float 3s ease-in-out infinite;
    }
    
    /* Custom headers */
    .gradient-header {
        background: linear-gradient(45deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }
    
    /* Stats cards */
    .stats-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #667eea;
        box-shadow: 0 5px 20px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar with user profile
def render_sidebar():
    with st.sidebar:
        # User profile card
        st.markdown("""
        <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
             border-radius: 15px; color: white; margin-bottom: 30px;'>
            <div style='font-size: 60px;'>👨‍🎓</div>
            <h3 style='margin: 10px 0;'>{}</h3>
            <div class='badge level-badge'>{}</div>
            <div style='margin-top: 15px;'>
                🔥 <strong>{}-day streak</strong>
            </div>
        </div>
        """.format(
            st.session_state.user_name or "Guest",
            st.session_state.user_level,
            st.session_state.streak_days
        ), unsafe_allow_html=True)
        
        # Navigation
        st.markdown("### 🧭 Navigation")
        
        nav_options = {
            "🏠 Dashboard": "Dashboard",
            "💬 Conversation": "Conversation",
            "🎤 Pronunciation": "Pronunciation",
            "📚 Vocabulary": "Vocabulary",
            "📝 Grammar": "Grammar",
            "🎮 Games": "Games",
            "📈 Progress": "Progress",
            "⚙️ Settings": "Settings"
        }
        
        for icon, page in nav_options.items():
            if st.button(icon, use_container_width=True, key=f"nav_{page}"):
                st.session_state.current_page = page
                st.rerun()
        
        # Daily goal progress
        st.markdown("---")
        st.markdown("### 🎯 Daily Goal")
        goal_progress = min(st.session_state.practice_time / st.session_state.daily_goal, 1)
        st.progress(goal_progress)
        st.caption(f"{st.session_state.practice_time}/{st.session_state.daily_goal} minutes")
        
        # Quick stats
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Points", f"🎖️ {st.session_state.total_points}")
        with col2:
            st.metric("Words", f"📚 {len(st.session_state.vocabulary)}")

# Hero section with animated elements
def render_hero():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style='padding: 30px 0;'>
            <h1 style='font-size: 3.5rem; margin-bottom: 10px;' class='gradient-header'>
                AI English Practice Partner
            </h1>
            <p style='font-size: 1.2rem; color: #666; margin-bottom: 30px;'>
                Your personal AI tutor for mastering English speaking, pronunciation, and grammar.
                Practice like never before with interactive conversations and real-time feedback.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Quick action buttons
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            if st.button("🎤 Start Speaking", use_container_width=True):
                st.session_state.current_page = "Pronunciation"
                st.rerun()
        with col_b:
            if st.button("💬 Chat Practice", use_container_width=True):
                st.session_state.current_page = "Conversation"
                st.rerun()
        with col_c:
            if st.button("🎮 Play Games", use_container_width=True):
                st.session_state.current_page = "Games"
                st.rerun()
    
    with col2:
        # Animated illustration
        st.markdown("""
        <div class='floating' style='text-align: center;'>
            <div style='font-size: 200px;'>🤖</div>
        </div>
        """, unsafe_allow_html=True)

# Dashboard with stats cards
def render_dashboard():
    st.markdown("## 📊 Your Learning Dashboard")
    
    # Top stats row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        with stylable_container(
            key="stats_card_1",
            css_styles="""
            {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 15px;
                padding: 20px;
                color: white;
            }
            """
        ):
            st.metric("🔥 Streak", f"{st.session_state.streak_days} days")
            st.caption("Keep it going!")
    
    with col2:
        with stylable_container(
            key="stats_card_2",
            css_styles="""
            {
                background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                border-radius: 15px;
                padding: 20px;
                color: white;
            }
            """
        ):
            st.metric("🎖️ Points", f"{st.session_state.total_points}")
            st.caption("+150 today")
    
    with col3:
        with stylable_container(
            key="stats_card_3",
            css_styles="""
            {
                background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
                border-radius: 15px;
                padding: 20px;
                color: white;
            }
            """
        ):
            st.metric("⏱️ Practice", f"{st.session_state.practice_time}m")
            st.caption("Daily goal: 30m")
    
    with col4:
        with stylable_container(
            key="stats_card_4",
            css_styles="""
            {
                background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
                border-radius: 15px;
                padding: 20px;
                color: white;
            }
            """
        ):
            st.metric("📚 Words", f"{len(st.session_state.vocabulary)}")
            st.caption("+5 new today")
    
    # Main content area
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        # Activity chart
        st.markdown("### 📈 Weekly Activity")
        activity_data = pd.DataFrame({
            'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            'Conversation': [25, 30, 20, 35, 40, 25, 30],
            'Pronunciation': [15, 20, 25, 15, 20, 30, 25],
            'Grammar': [10, 15, 10, 20, 15, 10, 15]
        })
        
        fig = px.bar(activity_data, x='Day', y=['Conversation', 'Pronunciation', 'Grammar'],
                    title="Practice Time (minutes)", barmode='stack',
                    color_discrete_sequence=['#667eea', '#4facfe', '#43e97b'])
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
        
        # Quick practice cards
        st.markdown("### ⚡ Quick Practice")
        qp_col1, qp_col2, qp_col3 = st.columns(3)
        
        with qp_col1:
            with stylable_container(
                key="quick_practice_1",
                css_styles="""
                {
                    background: #f8f9fa;
                    border-radius: 15px;
                    padding: 20px;
                    text-align: center;
                    cursor: pointer;
                    transition: all 0.3s ease;
                }
                :hover {
                    transform: translateY(-5px);
                    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                }
                """
            ):
                st.markdown("### 💬")
                st.markdown("**Daily Chat**")
                st.caption("5 min conversation")
                if st.button("Start", key="qp1"):
                    st.session_state.current_page = "Conversation"
                    st.rerun()
        
        with qp_col2:
            with stylable_container(
                key="quick_practice_2",
                css_styles="""
                {
                    background: #f8f9fa;
                    border-radius: 15px;
                    padding: 20px;
                    text-align: center;
                    cursor: pointer;
                    transition: all 0.3s ease;
                }
                """
            ):
                st.markdown("### 🎤")
                st.markdown("**Tongue Twister**")
                st.caption("Improve pronunciation")
                if st.button("Start", key="qp2"):
                    st.session_state.current_page = "Pronunciation"
                    st.rerun()
        
        with qp_col3:
            with stylable_container(
                key="quick_practice_3",
                css_styles="""
                {
                    background: #f8f9fa;
                    border-radius: 15px;
                    padding: 20px;
                    text-align: center;
                    cursor: pointer;
                    transition: all 0.3s ease;
                }
                """
            ):
                st.markdown("### 🎯")
                st.markdown("**Word Challenge**")
                st.caption("5 new words")
                if st.button("Start", key="qp3"):
                    st.session_state.current_page = "Vocabulary"
                    st.rerun()
    
    with col_right:
        # Achievements
        st.markdown("### 🏆 Achievements")
        achievements = [
            {"icon": "🔥", "name": "7-Day Streak", "progress": 100},
            {"icon": "💬", "name": "Chat Master", "progress": 75},
            {"icon": "🎤", "name": "Pronunciation Pro", "progress": 50},
            {"icon": "📚", "name": "Word Collector", "progress": 30},
            {"icon": "🌟", "name": "Grammar Guru", "progress": 20},
        ]
        
        for ach in achievements:
            with stylable_container(
                key=f"ach_{ach['name']}",
                css_styles="""
                {
                    background: white;
                    border-radius: 10px;
                    padding: 10px;
                    margin: 5px 0;
                    border-left: 3px solid #667eea;
                }
                """
            ):
                col_a, col_b = st.columns([1, 3])
                with col_a:
                    st.markdown(f"<h2>{ach['icon']}</h2>", unsafe_allow_html=True)
                with col_b:
                    st.write(ach['name'])
                    st.progress(ach['progress'] / 100)
        
        # Leaderboard
        st.markdown("### 🏅 Weekly Leaderboard")
        leaderboard = [
            {"name": "You", "points": 1250, "change": "▲"},
            {"name": "Alex", "points": 1100, "change": "▲"},
            {"name": "Maria", "points": 950, "change": "▼"},
            {"name": "John", "points": 850, "change": "▲"},
            {"name": "Sara", "points": 750, "change": "▼"},
        ]
        
        for i, player in enumerate(leaderboard):
            emoji = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"][i]
            st.markdown(f"{emoji} **{player['name']}** - {player['points']} pts {player['change']}")

# Enhanced conversation page
def render_conversation():
    st.markdown("## 💬 AI Conversation Practice")
    
    # Topic selection with cards
    st.markdown("### 🎯 Choose a Topic")
    
    topics = [
        {"icon": "🍽️", "name": "Restaurant", "color": "#FF6B6B", "scenes": ["Ordering food", "Complaining", "Paying bill"]},
        {"icon": "✈️", "name": "Travel", "color": "#4ECDC4", "scenes": ["Airport", "Hotel", "Directions"]},
        {"icon": "💼", "name": "Business", "color": "#45B7D1", "scenes": ["Interview", "Meeting", "Presentation"]},
        {"icon": "🛒", "name": "Shopping", "color": "#96CEB4", "scenes": ["Clothes", "Electronics", "Returns"]},
        {"icon": "🏥", "name": "Health", "color": "#FFEAA7", "scenes": ["Doctor", "Pharmacy", "Symptoms"]},
        {"icon": "🎬", "name": "Entertainment", "color": "#DDA0DD", "scenes": ["Movies", "Music", "Books"]},
    ]
    
    cols = st.columns(3)
    for idx, topic in enumerate(topics):
        with cols[idx % 3]:
            with stylable_container(
                key=f"topic_{topic['name']}",
                css_styles=f"""
                {{
                    background: {topic['color']}15;
                    border-radius: 15px;
                    padding: 20px;
                    border: 2px solid {topic['color']}40;
                    text-align: center;
                    cursor: pointer;
                    transition: all 0.3s ease;
                }}
                :hover {{
                    transform: scale(1.05);
                    border: 2px solid {topic['color']};
                }}
                """
            ):
                st.markdown(f"<h1>{topic['icon']}</h1>", unsafe_allow_html=True)
                st.markdown(f"**{topic['name']}**")
                for scene in topic['scenes']:
                    st.caption(f"• {scene}")
                if st.button("Select", key=f"sel_{topic['name']}"):
                    st.session_state.selected_topic = topic['name']
                    st.rerun()
    
    # Conversation interface
    if 'selected_topic' in st.session_state:
        st.divider()
        st.markdown(f"### 🎭 Role Play: {st.session_state.selected_topic}")
        
        # Scene setup
        role_scenes = {
            "Restaurant": ["You: Customer", "AI: Waiter"],
            "Travel": ["You: Tourist", "AI: Local Guide"],
            "Business": ["You: Job Applicant", "AI: Interviewer"],
        }
        
        scene = role_scenes.get(st.session_state.selected_topic, ["You: Student", "AI: Tutor"])
        col1, col2 = st.columns(2)
        with col1:
            st.info(scene[0])
        with col2:
            st.success(scene[1])
        
        # Chat interface
        if 'conversation_messages' not in st.session_state:
            st.session_state.conversation_messages = [
                {"role": "ai", "content": f"Hello! Welcome to our {st.session_state.selected_topic.lower()} practice. How can I help you today?"}
            ]
        
        # Display messages
        chat_container = st.container()
        with chat_container:
            for msg in st.session_state.conversation_messages:
                if msg['role'] == 'user':
                    st.markdown(f"""
                    <div style='display: flex; justify-content: flex-end; margin: 10px 0;'>
                        <div class='user-bubble'>
                            {msg['content']}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style='display: flex; justify-content: flex-start; margin: 10px 0;'>
                        <div class='ai-bubble'>
                            {msg['content']}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Input with voice option
        input_col1, input_col2 = st.columns([5, 1])
        with input_col1:
            user_input = st.text_input("Type your message...", key="chat_input", 
                                     placeholder="Speak naturally as you would in real conversation...")
        with input_col2:
            if st.button("🎤 Speak", use_container_width=True):
                st.info("Voice input coming soon! For now, type your message.")
        
        if user_input:
            # Add user message
            st.session_state.conversation_messages.append({"role": "user", "content": user_input})
            
            # Generate AI response
            with st.spinner("AI is thinking..."):
                time.sleep(1)  # Simulate AI thinking
                ai_response = generate_ai_response(user_input, st.session_state.selected_topic)
                st.session_state.conversation_messages.append({"role": "ai", "content": ai_response})
            
            st.rerun()
        
        # Feedback panel
        st.divider()
        st.markdown("### 📊 Conversation Feedback")
        
        feedback_cols = st.columns(3)
        with feedback_cols[0]:
            with stylable_container(
                key="feedback_grammar",
                css_styles="""
                {
                    background: #e3f2fd;
                    border-radius: 10px;
                    padding: 15px;
                }
                """
            ):
                st.markdown("**Grammar Score**")
                st.markdown("<h2 style='color: #1976d2;'>8.5/10</h2>", unsafe_allow_html=True)
                st.caption("Good job! Minor tense errors")
        
        with feedback_cols[1]:
            with stylable_container(
                key="feedback_vocab",
                css_styles="""
                {
                    background: #f3e5f5;
                    border-radius: 10px;
                    padding: 15px;
                }
                """
            ):
                st.markdown("**Vocabulary**")
                st.markdown("<h2 style='color: #7b1fa2;'>7/10</h2>", unsafe_allow_html=True)
                st.caption("Try using more varied words")
        
        with feedback_cols[2]:
            with stylable_container(
                key="feedback_fluency",
                css_styles="""
                {
                    background: #e8f5e9;
                    border-radius: 10px;
                    padding: 15px;
                }
                """
            ):
                st.markdown("**Fluency**")
                st.markdown("<h2 style='color: #388e3c;'>9/10</h2>", unsafe_allow_html=True)
                st.caption("Very natural flow!")

def generate_ai_response(user_input, topic):
    """Generate AI response based on topic"""
    responses = {
        "Restaurant": [
            f"That's a good order! For '{user_input}', would you like any drinks with that?",
            "Excellent choice! How would you like your steak cooked?",
            "I'll get that order started for you. Would you like to see the dessert menu?"
        ],
        "Travel": [
            "That's a great question! Could you tell me what kind of places you're interested in?",
            "I'd be happy to help with that! How many days will you be staying?",
            f"For '{user_input}', I recommend checking out the city center first."
        ],
        "Business": [
            "That's a good answer! Could you tell me more about your experience?",
            "Interesting! What challenges have you faced in previous roles?",
            f"Regarding '{user_input}', how do you handle pressure in the workplace?"
        ]
    }
    
    default_responses = [
        "Great point! Could you elaborate on that?",
        "I understand. How do you feel about that?",
        "That's interesting! What makes you say that?",
        "Good observation! Can you give me an example?",
        "I see. What do you think would happen next?"
    ]
    
    if topic in responses:
        return random.choice(responses[topic])
    else:
        return random.choice(default_responses)

# Enhanced pronunciation trainer
def render_pronunciation():
    st.markdown("## 🎤 Pronunciation Mastery")
    
    # Voice analyzer visualization
    st.markdown("### 🎵 Voice Analyzer")
    
    # Create waveform visualization
    fig = go.Figure()
    
    # Simulated waveform
    import numpy as np
    x = np.linspace(0, 4*np.pi, 1000)
    y = np.sin(x) * np.random.rand(1000)
    
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', 
                            line=dict(color='#667eea', width=2),
                            fill='tozeroy', fillcolor='rgba(102, 126, 234, 0.2)'))
    
    fig.update_layout(height=200, showlegend=False, 
                     margin=dict(l=0, r=0, t=0, b=0),
                     paper_bgcolor='rgba(0,0,0,0)',
                     plot_bgcolor='rgba(0,0,0,0)',
                     xaxis=dict(showgrid=False, zeroline=False),
                     yaxis=dict(showgrid=False, zeroline=False))
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Practice phrases
    st.markdown("### 🗣️ Practice Phrases")
    
    difficulty_levels = {
        "Easy": ["Hello, how are you?", "Thank you very much", "I love learning English"],
        "Medium": ["She sells seashells by the seashore", "Unique New York", "Red leather, yellow leather"],
        "Hard": ["Peter Piper picked a peck of pickled peppers", "How can a clam cram in a clean cream can?"]
    }
    
    selected_level = st.selectbox("Select Difficulty", list(difficulty_levels.keys()))
    
    # Display phrases in cards
    cols = st.columns(3)
    phrases = difficulty_levels[selected_level]
    
    for idx, phrase in enumerate(phrases):
        with cols[idx]:
            with stylable_container(
                key=f"phrase_{idx}",
                css_styles="""
                {
                    background: #f8f9fa;
                    border-radius: 15px;
                    padding: 20px;
                    text-align: center;
                    height: 200px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                }
                """
            ):
                st.markdown(f"<h3 style='font-size: 1.5rem; margin-bottom: 20px;'>\"{phrase}\"</h3>", unsafe_allow_html=True)
                
                col_a, col_b = st.columns(2)
                with col_a:
                    if st.button("🎤 Record", key=f"rec_{idx}"):
                        st.session_state.current_phrase = phrase
                        st.success(f"Recording: {phrase}")
                with col_b:
                    if st.button("▶️ Listen", key=f"play_{idx}"):
                        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    
    # Pronunciation feedback
    if 'current_phrase' in st.session_state:
        st.divider()
        st.markdown(f"### 📊 Analysis: \"{st.session_state.current_phrase}\"")
        
        # Score metrics
        col1, col2, col3, col4 = st.columns(4)
        
        metrics = [
            {"name": "Clarity", "score": 85, "color": "#4CAF50"},
            {"name": "Pace", "score": 70, "color": "#2196F3"},
            {"name": "Pitch", "score": 90, "color": "#9C27B0"},
            {"name": "Accent", "score": 65, "color": "#FF9800"}
        ]
        
        for idx, metric in enumerate(metrics):
            with [col1, col2, col3, col4][idx]:
                st.markdown(f"**{metric['name']}**")
                st.markdown(f"<h2 style='color: {metric['color']};'>{metric['score']}%</h2>", unsafe_allow_html=True)
                st.progress(metric['score'] / 100)
        
        # Detailed feedback
        st.markdown("#### 💡 Improvement Tips")
        
        tips = [
            "🗣️ **Slow down slightly** - Your pace is 12% faster than native speakers",
            "👄 **Focus on 'th' sounds** - Practice 'the', 'that', 'this'",
            "🎵 **Vary your pitch** - Try more rising intonation for questions",
            "👂 **Listen and repeat** - Mimic native speaker recordings"
        ]
        
        for tip in tips:
            with stylable_container(
                key=f"tip_{tip[:10]}",
                css_styles="""
                {
                    background: #fff3cd;
                    border-radius: 10px;
                    padding: 15px;
                    margin: 10px 0;
                    border-left: 4px solid #ffc107;
                }
                """
            ):
                st.markdown(tip)

# Enhanced vocabulary builder
def render_vocabulary():
    st.markdown("## 📚 Smart Vocabulary Builder")
    
    # Interactive word explorer
    tab1, tab2, tab3, tab4 = st.tabs(["✨ Word of Day", "📖 My Words", "🎮 Word Games", "📈 Progress"])
    
    with tab1:
        # Word of the day with rich content
        word_data = {
            "word": "Ephemeral",
            "phonetic": "/ɪˈfem.ər.əl/",
            "meaning": "Lasting for a very short time",
            "example": "The beauty of cherry blossoms is ephemeral, lasting only a week or two.",
            "synonyms": ["transient", "brief", "fleeting", "short-lived"],
            "antonyms": ["permanent", "enduring", "eternal"],
            "origin": "From Greek 'ephēmeros' meaning 'lasting a day'",
            "category": "Adjective",
            "difficulty": "Advanced"
        }
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            with stylable_container(
                key="word_of_day",
                css_styles="""
                {
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    border-radius: 20px;
                    padding: 30px;
                    color: white;
                }
                """
            ):
                st.markdown(f"<h1 style='font-size: 3rem; margin-bottom: 0;'>{word_data['word']}</h1>", unsafe_allow_html=True)
                st.markdown(f"*{word_data['phonetic']}*")
                st.markdown(f"**{word_data['category']}** • {word_data['difficulty']}")
                
                st.divider()
                
                st.markdown(f"### 📖 Meaning")
                st.markdown(word_data['meaning'])
                
                st.markdown(f"### 💬 Example")
                st.markdown(f"> *\"{word_data['example']}\"*")
        
        with col2:
            # Word details
            with stylable_container(
                key="word_details",
                css_styles="""
                {
                    background: white;
                    border-radius: 15px;
                    padding: 20px;
                    box-shadow: 0 5px 20px rgba(0,0,0,0.1);
                }
                """
            ):
                st.markdown("### 📝 Details")
                
                st.markdown("**Synonyms**")
                for syn in word_data['synonyms']:
                    st.markdown(f"`{syn}`")
                
                st.markdown("**Antonyms**")
                for ant in word_data['antonyms']:
                    st.markdown(f"`{ant}`")
                
                st.markdown("**Origin**")
                st.caption(word_data['origin'])
                
                if st.button("➕ Add to My Words", use_container_width=True):
                    if word_data not in st.session_state.vocabulary:
                        st.session_state.vocabulary.append(word_data)
                        st.success("Word added!")
    
    with tab2:
        # User's vocabulary with search and filter
        search_col, filter_col = st.columns([3, 1])
        with search_col:
            search_term = st.text_input("🔍 Search your words...")
        with filter_col:
            filter_by = st.selectbox("Filter by", ["All", "Beginner", "Intermediate", "Advanced"])
        
        if st.session_state.vocabulary:
            # Display words in grid
            cols = st.columns(3)
            for idx, word in enumerate(st.session_state.vocabulary):
                with cols[idx % 3]:
                    with stylable_container(
                        key=f"word_card_{idx}",
                        css_styles="""
                        {
                            background: white;
                            border-radius: 15px;
                            padding: 20px;
                            margin-bottom: 20px;
                            box-shadow: 0 3px 10px rgba(0,0,0,0.08);
                            border: 1px solid #e0e0e0;
                        }
                        """
                    ):
                        st.markdown(f"**{word['word']}**")
                        st.caption(f"*{word['phonetic']}*")
                        st.write(word['meaning'][:50] + "...")
                        
                        # Mastery slider
                        mastery = st.slider("Mastery", 0, 100, 50, 
                                          key=f"mastery_{word['word']}")
                        st.progress(mastery / 100)
                        
                        col_a, col_b = st.columns(2)
                        with col_a:
                            if st.button("📖 Review", key=f"rev_{word['word']}"):
                                st.info(f"Reviewing {word['word']}")
                        with col_b:
                            if st.button("🗑️", key=f"del_{word['word']}"):
                                st.session_state.vocabulary.pop(idx)
                                st.rerun()
        else:
            st.info("No words yet. Start adding words from 'Word of the Day'!")
    
    with tab3:
        # Vocabulary games
        st.markdown("### 🎮 Word Games")
        
        game_col1, game_col2, game_col3 = st.columns(3)
        
        with game_col1:
            with stylable_container(
                key="game_1",
                css_styles="""
                {
                    background: linear-gradient(135deg, #FF9A8B 0%, #FF6A88 100%);
                    border-radius: 15px;
                    padding: 30px;
                    text-align: center;
                    color: white;
                    cursor: pointer;
                    transition: all 0.3s ease;
                }
                :hover {
                    transform: scale(1.05);
                }
                """
            ):
                st.markdown("<h1>🔤</h1>", unsafe_allow_html=True)
                st.markdown("**Word Match**")
                st.caption("Match words with meanings")
                if st.button("Play Now", key="game1"):
                    st.info("Starting Word Match...")
        
        with game_col2:
            with stylable_container(
                key="game_2",
                css_styles="""
                {
                    background: linear-gradient(135deg, #42E695 0%, #3BB2B8 100%);
                    border-radius: 15px;
                    padding: 30px;
                    text-align: center;
                    color: white;
                }
                """
            ):
                st.markdown("<h1>🧩</h1>", unsafe_allow_html=True)
                st.markdown("**Fill-in Blanks**")
                st.caption("Complete sentences")
                if st.button("Play Now", key="game2"):
                    st.info("Starting Fill-in Blanks...")
        
        with game_col3:
            with stylable_container(
                key="game_3",
                css_styles="""
                {
                    background: linear-gradient(135deg, #FFD26F 0%, #3677FF 100%);
                    border-radius: 15px;
                    padding: 30px;
                    text-align: center;
                    color: white;
                }
                """
            ):
                st.markdown("<h1>⚡</h1>", unsafe_allow_html=True)
                st.markdown("**Speed Quiz**")
                st.caption("Test your knowledge")
                if st.button("Play Now", key="game3"):
                    st.info("Starting Speed Quiz...")

# Main app flow
def main():
    init_session_state()
    
    # Add confetti on achievements
    if 'show_confetti' in st.session_state and st.session_state.show_confetti:
        rain(
            emoji="🎉",
            font_size=30,
            falling_speed=5,
            animation_length=1,
        )
        st.session_state.show_confetti = False
    
    # Top bar with user info
    col1, col2, col3 = st.columns([6, 1, 1])
    
    with col1:
        st.markdown("<h1 style='margin: 0;'>🎓 English Practice Partner</h1>", unsafe_allow_html=True)
    
    with col2:
        st.metric("🔥", st.session_state.streak_days)
    
    with col3:
        st.metric("🎖️", st.session_state.total_points)
    
    # Main content area with sidebar
    main_col1, main_col2 = st.columns([3, 1])
    
    with main_col1:
        # Page routing
        if 'current_page' not in st.session_state:
            st.session_state.current_page = "Dashboard"
        
        if st.session_state.current_page == "Dashboard":
            render_dashboard()
        elif st.session_state.current_page == "Conversation":
            render_conversation()
        elif st.session_state.current_page == "Pronunciation":
            render_pronunciation()
        elif st.session_state.current_page == "Vocabulary":
            render_vocabulary()
        elif st.session_state.current_page == "Grammar":
            render_grammar()
        elif st.session_state.current_page == "Progress":
            render_progress()
        elif st.session_state.current_page == "Games":
            render_games()
        elif st.session_state.current_page == "Settings":
            render_settings()
    
    with main_col2:
        render_sidebar()

# Additional pages (simplified versions)
def render_grammar():
    st.markdown("## 📝 Grammar Mastery")
    # Add grammar exercises here
    st.info("Grammar exercises coming soon!")

def render_progress():
    st.markdown("## 📈 Learning Analytics")
    # Add detailed progress charts
    st.info("Detailed analytics coming soon!")

def render_games():
    st.markdown("## 🎮 Learning Games")
    # Add educational games
    st.info("Interactive games coming soon!")

def render_settings():
    st.markdown("## ⚙️ Settings")
    # Add user settings
    st.info("Settings panel coming soon!")

if __name__ == "__main__":
    main()