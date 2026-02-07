import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import random

def render():
    st.markdown("## 📈 Learning Progress")
    
    # Tabs for different progress views
    tab1, tab2, tab3 = st.tabs(["📊 Overview", "📅 Timeline", "🏆 Achievements"])
    
    with tab1:
        render_overview()
    
    with tab2:
        render_timeline()
    
    with tab3:
        render_achievements()

def render_overview():
    """Progress overview"""
    
    # Summary stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Practice", "45 hours", "+5 this week")
    
    with col2:
        st.metric("Words Learned", "156", "+12 this week")
    
    with col3:
        st.metric("Conversations", "42", "+5 this week")
    
    with col4:
        st.metric("Accuracy", "85%", "+2%")
    
    # Skill radar chart
    st.markdown("### 🎯 Skill Assessment")
    
    categories = ['Speaking', 'Listening', 'Vocabulary', 'Grammar', 'Pronunciation', 'Fluency']
    values = [85, 78, 92, 76, 82, 88]
    
    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        fillcolor='rgba(102, 126, 234, 0.2)',
        line_color='#667eea',
        line_width=2
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                gridcolor='lightgray',
                angle=90
            )),
        showlegend=False,
        height=400,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed skill breakdown
    st.markdown("### 📋 Skill Breakdown")
    
    skills_data = {
        'Skill': ['Speaking', 'Listening', 'Vocabulary', 'Grammar', 'Pronunciation', 'Fluency'],
        'Current': [85, 78, 92, 76, 82, 88],
        'Target': [90, 85, 95, 85, 90, 90]
    }
    
    df = pd.DataFrame(skills_data)
    
    fig = go.Figure(data=[
        go.Bar(name='Current Level', x=df['Skill'], y=df['Current'], marker_color='#667eea'),
        go.Bar(name='Target Level', x=df['Skill'], y=df['Target'], marker_color='#4CAF50', opacity=0.6)
    ])
    
    fig.update_layout(
        barmode='group',
        height=300,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)

def render_timeline():
    """Progress timeline"""
    
    # Generate sample timeline data
    dates = pd.date_range(start='2024-01-01', end='2024-01-30', freq='D')
    
    timeline_data = pd.DataFrame({
        'Date': dates,
        'Practice Minutes': [random.randint(15, 60) for _ in range(len(dates))],
        'New Words': [random.randint(0, 5) for _ in range(len(dates))],
        'Accuracy': [random.randint(70, 95) for _ in range(len(dates))]
    })
    
    # Practice time chart
    st.markdown("### ⏰ Practice Time")
    
    fig = px.line(timeline_data, x='Date', y='Practice Minutes',
                  title="Daily Practice Minutes",
                  markers=True)
    
    fig.update_traces(line_color='#667eea', line_width=3)
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=40, b=20))
    
    st.plotly_chart(fig, use_container_width=True)
    
    # New words chart
    st.markdown("### 📚 New Words Learned")
    
    fig = px.bar(timeline_data, x='Date', y='New Words',
                 title="Daily New Vocabulary Words")
    
    fig.update_traces(marker_color='#4CAF50')
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=40, b=20))
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Accuracy trend
    st.markdown("### 🎯 Accuracy Trend")
    
    fig = px.line(timeline_data, x='Date', y='Accuracy',
                  title="Daily Accuracy Percentage",
                  markers=True)
    
    fig.update_traces(line_color='#FF9800', line_width=3)
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=40, b=20))
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Weekly summary
    st.markdown("### 📅 Weekly Summary")
    
    # Create weekly data
    timeline_data['Week'] = timeline_data['Date'].dt.isocalendar().week
    weekly_summary = timeline_data.groupby('Week').agg({
        'Practice Minutes': 'sum',
        'New Words': 'sum',
        'Accuracy': 'mean'
    }).reset_index()
    
    weekly_summary['Week'] = 'Week ' + weekly_summary['Week'].astype(str)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Weekly Practice", f"{weekly_summary['Practice Minutes'].iloc[-1]} min")
    
    with col2:
        st.metric("Weekly Words", f"{weekly_summary['New Words'].iloc[-1]} words")
    
    with col3:
        st.metric("Weekly Accuracy", f"{weekly_summary['Accuracy'].iloc[-1]:.1f}%")

