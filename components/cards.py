import streamlit as st
import plotly.graph_objects as go

def create_feature_card(title, description, icon, color="#667eea", button_text="Try Now", button_callback=None):
    """Create a feature card"""
    html = f"""
    <div class="feature-card">
        <div style="font-size: 48px; margin-bottom: 15px; color: {color};">{icon}</div>
        <h3 style="margin: 0 0 10px 0; color: #333;">{title}</h3>
        <p style="color: #666; margin: 0 0 20px 0;">{description}</p>
    </div>
    """
    
    col = st.columns(1)[0]
    with col:
        st.markdown(html, unsafe_allow_html=True)
        if button_callback and st.button(button_text, key=f"btn_{title}", use_container_width=True):
            button_callback()

def create_stats_card(title, value, change=None, icon="📊", color="#667eea"):
    """Create a stats card"""
    change_html = ""
    if change:
        change_color = "#4CAF50" if change.startswith("+") else "#F44336"
        change_html = f'<span style="color: {change_color}; font-size: 0.8em;">{change}</span>'
    
    html = f"""
    <div style="background: white; border-radius: 15px; padding: 20px; 
                box-shadow: 0 5px 15px rgba(0,0,0,0.05); border-left: 4px solid {color};">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h4 style="margin: 0; color: #666; font-size: 0.9em;">{title}</h4>
                <h2 style="margin: 10px 0; color: #333;">{icon} {value}</h2>
                {change_html}
            </div>
        </div>
    </div>
    """
    
    return html

def create_progress_card(title, current, total, color="#667eea"):
    """Create a progress card"""
    progress = (current / total) * 100 if total > 0 else 0
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=progress,
        number={'suffix': "%"},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': color},
            'steps': [
                {'range': [0, 100], 'color': "#f0f0f0"}
            ],
        }
    ))
    
    fig.update_layout(height=150, margin=dict(l=10, r=10, t=10, b=10))
    
    return fig