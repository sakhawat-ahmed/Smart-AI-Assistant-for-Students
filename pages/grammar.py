import streamlit as st
import random

def render():
    st.markdown("## 📝 Grammar Mastery")
    
    # Grammar topics
    st.markdown("### 🎯 Choose a Grammar Topic")
    
    topics = [
        {"name": "Tenses", "icon": "⏰", "description": "Present, Past, Future tenses"},
        {"name": "Articles", "icon": "📰", "description": "a, an, the usage"},
        {"name": "Prepositions", "icon": "📍", "description": "in, on, at, by, with"},
        {"name": "Modals", "icon": "🔧", "description": "can, could, should, must"},
        {"name": "Conditionals", "icon": "🔀", "description": "If clauses and results"},
        {"name": "Reported Speech", "icon": "🗣️", "description": "Indirect speech"},
    ]
    
    cols = st.columns(3)
    for idx, topic in enumerate(topics):
        with cols[idx % 3]:
            if st.button(
                f"{topic['icon']} {topic['name']}",
                use_container_width=True,
                help=topic['description'],
                key=f"grammar_{idx}"
            ):
                st.session_state.selected_grammar_topic = topic['name']
                st.rerun()
    
    # Grammar exercises
    if 'selected_grammar_topic' in st.session_state:
        render_grammar_exercises()

def render_grammar_exercises():
    """Render grammar exercises based on selected topic"""
    
    topic = st.session_state.selected_grammar_topic
    
    st.divider()
    
    # Topic header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"### {topic} Exercises")
    with col2:
        if st.button("🔁 Change Topic"):
            del st.session_state.selected_grammar_topic
            st.rerun()
    
    # Explanation
    explanations = {
        "Tenses": """
        **English Tenses Overview:**
        
        **Present Simple:** Used for habits, facts, and general truths
        Example: "I **work** every day."
        
        **Present Continuous:** Used for actions happening now
        Example: "I **am working** right now."
        
        **Past Simple:** Used for completed actions in the past
        Example: "I **worked** yesterday."
        
        **Future Simple:** Used for predictions and spontaneous decisions
        Example: "I **will work** tomorrow."
        """,
        "Articles": """
        **Articles (a, an, the):**
        
        **a/an:** Used for singular countable nouns (first mention)
        - "a" before consonant sounds: a book, a university
        - "an" before vowel sounds: an apple, an hour
        
        **the:** Used for specific or previously mentioned nouns
        - The book on the table (specific book)
        - I bought a car. The car is red. (second mention)
        
        **No article:** Used for general concepts, plural nouns in general
        - Cats are animals. (cats in general)
        - I love music. (music in general)
        """,
        "Prepositions": """
        **Common Prepositions:**
        
        **Time:**
        - **at** for specific times: at 3 PM, at night
        - **on** for days/dates: on Monday, on June 5th
        - **in** for months/years/seasons: in January, in 2024, in summer
        
        **Place:**
        - **in** for enclosed spaces: in the room, in the car
        - **on** for surfaces: on the table, on the wall
        - **at** for specific points: at the station, at home
        
        **Other:**
        - **by** for means: by car, by email
        - **with** for accompaniment: with friends, with a pen
        - **about** for topics: about English, about you
        """
    }
    
    if topic in explanations:
        with st.expander("📚 Grammar Rules"):
            st.markdown(explanations[topic])
    
    # Exercises based on topic
    if topic == "Tenses":
        render_tenses_exercises()
    elif topic == "Articles":
        render_articles_exercises()
    elif topic == "Prepositions":
        render_prepositions_exercises()
    else:
        st.info(f"Exercises for {topic} coming soon!")
        
        # Sample exercise
        st.markdown("### Sample Exercise")
        
        questions = [
            "This is ______ interesting book.",
            "She lives ______ London.",
            "They ______ (go) to school every day.",
            "If I ______ (have) time, I will call you.",
            "He said he ______ (be) tired."
        ]
        
        for i, question in enumerate(questions):
            answer = st.text_input(f"Q{i+1}: {question}", key=f"sample_{i}")
            if answer:
                st.caption("Check your answer with a teacher or grammar book!")

