import streamlit as st
import pandas as pd
import plotly.express as px
from components.cards import create_feature_card, create_stats_card
from components.charts import create_activity_chart, create_skill_radar, create_progress_timeline
import streamlit.components.v1 as components

def render():
    st.markdown("## 📊 Learning Dashboard")
    
    # Top stats row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(create_stats_card("Streak Days", "7", "+2", "🔥", "#FF6B6B"), 
                   unsafe_allow_html=True)
    
    with col2:
        st.markdown(create_stats_card("Total Points", "1,250", "+150", "🎖️", "#4CAF50"), 
                   unsafe_allow_html=True)
    
    with col3:
        st.markdown(create_stats_card("Practice Time", "45min", "+15min", "⏱️", "#2196F3"), 
                   unsafe_allow_html=True)
    
    with col4:
        st.markdown(create_stats_card("Vocabulary", "42 words", "+5", "📚", "#9C27B0"), 
                   unsafe_allow_html=True)
    
    # Charts section
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.markdown("### 📈 Weekly Activity")
        st.plotly_chart(create_activity_chart(), use_container_width=True)
        
        st.markdown("### 📅 Progress Timeline")
        st.plotly_chart(create_progress_timeline(), use_container_width=True)
    
    with col_right:
        st.markdown("### 🎯 Skill Radar")
        st.plotly_chart(create_skill_radar(), use_container_width=True)
        
        st.markdown("### 🏆 Recent Achievements")
        
        achievements = [
            {"icon": "🥇", "title": "7-Day Streak", "desc": "Practiced 7 days in a row"},
            {"icon": "💬", "title": "Chat Master", "desc": "Completed 10 conversations"},
            {"icon": "🎤", "title": "Pronunciation Pro", "desc": "Achieved 90% pronunciation score"},
            {"icon": "📚", "title": "Word Collector", "desc": "Learned 50 new words"},
        ]
        
        for ach in achievements:
            with st.container():
                col_a, col_b = st.columns([1, 4])
                with col_a:
                    st.markdown(f"<h2>{ach['icon']}</h2>", unsafe_allow_html=True)
                with col_b:
                    st.write(f"**{ach['title']}**")
                    st.caption(ach['desc'])
                st.divider()
    
    # Features section
    st.markdown("## 🚀 Quick Start")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        create_feature_card(
            "AI Conversation",
            "Practice real conversations with our AI tutor",
            "💬",
            "#667eea",
            "Start Chat",
            lambda: st.session_state.update({"page": "Conversation"})
        )
    
    with col2:
        create_feature_card(
            "Pronunciation",
            "Improve your accent and pronunciation",
            "🎤",
            "#4CAF50",
            "Practice Now",
            lambda: st.session_state.update({"page": "Pronunciation"})
        )
    
    with col3:
        create_feature_card(
            "Vocabulary Builder",
            "Learn new words with context",
            "📚",
            "#FF9800",
            "Learn Words",
            lambda: st.session_state.update({"page": "Vocabulary"})
        )
    
    # Daily challenge
    st.markdown("## 🎯 Daily Challenge")
    
    with st.container():
        st.info("""
        **Today's Challenge:** Have a 5-minute conversation about your favorite hobby.
        - Speak for at least 5 minutes
        - Use at least 3 new vocabulary words
        - Focus on correct tense usage
        
        **Reward:** 50 points + 🏆 Achievement
        """)
        
        if st.button("Start Daily Challenge", type="primary", use_container_width=True):
            st.session_state.page = "Conversation"
            st.rerun()