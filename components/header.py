import streamlit as st
import datetime

def render_header():
    col1, col2, col3 = st.columns([3, 2, 1])
    
    with col1:
        st.markdown("""
        <h1 class='gradient-text' style='margin: 0;'>🎓 English Practice Partner</h1>
        <p style='color: #666; margin: 0;'>Your AI-powered English learning companion</p>
        """, unsafe_allow_html=True)
    
    with col2:
        today = datetime.datetime.now().strftime("%A, %B %d")
        st.markdown(f"""
        <div style='text-align: center; padding: 10px; background: #f8f9fa; border-radius: 10px;'>
            <p style='margin: 0; color: #667eea; font-weight: bold;'>{today}</p>
            <p style='margin: 0; font-size: 0.8em; color: #666;'>Daily Goal: 30min</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"""
            <div style='text-align: center;'>
                <p style='margin: 0; font-size: 0.8em; color: #666;'>Streak</p>
                <h3 style='margin: 0; color: #ff6b6b;'>🔥 {st.session_state.user_stats['streak']}</h3>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown(f"""
            <div style='text-align: center;'>
                <p style='margin: 0; font-size: 0.8em; color: #666;'>Points</p>
                <h3 style='margin: 0; color: #4CAF50;'>🎖️ {st.session_state.user_stats['points']}</h3>
            </div>
            """, unsafe_allow_html=True)
    
    st.divider()