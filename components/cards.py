import streamlit as st
import streamlit.components.v1 as components

def create_feature_card(title, description, icon, color="#667eea", action=None):
    """Create a beautiful feature card"""
    html = f"""
    <div style='
        background: linear-gradient(135deg, {color}15 0%, {color}05 100%);
        border-radius: 20px;
        padding: 25px;
        border: 2px solid {color}30;
        margin: 15px 0;
        transition: all 0.3s ease;
        cursor: pointer;
        height: 100%;
    '
    onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 15px 35px rgba(0,0,0,0.1)';"
    onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';">
        <div style='font-size: 48px; margin-bottom: 15px;'>{icon}</div>
        <h3 style='margin: 0 0 10px 0; color: #333;'>{title}</h3>
        <p style='color: #666; margin: 0;'>{description}</p>
    </div>
    """
    
    col = st.columns(1)[0]
    with col:
        components.html(html, height=200)
        
        if action and st.button("Try Now", key=f"btn_{title}", use_container_width=True):
            action()

def create_progress_card(title, current, total, icon="📊"):
    """Create a progress card"""
    progress = current / total
    color = "#4CAF50" if progress >= 0.7 else "#FF9800" if progress >= 0.4 else "#F44336"
    
    html = f"""
    <div style='
        background: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.05);
        margin: 10px 0;
    '>
        <div style='display: flex; align-items: center; margin-bottom: 15px;'>
            <div style='font-size: 24px; margin-right: 15px;'>{icon}</div>
            <div>
                <h4 style='margin: 0; color: #333;'>{title}</h4>
                <p style='margin: 5px 0 0 0; color: #666; font-size: 0.9em;'>
                    {current} of {total} complete
                </p>
            </div>
        </div>
        <div style='
            background: #f0f0f0;
            border-radius: 10px;
            height: 8px;
            overflow: hidden;
        '>
            <div style='
                background: {color};
                height: 100%;
                width: {progress * 100}%;
                border-radius: 10px;
                transition: width 0.5s ease;
            '></div>
        </div>
        <div style='
            display: flex;
            justify-content: space-between;
            margin-top: 10px;
            color: #666;
            font-size: 0.9em;
        '>
            <span>0%</span>
            <span>{int(progress * 100)}%</span>
            <span>100%</span>
        </div>
    </div>
    """
    
    components.html(html, height=150)