def render_tenses_exercises():
    """Tenses exercises"""
    
    st.markdown("### ⏰ Tense Practice")
    
    # Exercise 1: Fill in the blanks
    st.markdown("#### Exercise 1: Fill in the blanks with correct tense")
    
    tense_exercises = [
        {
            "sentence": "I usually ______ (go) to bed at 11 PM.",
            "correct": "go",
            "explanation": "Present simple for habits"
        },
        {
            "sentence": "Right now, she ______ (study) for her exam.",
            "correct": "is studying",
            "explanation": "Present continuous for actions happening now"
        },
        {
            "sentence": "Yesterday, they ______ (visit) the museum.",
            "correct": "visited",
            "explanation": "Past simple for completed actions"
        },
        {
            "sentence": "By next year, I ______ (learn) English for 5 years.",
            "correct": "will have been learning",
            "explanation": "Future perfect continuous for duration"
        },
        {
            "sentence": "When I arrived, they ______ already ______ (finish) dinner.",
            "correct": "had finished",
            "explanation": "Past perfect for actions before another past action"
        }
    ]
    
    user_answers = []
    for i, ex in enumerate(tense_exercises):
        answer = st.text_input(
            f"{i+1}. {ex['sentence']}",
            key=f"tense_{i}",
            placeholder="Type the correct verb form"
        )
        user_answers.append(answer)
        
        if answer:
            if answer.lower() == ex['correct'].lower():
                st.success(f"Correct! {ex['explanation']}")
            else:
                st.error(f"Try again. Hint: {ex['explanation']}")
    
    # Exercise 2: Multiple choice
    st.markdown("#### Exercise 2: Choose the correct tense")
    
    mc_questions = [
        {
            "question": "Which sentence is in present perfect?",
            "options": [
                "I eat breakfast every day.",
                "I have eaten breakfast.",
                "I am eating breakfast.",
                "I will eat breakfast."
            ],
            "correct": 1
        },
        {
            "question": "Choose the past continuous sentence:",
            "options": [
                "She sings beautifully.",
                "She was singing when I called.",
                "She has sung that song before.",
                "She will sing tomorrow."
            ],
            "correct": 1
        }
    ]
    
    for i, q in enumerate(mc_questions):
        answer = st.radio(
            q["question"],
            q["options"],
            key=f"mc_tense_{i}"
        )
        
        if answer:
            if q["options"].index(answer) == q["correct"]:
                st.success("✓ Correct!")
            else:
                st.error("✗ Try again")

def render_articles_exercises():
    """Articles exercises"""
    
    st.markdown("### 📰 Articles Practice")
    
    # Fill in the blanks
    st.markdown("#### Fill in the blanks with a, an, the, or leave blank")
    
    article_exercises = [
        "I saw ______ interesting movie last night.",
        "She is ______ best student in our class.",
        "He wants to buy ______ new car.",
        "______ Mount Everest is in Nepal.",
        "I need ______ information about this topic.",
        "She plays ______ piano beautifully.",
        "They went to ______ United States last year.",
        "I'll be back in ______ hour."
    ]
    
    answers = ["an", "the", "a", "The", "", "the", "the", "an"]
    
    user_answers = []
    for i, sentence in enumerate(article_exercises):
        answer = st.text_input(
            f"{i+1}. {sentence}",
            key=f"article_{i}",
            placeholder="a/an/the or leave empty"
        )
        user_answers.append(answer)
        
        if answer:
            if answer.lower() == answers[i].lower() or (answer == "" and answers[i] == ""):
                st.success("Correct!")
            else:
                st.error(f"The correct answer is: '{answers[i]}'")
    
    # Rule practice
    st.markdown("#### Identify the rule")
    
    rule_questions = [
        {
            "sentence": "The sun rises in the east.",
            "rules": [
                "Use 'the' with unique things (sun, moon, earth)",
                "Use 'the' with cardinal directions",
                "Both of the above"
            ],
            "correct": 2
        },
        {
            "sentence": "I need a pen and some paper.",
            "rules": [
                "Use 'a' with countable nouns",
                "Use no article with uncountable nouns",
                "Both of the above"
            ],
            "correct": 2
        }
    ]
    
    for i, q in enumerate(rule_questions):
        st.write(f"**Sentence:** {q['sentence']}")
        answer = st.radio(
            "Which rule applies?",
            q["rules"],
            key=f"rule_{i}"
        )
        
        if answer:
            if q["rules"].index(answer) == q["correct"]:
                st.success("✓ Correct!")
            else:
                st.error("✗ Try again")

