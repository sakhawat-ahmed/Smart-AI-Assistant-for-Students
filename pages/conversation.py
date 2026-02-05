import streamlit as st
import time
import random
from datetime import datetime
from components.cards import create_feature_card

def render():
    st.markdown("## 💬 AI Conversation Practice")
    
    # Topic selection
    st.markdown("### 🎯 Choose a Topic")
    
    topics = [
        {"icon": "🍽️", "name": "Restaurant", "scenes": ["Ordering food", "Making reservations", "Complaining"]},
        {"icon": "✈️", "name": "Travel", "scenes": ["Airport check-in", "Hotel booking", "Asking directions"]},
        {"icon": "💼", "name": "Business", "scenes": ["Job interview", "Business meeting", "Email writing"]},
        {"icon": "🛒", "name": "Shopping", "scenes": ["Clothes shopping", "Electronics", "Returns & exchanges"]},
        {"icon": "🏥", "name": "Healthcare", "scenes": ["Doctor's visit", "Pharmacy", "Symptoms description"]},
        {"icon": "🎬", "name": "Entertainment", "scenes": ["Movies & TV", "Music", "Books & reading"]},
    ]
    
    cols = st.columns(3)
    for idx, topic in enumerate(topics):
        with cols[idx % 3]:
            if st.button(
                f"{topic['icon']} {topic['name']}",
                use_container_width=True,
                key=f"topic_{idx}"
            ):
                st.session_state.selected_topic = topic
                st.rerun()
    
    # Conversation interface
    if 'selected_topic' in st.session_state:
        topic = st.session_state.selected_topic
        
        st.divider()
        
        # Topic header
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"### {topic['icon']} {topic['name']}")
            st.caption(" | ".join(topic['scenes']))
        with col2:
            if st.button("🔁 Change Topic"):
                del st.session_state.selected_topic
                st.rerun()
        
        # Role assignment
        st.markdown("#### 🎭 Role Play")
        roles = {
            "Restaurant": ["You: Customer", "AI: Waiter"],
            "Travel": ["You: Tourist", "AI: Travel Agent"],
            "Business": ["You: Job Applicant", "AI: Interviewer"],
            "Shopping": ["You: Customer", "AI: Sales Assistant"],
            "Healthcare": ["You: Patient", "AI: Doctor"],
            "Entertainment": ["You: Movie Buff", "AI: Friend"]
        }
        
        role = roles.get(topic['name'], ["You: Student", "AI: Tutor"])
        col_a, col_b = st.columns(2)
        with col_a:
            st.info(role[0])
        with col_b:
            st.success(role[1])
        
        # Chat interface
        if 'messages' not in st.session_state:
            st.session_state.messages = [
                {"role": "ai", "content": f"Hello! I'll be your {role[1].split(': ')[1].lower()} today. How can I help you?", "time": "Now"}
            ]
        
        # Display chat
        chat_container = st.container()
        with chat_container:
            for msg in st.session_state.messages:
                if msg['role'] == 'user':
                    st.markdown(f"""
                    <div style='display: flex; justify-content: flex-end; margin: 10px 0;'>
                        <div style='background: linear-gradient(45deg, #667eea, #764ba2); color: white; 
                             padding: 12px 18px; border-radius: 18px 18px 4px 18px; max-width: 70%;'>
                            {msg['content']}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style='display: flex; justify-content: flex-start; margin: 10px 0;'>
                        <div style='background: #f0f2f6; color: #333; padding: 12px 18px; 
                             border-radius: 18px 18px 18px 4px; max-width: 70%;'>
                            {msg['content']}
                            <div style='font-size: 0.8em; color: #666; margin-top: 5px;'>{msg['time']}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Input area
        st.divider()
        col1, col2 = st.columns([5, 1])
        
        with col1:
            user_input = st.text_input(
                "Type your message...",
                key="chat_input",
                placeholder=f"Speak as {role[0].split(': ')[1]}..."
            )
        
        with col2:
            if st.button("🎤 Speak", use_container_width=True, disabled=True):
                st.info("Voice input coming soon!")
        
        if user_input:
            # Add user message
            st.session_state.messages.append({
                "role": "user", 
                "content": user_input,
                "time": "Now"
            })
            
            # Generate AI response
            with st.spinner("AI is thinking..."):
                time.sleep(1)  # Simulate thinking
                ai_response = generate_ai_response(user_input, topic['name'])
                st.session_state.messages.append({
                    "role": "ai",
                    "content": ai_response,
                    "time": "Now"
                })
            
            # Add to conversation history
            st.session_state.conversation_history.append({
                "topic": topic['name'],
                "user_input": user_input,
                "ai_response": ai_response,
                "timestamp": datetime.now()
            })
            
            st.rerun()
        
        # Conversation tools
        st.divider()
        st.markdown("#### 🛠️ Conversation Tools")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📋 Get Feedback", use_container_width=True):
                st.info("""
                **Feedback:**
                - Good sentence structure
                - Good use of vocabulary
                - Suggestion: Try using more complex sentences
                """)
        
        with col2:
            if st.button("🔍 Grammar Check", use_container_width=True):
                st.success("""
                **Grammar Analysis:**
                - No major errors found
                - Suggestion: Use present perfect tense for recent actions
                """)
        
        with col3:
            if st.button("🔄 New Scene", use_container_width=True):
                st.session_state.messages = [
                    {"role": "ai", "content": f"Let's try a different scene. {random.choice(topic['scenes'])}", "time": "Now"}
                ]
                st.rerun()

def generate_ai_response(user_input, topic):
    """Generate AI response based on topic"""
    responses = {
        "Restaurant": [
            "That's a great choice! Would you like any drinks with your meal?",
            "I'll get that started for you. How would you like your steak cooked?",
            "The special today is grilled salmon. Would you like to hear about our desserts?"
        ],
        "Travel": [
            "That sounds like a wonderful destination! How many days will you be staying?",
            "I'd recommend visiting the city center first. What kind of activities interest you?",
            "For that destination, you'll need a visa. Have you checked the requirements?"
        ],
        "Business": [
            "That's impressive experience! Could you tell me more about your achievements?",
            "What challenges have you faced in previous roles and how did you overcome them?",
            "Where do you see yourself in five years?"
        ]
    }
    
    # Get topic-specific responses or use default
    topic_responses = responses.get(topic, [
        "Interesting! Tell me more about that.",
        "I see. How do you feel about that situation?",
        "That's a good point. What happened next?",
        "Could you elaborate on that?",
        "What do you think about trying a different approach?"
    ])
    
    return random.choice(topic_responses)