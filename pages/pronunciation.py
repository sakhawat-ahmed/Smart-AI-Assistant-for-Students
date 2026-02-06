import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time
from components.cards import create_feature_card

def render():
    st.markdown("## 🎤 Pronunciation Trainer")
    
    # Introduction
    st.info("""
    **Improve your English pronunciation with real-time feedback.**
    Practice difficult sounds, word stress, and intonation patterns.
    """)
    
    # Main practice area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🗣️ Practice Phrases")
        
        # Difficulty selection
        difficulty = st.selectbox(
            "Select difficulty level",
            ["Beginner", "Intermediate", "Advanced"],
            index=1
        )
        
        # Phrases by difficulty
        phrases = {
            "Beginner": [
                "Hello, how are you today?",
                "I would like a cup of coffee.",
                "Where is the nearest station?",
                "Thank you very much for your help.",
                "Could you repeat that, please?"
            ],
            "Intermediate": [
                "The quick brown fox jumps over the lazy dog.",
                "She sells seashells by the seashore.",
                "Peter Piper picked a peck of pickled peppers.",
                "How much wood would a woodchuck chuck?",
                "Unique New York, New York's unique."
            ],
            "Advanced": [
                "The sixth sick sheik's sixth sheep's sick.",
                "Betty Botter bought some butter.",
                "Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair.",
                "I slit the sheet, the sheet I slit, and on the slitted sheet I sit.",
                "Six thick thistle sticks."
            ]
        }
        
        selected_phrases = phrases.get(difficulty, phrases["Intermediate"])
        
        # Display phrases
        for i, phrase in enumerate(selected_phrases):
            col_a, col_b = st.columns([4, 1])
            with col_a:
                st.markdown(f"**{i+1}. {phrase}**")
            with col_b:
                if st.button("🎤 Practice", key=f"phrase_{i}"):
                    st.session_state.current_phrase = phrase
                    st.session_state.recording = True
                    st.success(f"Recording: '{phrase}'")
    
    with col2:
        st.markdown("### 🎯 Target Sounds")
        
        sounds = [
            ("θ", "th (think)", "Voiceless dental fricative"),
            ("ð", "th (this)", "Voiced dental fricative"),
            ("r", "r (red)", "Alveolar approximant"),
            ("l", "l (light)", "Alveolar lateral approximant"),
            ("ʃ", "sh (she)", "Voiceless postalveolar fricative"),
            ("ʒ", "s (measure)", "Voiced postalveolar fricative"),
        ]
        
        for symbol, example, description in sounds:
            with st.expander(f"{symbol} - {example}"):
                st.write(description)
                if st.button(f"Practice {symbol}", key=f"sound_{symbol}"):
                    st.info(f"Practice words with '{symbol}' sound")
    
    # Recording and feedback
    if 'current_phrase' in st.session_state:
        st.divider()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"### 📝 Current Practice")
            st.markdown(f"**Phrase:** {st.session_state.current_phrase}")
            
            # Recording controls
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                if st.button("⏺️ Record", type="primary", use_container_width=True):
                    st.session_state.recording = True
                    st.success("Recording started... Speak now!")
            
            with col_b:
                if st.button("⏸️ Pause", use_container_width=True):
                    st.session_state.recording = False
                    st.info("Recording paused")
            
            with col_c:
                if st.button("▶️ Playback", use_container_width=True):
                    st.info("Playing back your recording...")
        
        with col2:
            st.markdown("### 📊 Analysis")
            
            # Simulated analysis metrics
            metrics = {
                "Clarity": {"score": 85, "feedback": "Clear pronunciation"},
                "Pace": {"score": 70, "feedback": "Slightly fast, try slowing down"},
                "Pitch": {"score": 90, "feedback": "Good intonation"},
                "Accuracy": {"score": 80, "feedback": "Minor vowel sound issues"}
            }
            
            for metric, data in metrics.items():
                st.write(f"**{metric}:** {data['score']}%")
                st.progress(data['score'] / 100)
                st.caption(data['feedback'])
    
    # Waveform visualization
    st.divider()
    st.markdown("### 📈 Voice Waveform")
    
    # Create simulated waveform
    x = np.linspace(0, 4 * np.pi, 1000)
    y = np.sin(x) * np.random.rand(1000)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines',
        fill='tozeroy',
        fillcolor='rgba(102, 126, 234, 0.2)',
        line=dict(color='#667eea', width=2)
    ))
    
    fig.update_layout(
        height=200,
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis=dict(showgrid=False, showticklabels=False),
        yaxis=dict(showgrid=False, showticklabels=False),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Pronunciation tips
    st.markdown("### 💡 Pronunciation Tips")
    
    tips = [
        "🎯 **Slow down** - Native speakers often speak slower than learners think",
        "👂 **Listen carefully** to how native speakers pronounce words",
        "🎵 **Pay attention to stress** - English is a stress-timed language",
        "👄 **Practice difficult sounds** in isolation first",
        "📱 **Use mirror practice** to watch your mouth movements",
        "🎧 **Record and compare** with native speaker audio"
    ]
    
    for tip in tips:
        st.markdown(f"- {tip}")
    
    # Practice exercises
    st.divider()
    st.markdown("### 🏋️ Practice Exercises")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        create_feature_card(
            "Minimal Pairs",
            "Practice similar sounding words",
            "🔤",
            "#4CAF50",
            "Start Exercise",
            lambda: st.info("Minimal pairs exercise started")
        )
    
    with col2:
        create_feature_card(
            "Tongue Twisters",
            "Improve articulation and speed",
            "🌀",
            "#2196F3",
            "Start Exercise",
            lambda: st.info("Tongue twisters exercise started")
        )
    
    with col3:
        create_feature_card(
            "Sentence Stress",
            "Learn word emphasis patterns",
            "⚖️",
            "#FF9800",
            "Start Exercise",
            lambda: st.info("Sentence stress exercise started")
        )