def render_achievements():
    """Achievements display"""
    
    st.markdown("### 🏆 Your Achievements")
    
    achievements = [
        {
            "icon": "🔥",
            "title": "7-Day Streak",
            "description": "Practiced for 7 consecutive days",
            "date": "2024-01-15",
            "unlocked": True,
            "points": 100
        },
        {
            "icon": "💬",
            "title": "Conversation Master",
            "description": "Completed 50 conversations",
            "date": "2024-01-20",
            "unlocked": True,
            "points": 150
        },
        {
            "icon": "📚",
            "title": "Vocabulary Collector",
            "description": "Learned 100 words",
            "date": "2024-01-25",
            "unlocked": True,
            "points": 200
        },
        {
            "icon": "🎤",
            "title": "Pronunciation Pro",
            "description": "Achieved 90% pronunciation score",
            "date": None,
            "unlocked": False,
            "points": 100
        },
        {
            "icon": "🌟",
            "title": "Grammar Guru",
            "description": "Scored 95% on grammar tests",
            "date": None,
            "unlocked": False,
            "points": 150
        },
        {
            "icon": "🚀",
            "title": "Speed Learner",
            "description": "Complete 30 days of practice",
            "date": None,
            "unlocked": False,
            "points": 300
        }
    ]
    
    # Display achievements in grid
    cols = st.columns(3)
    
    for idx, achievement in enumerate(achievements):
        with cols[idx % 3]:
            if achievement['unlocked']:
                bg_color = "#e8f5e9"
                border_color = "#4CAF50"
                date_text = f"Unlocked: {achievement['date']}"
            else:
                bg_color = "#f5f5f5"
                border_color = "#9e9e9e"
                date_text = "Locked"
            
            st.markdown(f"""
            <div style='background: {bg_color}; border: 2px solid {border_color}; 
                 border-radius: 15px; padding: 20px; text-align: center; margin-bottom: 20px;'>
                <div style='font-size: 40px; margin-bottom: 10px;'>{achievement['icon']}</div>
                <h4 style='margin: 10px 0;'>{achievement['title']}</h4>
                <p style='margin: 10px 0; font-size: 0.9em; color: #666;'>
                    {achievement['description']}
                </p>
                <div style='display: flex; justify-content: space-between; align-items: center; 
                     margin-top: 15px; font-size: 0.8em;'>
                    <span style='color: #666;'>{date_text}</span>
                    <span style='color: #FF9800; font-weight: bold;'>{achievement['points']} pts</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Points summary
    st.markdown("### 🎖️ Points Summary")
    
    unlocked_achievements = [a for a in achievements if a['unlocked']]
    total_points = sum(a['points'] for a in unlocked_achievements)
    possible_points = sum(a['points'] for a in achievements)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Total Points", f"{total_points}")
    
    with col2:
        st.metric("Possible Points", f"{possible_points}")
    
    # Progress towards next achievement
    st.markdown("### 🎯 Next Achievement")
    
    locked_achievements = [a for a in achievements if not a['unlocked']]
    if locked_achievements:
        next_achievement = locked_achievements[0]
        
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.markdown(f"<div style='font-size: 50px; text-align: center;'>{next_achievement['icon']}</div>", 
                       unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"**{next_achievement['title']}**")
            st.write(next_achievement['description'])
            st.progress(0.6)  # 60% progress
            st.caption("Complete 3 more pronunciation exercises to unlock!")
    
    # Milestone tracker
    st.markdown("### 📊 Milestone Tracker")
    
    milestones = [
        {"goal": "100 Practice Hours", "current": 45, "total": 100},
        {"goal": "500 Vocabulary Words", "current": 156, "total": 500},
        {"goal": "100 Conversations", "current": 42, "total": 100},
        {"goal": "30-Day Streak", "current": 7, "total": 30}
    ]
    
    for milestone in milestones:
        progress = milestone['current'] / milestone['total']
        
        st.write(f"**{milestone['goal']}**")
        st.progress(progress)
        
        col1, col2 = st.columns(2)
        with col1:
            st.caption(f"Current: {milestone['current']}")
        with col2:
            st.caption(f"Remaining: {milestone['total'] - milestone['current']}")