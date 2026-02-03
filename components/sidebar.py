import streamlit as st
import plotly.graph_objects as go

def render_sidebar():
    # User profile
    st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <div style='width: 80px; height: 80px; background: linear-gradient(45deg, #667eea, #764ba2); 
             border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; 
             font-size: 30px; color: white; margin-bottom: 10px;'>
            👤
        </div>
        <h4 style='margin: 5px 0;'>{}</h4>
        <div style='background: #e3f2fd; color: #1976d2; padding: 5px 15px; border-radius: 20px; 
             display: inline-block; font-size: 0.8em; margin: 5px 0;'>
            {}
        </div>
    </div>
    """.format(st.session_state.username, st.session_state.user_stats['level']), unsafe_allow_html=True)
    
    st.divider()
    
    # Daily progress
    st.markdown("### 🎯 Daily Progress")
    progress = min(st.session_state.user_stats['practice_time'] / 30, 1)
    
    # Progress donut chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=progress * 100,
        number={'suffix': "%"},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': "#667eea"},
            'steps': [
                {'range': [0, 100], 'color': "#f0f0f0"}
            ],
        }
    ))
    
    fig.update_layout(height=150, margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig, use_container_width=True)
    
    st.caption(f"{st.session_state.user_stats['practice_time']}/30 minutes completed")
    
    st.divider()
    
    # Quick stats
    st.markdown("### 📊 Quick Stats")
    
    stats = [
        ("⏱️", "Practice Time", f"{st.session_state.user_stats['practice_time']} min"),
        ("📚", "Vocabulary", f"{st.session_state.user_stats['vocabulary']} words"),
        ("💬", "Conversations", "12 sessions"),
        ("🎯", "Accuracy", "85%")
    ]
    
    for icon, label, value in stats:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown(f"<h3>{icon}</h3>", unsafe_allow_html=True)
        with col2:
            st.write(label)
            st.markdown(f"**{value}**")
    
    st.divider()
    
    # Quick actions
    st.markdown("### ⚡ Quick Actions")
    
    if st.button("🎤 Start Speaking Practice", use_container_width=True):
        st.session_state.page = "Pronunciation"
        st.rerun()
    
    if st.button("💬 New Conversation", use_container_width=True):
        st.session_state.page = "Conversation"
        st.rerun()
    
    if st.button("📚 Learn New Words", use_container_width=True):
        st.session_state.page = "Vocabulary"
        st.rerun()
    
    st.divider()
    
    # Settings
    if st.button("⚙️ Settings", use_container_width=True):
        st.info("Settings panel coming soon!")