def render_prepositions_exercises():
    """Prepositions exercises"""
    
    st.markdown("### 📍 Prepositions Practice")
    
    # Time prepositions
    st.markdown("#### Time Prepositions")
    
    time_exercises = [
        ("I have a meeting ______ 3 PM.", ["at", "on", "in"], 0),
        ("Her birthday is ______ June.", ["at", "on", "in"], 2),
        ("We'll meet ______ Monday.", ["at", "on", "in"], 1),
        ("I was born ______ 1990.", ["at", "on", "in"], 2),
        ("The shop closes ______ midnight.", ["at", "on", "in"], 0)
    ]
    
    for i, (sentence, options, correct) in enumerate(time_exercises):
        answer = st.selectbox(
            f"{i+1}. {sentence}",
            ["Select..."] + options,
            key=f"time_prep_{i}"
        )
        
        if answer != "Select...":
            if options.index(answer) == correct:
                st.success("✓ Correct!")
            else:
                st.error(f"✗ The correct preposition is '{options[correct]}'")
    
    # Place prepositions
    st.markdown("#### Place Prepositions")
    
    place_exercises = [
        ("The book is ______ the table.", ["in", "on", "at"], 1),
        ("She lives ______ New York.", ["in", "on", "at"], 0),
        ("Wait for me ______ the bus stop.", ["in", "on", "at"], 2),
        ("There's a picture ______ the wall.", ["in", "on", "at"], 1),
        ("He's sitting ______ the front of the car.", ["in", "on", "at"], 0)
    ]
    
    for i, (sentence, options, correct) in enumerate(place_exercises):
        answer = st.selectbox(
            f"{i+1}. {sentence}",
            ["Select..."] + options,
            key=f"place_prep_{i}"
        )
        
        if answer != "Select...":
            if options.index(answer) == correct:
                st.success("✓ Correct!")
            else:
                st.error(f"✗ The correct preposition is '{options[correct]}'")
    
    # Mixed prepositions
    st.markdown("#### Mixed Prepositions")
    
    mixed_exercises = [
        "I'm good ______ math.",
        "She's interested ______ learning English.",
        "He apologized ______ being late.",
        "They're talking ______ the weather.",
        "I'm looking forward ______ seeing you."
    ]
    
    mixed_answers = ["at", "in", "for", "about", "to"]
    mixed_options = [["at", "in", "for"], ["in", "at", "with"], ["for", "about", "to"], ["about", "on", "with"], ["to", "for", "at"]]
    
    for i, (sentence, options, correct_answer) in enumerate(zip(mixed_exercises, mixed_options, mixed_answers)):
        answer = st.selectbox(
            f"{i+1}. {sentence}",
            ["Select..."] + options,
            key=f"mixed_prep_{i}"
        )
        
        if answer != "Select...":
            if answer == correct_answer:
                st.success("✓ Correct!")
            else:
                st.error(f"✗ The correct preposition is '{correct_answer}'")