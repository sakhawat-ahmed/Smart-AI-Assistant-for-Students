import streamlit as st
import random
import pandas as pd
from datetime import datetime, timedelta

def render():
    st.markdown("## 📚 Vocabulary Builder")
    
    # Tabs for different vocabulary activities
    tab1, tab2, tab3, tab4 = st.tabs(["✨ Word of Day", "📖 My Words", "🎮 Word Games", "📈 Progress"])
    
    with tab1:
        render_word_of_day()
    
    with tab2:
        render_my_words()
    
    with tab3:
        render_word_games()
    
    with tab4:
        render_vocabulary_progress()

def render_word_of_day():
    """Word of the day section"""
    
    word_data = {
        "word": "Ubiquitous",
        "phonetic": "/juːˈbɪk.wɪ.təs/",
        "part_of_speech": "adjective",
        "meaning": "Present, appearing, or found everywhere",
        "example": "Mobile phones have become ubiquitous in modern society.",
        "synonyms": ["omnipresent", "pervasive", "universal", "everywhere"],
        "antonyms": ["rare", "scarce", "uncommon"],
        "origin": "Mid 19th century: from Latin ubique 'everywhere' + -ous.",
        "difficulty": "Intermediate",
        "category": "Formal"
    }
    
    # Word display
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
             color: white; padding: 30px; border-radius: 15px;'>
            <h1 style='margin: 0; font-size: 3rem;'>{word_data['word']}</h1>
            <p style='font-size: 1.2rem; margin: 10px 0;'><i>{word_data['phonetic']}</i></p>
            <div style='display: inline-block; background: rgba(255,255,255,0.2); 
                 padding: 5px 15px; border-radius: 20px; margin: 10px 0;'>
                {word_data['part_of_speech']} • {word_data['difficulty']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Meaning and example
        st.markdown(f"""
        ### 📖 Meaning
        {word_data['meaning']}
        
        ### 💬 Example
        > *"{word_data['example']}"*
        """)
    
    with col2:
        # Add to my words button
        if st.button("➕ Add to My Words", use_container_width=True, type="primary"):
            if 'vocabulary_list' not in st.session_state:
                st.session_state.vocabulary_list = []
            
            word_data['added_date'] = datetime.now()
            word_data['mastery'] = 0
            word_data['review_count'] = 0
            
            st.session_state.vocabulary_list.append(word_data)
            st.success(f"'{word_data['word']}' added to your vocabulary!")
        
        # Word details
        st.markdown("### 📝 Details")
        
        st.markdown("**Synonyms**")
        for syn in word_data['synonyms']:
            st.markdown(f"`{syn}`")
        
        st.markdown("**Antonyms**")
        for ant in word_data['antonyms']:
            st.markdown(f"`{ant}`")
        
        st.markdown("**Origin**")
        st.caption(word_data['origin'])
        
        # Practice button
        if st.button("🔄 Practice This Word", use_container_width=True):
            st.info("Practice session started with 'Ubiquitous'")

def render_my_words():
    """User's vocabulary list"""
    
    st.markdown("### 📖 My Vocabulary Collection")
    
    # Search and filter
    col1, col2, col3 = st.columns([3, 2, 1])
    
    with col1:
        search_term = st.text_input("🔍 Search words...", placeholder="Type to search your words")
    
    with col2:
        filter_by = st.selectbox("Filter by", ["All", "Beginner", "Intermediate", "Advanced", "Needs Review"])
    
    with col3:
        sort_by = st.selectbox("Sort by", ["Date Added", "Alphabetical", "Mastery"])
    
    # Display vocabulary list
    if 'vocabulary_list' in st.session_state and st.session_state.vocabulary_list:
        words = st.session_state.vocabulary_list
        
        # Filter and sort
        if search_term:
            words = [w for w in words if search_term.lower() in w['word'].lower()]
        
        if filter_by != "All":
            words = [w for w in words if w['difficulty'] == filter_by]
        
        # Display in grid
        cols = st.columns(3)
        for idx, word in enumerate(words):
            with cols[idx % 3]:
                with st.container():
                    st.markdown(f"""
                    <div style='background: white; border-radius: 10px; padding: 15px; 
                         margin-bottom: 15px; border: 1px solid #e0e0e0;'>
                        <h4 style='margin: 0;'>{word['word']}</h4>
                        <p style='margin: 5px 0; color: #666; font-size: 0.9em;'>
                            <i>{word.get('phonetic', '')}</i>
                        </p>
                        <p style='margin: 10px 0; font-size: 0.9em;'>
                            {word['meaning'][:60]}...
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Mastery slider
                    mastery = st.slider(
                        "Mastery",
                        0, 100, 
                        word.get('mastery', 0),
                        key=f"mastery_{word['word']}"
                    )
                    
                    # Actions
                    col_a, col_b = st.columns(2)
                    with col_a:
                        if st.button("Review", key=f"review_{word['word']}"):
                            st.info(f"Reviewing {word['word']}")
                    with col_b:
                        if st.button("❌", key=f"delete_{word['word']}"):
                            st.session_state.vocabulary_list.pop(idx)
                            st.rerun()
    else:
        st.info("Your vocabulary list is empty. Add words from 'Word of the Day' to get started!")
        
        # Sample words to add
        st.markdown("### 💡 Try These Common Words:")
        sample_words = [
            {"word": "Essential", "meaning": "Absolutely necessary", "level": "Beginner"},
            {"word": "Challenge", "meaning": "A difficult task", "level": "Beginner"},
            {"word": "Opportunity", "meaning": "A good chance for advancement", "level": "Intermediate"},
            {"word": "Significant", "meaning": "Important or noticeable", "level": "Intermediate"},
            {"word": "Comprehensive", "meaning": "Complete and including everything", "level": "Advanced"},
            {"word": "Ambiguous", "meaning": "Having more than one possible meaning", "level": "Advanced"},
        ]
        
        cols = st.columns(3)
        for idx, word in enumerate(sample_words):
            with cols[idx % 3]:
                if st.button(f"➕ {word['word']}", use_container_width=True):
                    if 'vocabulary_list' not in st.session_state:
                        st.session_state.vocabulary_list = []
                    
                    st.session_state.vocabulary_list.append({
                        "word": word['word'],
                        "meaning": word['meaning'],
                        "difficulty": word['level'],
                        "added_date": datetime.now(),
                        "mastery": 0
                    })
                    st.success(f"Added '{word['word']}'")

def render_word_games():
    """Vocabulary games"""
    
    st.markdown("### 🎮 Word Games")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container():
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, #FF9A8B 0%, #FF6A88 100%); 
                 color: white; padding: 30px; border-radius: 15px; text-align: center;'>
                <h1 style='font-size: 3rem; margin: 0;'>🔤</h1>
                <h3 style='margin: 10px 0;'>Word Match</h3>
                <p style='margin: 0;'>Match words with their meanings</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Play Match Game", use_container_width=True):
                st.session_state.game = "match"
                st.rerun()
    
    with col2:
        with st.container():
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, #42E695 0%, #3BB2B8 100%); 
                 color: white; padding: 30px; border-radius: 15px; text-align: center;'>
                <h1 style='font-size: 3rem; margin: 0;'>🧩</h1>
                <h3 style='margin: 10px 0;'>Fill-in Blanks</h3>
                <p style='margin: 0;'>Complete sentences with correct words</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Play Fill-in Game", use_container_width=True):
                st.session_state.game = "fill"
                st.rerun()
    
    with col3:
        with st.container():
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, #FFD26F 0%, #3677FF 100%); 
                 color: white; padding: 30px; border-radius: 15px; text-align: center;'>
                <h1 style='font-size: 3rem; margin: 0;'>⚡</h1>
                <h3 style='margin: 10px 0;'>Speed Quiz</h3>
                <p style='margin: 0;'>Test your knowledge against the clock</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Play Speed Quiz", use_container_width=True):
                st.session_state.game = "quiz"
                st.rerun()
    
    # Game area
    if 'game' in st.session_state:
        st.divider()
        
        if st.session_state.game == "match":
            render_match_game()
        elif st.session_state.game == "fill":
            render_fill_game()
        elif st.session_state.game == "quiz":
            render_quiz_game()

def render_match_game():
    """Word matching game"""
    st.markdown("### 🔤 Word Matching Game")
    
    # Game words
    words = [
        {"word": "Benevolent", "meaning": "Well meaning and kindly"},
        {"word": "Ephemeral", "meaning": "Lasting for a very short time"},
        {"word": "Meticulous", "meaning": "Showing great attention to detail"},
        {"word": "Ubiquitous", "meaning": "Present, appearing, or found everywhere"},
        {"word": "Ambiguous", "meaning": "Having more than one possible meaning"},
    ]
    
    # Shuffle words and meanings
    random.shuffle(words)
    meanings = [w["meaning"] for w in words]
    random.shuffle(meanings)
    
    # Display game
    st.info("**Instructions:** Match each word with its correct meaning by selecting from the dropdown.")
    
    score = 0
    for i, word in enumerate(words):
        col1, col2, col3 = st.columns([2, 3, 1])
        
        with col1:
            st.markdown(f"**{word['word']}**")
        
        with col2:
            selected = st.selectbox(
                "Select meaning",
                ["Choose..."] + meanings,
                key=f"match_{i}",
                label_visibility="collapsed"
            )
        
        with col3:
            if selected == word['meaning']:
                st.success("✓ Correct!")
                score += 1
            elif selected != "Choose...":
                st.error("✗ Try again")
    
    # Score
    st.divider()
    st.markdown(f"### Score: {score}/{len(words)}")
    
    if score == len(words):
        st.balloons()
        st.success("🎉 Perfect score! Well done!")
    
    if st.button("🔄 Play Again"):
        st.session_state.game = "match"
        st.rerun()

def render_fill_game():
    """Fill in the blanks game"""
    st.markdown("### 🧩 Fill in the Blanks")
    
    sentences = [
        "The new policy will have a ______ impact on the environment. (significant/ambiguous)",
        "Her ______ attention to detail made her an excellent editor. (meticulous/ephemeral)",
        "Smartphones have become ______ in modern society. (ubiquitous/benevolent)",
        "The beauty of cherry blossoms is ______, lasting only a week. (ephemeral/ambiguous)",
        "His ______ nature made him popular among his colleagues. (benevolent/meticulous)"
    ]
    
    answers = ["significant", "meticulous", "ubiquitous", "ephemeral", "benevolent"]
    
    st.info("**Instructions:** Fill in the blanks with the correct word from the options given.")
    
    user_answers = []
    for i, sentence in enumerate(sentences):
        # Extract options
        options = sentence[sentence.find("(")+1:sentence.find(")")].split("/")
        sentence_text = sentence[:sentence.find("(")].strip()
        
        # Display sentence with selectbox
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown(f"{sentence_text} ______")
        
        with col2:
            answer = st.selectbox(
                "Choose word",
                ["Select..."] + options,
                key=f"fill_{i}",
                label_visibility="collapsed"
            )
        
        user_answers.append(answer)
    
    # Check answers
    if st.button("Check Answers"):
        correct = 0
        for i, (user_ans, correct_ans) in enumerate(zip(user_answers, answers)):
            if user_ans == correct_ans:
                st.success(f"Sentence {i+1}: ✓ Correct!")
                correct += 1
            elif user_ans != "Select...":
                st.error(f"Sentence {i+1}: ✗ The correct word is '{correct_ans}'")
            else:
                st.warning(f"Sentence {i+1}: Please select an answer")
        
        st.markdown(f"### Score: {correct}/{len(sentences)}")
        
        if correct == len(sentences):
            st.balloons()

def render_quiz_game():
    """Speed quiz game"""
    st.markdown("### ⚡ Speed Quiz")
    
    # Timer
    if 'quiz_time' not in st.session_state:
        st.session_state.quiz_time = 60
        st.session_state.quiz_started = False
    
    col1, col2 = st.columns(2)
    
    with col1:
        if not st.session_state.quiz_started:
            if st.button("Start Quiz", type="primary"):
                st.session_state.quiz_started = True
                st.session_state.quiz_start_time = datetime.now()
        else:
            time_left = 60 - (datetime.now() - st.session_state.quiz_start_time).seconds
            st.metric("Time Left", f"{max(0, time_left)} seconds")
    
    with col2:
        st.metric("Questions", "0/10")
    
    # Quiz questions
    questions = [
        {
            "question": "What does 'ephemeral' mean?",
            "options": ["Lasting forever", "Lasting a very short time", "Extremely large", "Very colorful"],
            "answer": 1
        },
        {
            "question": "Which word means 'showing great attention to detail'?",
            "options": ["Benevolent", "Meticulous", "Ubiquitous", "Ambiguous"],
            "answer": 1
        },
        {
            "question": "What is the opposite of 'ubiquitous'?",
            "options": ["Common", "Rare", "Everywhere", "Popular"],
            "answer": 1
        },
        {
            "question": "Which word describes something with more than one meaning?",
            "options": ["Clear", "Specific", "Ambiguous", "Obvious"],
            "answer": 2
        }
    ]
    
    if st.session_state.quiz_started:
        for i, q in enumerate(questions[:3]):  # Show only 3 for demo
            st.radio(
                q["question"],
                q["options"],
                key=f"quiz_{i}"
            )

def render_vocabulary_progress():
    """Vocabulary progress tracking"""
    st.markdown("### 📈 Vocabulary Progress")
    
    # Stats
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_words = len(st.session_state.get('vocabulary_list', []))
        st.metric("Total Words", total_words)
    
    with col2:
        # Calculate average mastery
        if st.session_state.get('vocabulary_list'):
            avg_mastery = sum(w.get('mastery', 0) for w in st.session_state.vocabulary_list) / len(st.session_state.vocabulary_list)
            st.metric("Average Mastery", f"{avg_mastery:.0f}%")
        else:
            st.metric("Average Mastery", "0%")
    
    with col3:
        st.metric("Words This Week", "12")
    
    # Progress chart
    st.markdown("#### 📊 Mastery Progress")
    
    # Sample data for chart
    data = pd.DataFrame({
        'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
        'New Words': [5, 8, 12, 15],
        'Mastery %': [40, 55, 68, 75]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.bar_chart(data.set_index('Week')['New Words'])
        st.caption("New words learned per week")
    
    with col2:
        st.line_chart(data.set_index('Week')['Mastery %'])
        st.caption("Average mastery percentage")
    
    # Word categories
    st.markdown("#### 🏷️ Word Categories")
    
    if st.session_state.get('vocabulary_list'):
        categories = {}
        for word in st.session_state.vocabulary_list:
            cat = word.get('category', 'General')
            categories[cat] = categories.get(cat, 0) + 1
        
        for category, count in categories.items():
            st.write(f"**{category}:** {count} words")
            st.progress(count / max(categories.values()))
    else:
        st.info("Add words to see category breakdown")
    
    # Review schedule
    st.markdown("#### 📅 Review Schedule")
    
    review_schedule = [
        {"word": "Ubiquitous", "next_review": "Today", "mastery": 75},
        {"word": "Ephemeral", "next_review": "Tomorrow", "mastery": 60},
        {"word": "Meticulous", "next_review": "In 3 days", "mastery": 80},
        {"word": "Benevolent", "next_review": "In 5 days", "mastery": 90},
    ]
    
    for item in review_schedule:
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            st.write(f"**{item['word']}**")
        with col2:
            st.write(f"Next: {item['next_review']}")
        with col3:
            st.button("Review", key=f"review_{item['word']}")