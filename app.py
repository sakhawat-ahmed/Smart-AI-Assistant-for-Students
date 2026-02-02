import streamlit as st
from streamlit_option_menu import option_menu
import pages.dashboard as dashboard
import pages.conversation as conversation
import pages.pronunciation as pronunciation
import pages.vocabulary as vocabulary
import pages.grammar as grammar
import pages.progress as progress_page
from utils.database import init_db, get_user_stats
from components.header import render_header
from components.sidebar import render_sidebar
import time

# Page configuration
st.set_page_config(
    page_title="English Practice Partner | AI Tutor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    /* Main styles */
    .main {
        padding: 0;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(45deg, #667eea, #764ba2);
        border-radius: 10px;
    }
    
    /* Gradient text */
    .gradient-text {
        background: linear-gradient(45deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Card styles */
    .feature-card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        height: 100%;
        border: 1px solid #f0f0f0;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.12);
    }
    
    /* Stats card */
    .stats-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
def init_session_state():
    if 'page' not in st.session_state:
        st.session_state.page = "Dashboard"
    if 'user_stats' not in st.session_state:
        st.session_state.user_stats = {
            'streak': 7,
            'points': 1250,
            'practice_time': 45,
            'vocabulary': 42,
            'level': 'B1 Intermediate'
        }
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []
    if 'vocabulary_list' not in st.session_state:
        st.session_state.vocabulary_list = []
    if 'username' not in st.session_state:
        st.session_state.username = "Student"

# Main app
def main():
    init_session_state()
    
    # Initialize database
    init_db()
    
    # Render header
    render_header()
    
    # Sidebar navigation
    with st.sidebar:
        selected = option_menu(
            menu_title="Navigation",
            options=["Dashboard", "Conversation", "Pronunciation", "Vocabulary", "Grammar", "Progress"],
            icons=['house', 'chat', 'mic', 'book', 'pencil', 'graph-up'],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#f8f9fa"},
                "icon": {"color": "#667eea", "font-size": "18px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#e0e0e0",
                },
                "nav-link-selected": {"background-color": "#667eea"},
            }
        )
        
        # Render sidebar content
        render_sidebar()
    
    # Main content area
    if selected == "Dashboard":
        dashboard.render()
    elif selected == "Conversation":
        conversation.render()
    elif selected == "Pronunciation":
        pronunciation.render()
    elif selected == "Vocabulary":
        vocabulary.render()
    elif selected == "Grammar":
        grammar.render()
    elif selected == "Progress":
        progress_page.render()

if __name__ == "__main__":
    main()