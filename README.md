# 🎓 English Practice Partner - AI-Powered Language Learning Platform

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

An intelligent web application that serves as an AI-powered English learning companion, providing interactive conversation practice, pronunciation training, vocabulary building, and grammar exercises with real-time feedback.

## ✨ Features

### 🎯 Core Features
- **💬 AI Conversation Practice** - Role-play real-life scenarios with an intelligent AI tutor
- **🎤 Pronunciation Trainer** - Voice analysis with waveform visualization and feedback
- **📚 Vocabulary Builder** - Interactive word learning with games and spaced repetition
- **📝 Grammar Exercises** - Topic-based practice with instant corrections
- **📈 Progress Tracking** - Detailed analytics and skill assessment with visual charts
- **🏆 Gamification** - Achievements, points system, and daily streaks

### 🚀 Advanced Features
- **Real-time Feedback** - Instant grammar correction and pronunciation analysis
- **Interactive Games** - Vocabulary matching, fill-in-blanks, and speed quizzes
- **Personalized Learning** - Adaptive exercises based on user level and progress
- **Voice Integration** - Speech-to-text and text-to-speech capabilities
- **Progress Analytics** - Skill radar charts, timeline tracking, and milestone achievements
- **Database Persistence** - SQLite database for storing user progress and vocabulary

## 🏗️ Architecture

```
english_practice_partner_v2/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (API keys)
├── assets/              # Static assets (images, icons)
├── components/          # Reusable UI components
│   ├── header.py        # Top navigation bar
│   ├── sidebar.py       # Sidebar with user stats
│   ├── cards.py         # Custom card components
│   └── charts.py        # Data visualization charts
├── pages/               # Application pages
│   ├── dashboard.py     # Main dashboard with stats
│   ├── conversation.py  # AI conversation practice
│   ├── pronunciation.py # Pronunciation training
│   ├── vocabulary.py    # Vocabulary building
│   ├── grammar.py       # Grammar exercises
│   └── progress.py      # Progress tracking
└── utils/               # Utility modules
    ├── ai_handler.py    # OpenAI API integration
    ├── speech_utils.py  # Speech recognition and synthesis
    ├── assessment.py    # Learning assessment algorithms
    └── database.py      # SQLite database operations
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/english-practice-partner.git
cd english-practice-partner
```

### Step 2: Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Create a `.env` file in the project root:
```env
# OpenAI API Key (optional, for enhanced AI features)
OPENAI_API_KEY=your_openai_api_key_here

# App Settings
APP_ENV=development
DEBUG=True
```

### Step 5: Run the Application
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## 🚀 Deployment

### Deploy on Streamlit Cloud (Recommended)
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Select your repository and branch
5. Set main file path to `app.py`
6. Add your secrets in the "Advanced settings":
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### Alternative Deployment Options
- **Heroku**: Use Procfile and requirements.txt
- **AWS Elastic Beanstalk**: Python platform
- **Docker**: Containerize the application
- **Railway.app**: Simple one-click deployment

## 📖 Usage Guide

### Getting Started
1. **First Launch**: The app will create a SQLite database automatically
2. **Set Your Level**: Choose your English proficiency level (A1-C2)
3. **Daily Goal**: Set a daily practice target (default: 30 minutes)

### Features Walkthrough

#### 🏠 Dashboard
- View your learning statistics
- Track daily streaks and points
- Access quick practice sessions
- Monitor weekly activity

#### 💬 Conversation Practice
- Select from 6+ real-world topics
- Role-play with AI tutor
- Receive instant grammar feedback
- Practice different scenarios

#### 🎤 Pronunciation Trainer
- Practice phrases at different difficulty levels
- View voice waveform visualization
- Get detailed feedback on clarity, pace, and pitch
- Access tongue twisters and minimal pairs

#### 📚 Vocabulary Builder
- Learn "Word of the Day" with detailed examples
- Build personal word collection
- Play interactive vocabulary games
- Track mastery progress

#### 📝 Grammar Exercises
- Practice specific grammar topics
- Complete fill-in-the-blank exercises
- Get explanations for grammar rules
- Multiple-choice quizzes

#### 📈 Progress Tracking
- View skill assessment radar chart
- Track learning timeline
- Unlock achievements
- Monitor milestone progress

## 🔧 Configuration

### API Keys
The application can be enhanced with the following API keys (optional):

1. **OpenAI API**: For advanced AI conversation features
   - Get key from [OpenAI Platform](https://platform.openai.com/api-keys)
   - Add to `.env` as `OPENAI_API_KEY`

2. **Google Cloud Speech-to-Text** (Future Enhancement):
   - Enable Speech-to-Text API
   - Add credentials to `.env`

### Customization
- Modify color schemes in `app.py` CSS
- Adjust difficulty levels in respective page files
- Add new vocabulary words in `vocabulary.py`
- Create new grammar exercises in `grammar.py`

## 🧪 Testing

### Run Basic Tests
```bash
# Test database initialization
python -c "from utils.database import init_db; init_db(); print('Database initialized successfully')"

# Test AI handler (requires OpenAI API key)
python -c "from utils.ai_handler import AIHandler; ai = AIHandler(); print(ai.get_conversation_response('Hello'))"
```

### Test Components
```bash
# Run Streamlit in test mode
streamlit run app.py --server.headless true
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Contribution Guidelines
- Follow PEP 8 style guide for Python code
- Add comments for complex functions
- Update documentation when adding new features
- Write tests for new functionality

### Project Structure
- Add new pages in the `pages/` directory
- Create reusable components in `components/`
- Utility functions go in `utils/`
- Static assets in `assets/`

## 📁 Project Structure Details

### Components
- `components/header.py`: Main navigation and user stats display
- `components/sidebar.py`: Sidebar with navigation and quick stats
- `components/cards.py`: Reusable card components for features
- `components/charts.py`: Plotly charts for data visualization

### Pages
- `pages/dashboard.py`: Main dashboard with learning analytics
- `pages/conversation.py`: AI conversation interface
- `pages/pronunciation.py`: Pronunciation training module
- `pages/vocabulary.py`: Vocabulary learning and games
- `pages/grammar.py`: Grammar exercises and practice
- `pages/progress.py`: Progress tracking and achievements

### Utilities
- `utils/ai_handler.py`: OpenAI GPT integration for conversations
- `utils/speech_utils.py`: Speech recognition and text-to-speech
- `utils/assessment.py`: Learning assessment algorithms
- `utils/database.py`: SQLite database operations and schemas

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError` for dependencies
**Solution**: 
```bash
pip install -r requirements.txt
```

**Issue**: OpenAI API not working
**Solution**: 
- Check API key in `.env` file
- Ensure OpenAI account has credits
- Verify internet connection

**Issue**: Speech recognition not working
**Solution**:
- Install PyAudio: `pip install pyaudio`
- On macOS: `brew install portaudio`
- On Linux: `sudo apt-get install python3-pyaudio`

**Issue**: Database errors
**Solution**:
- Delete `english_practice.db` and restart app
- Check file permissions

### Performance Tips
- Use Chrome or Firefox for best performance
- Clear browser cache if UI seems slow
- Close unused browser tabs
- For large vocabulary lists, use search filters

## 🔮 Future Enhancements

### Planned Features
- [ ] **Mobile App**: React Native version
- [ ] **Social Features**: Peer practice and competitions
- [ ] **Teacher Dashboard**: Classroom management tools
- [ ] **Advanced Pronunciation**: ML-based accent analysis
- [ ] **Offline Mode**: Practice without internet
- [ ] **Multi-language Support**: Learn English from other languages
- [ ] **Certification**: Progress certificates
- [ ] **AR/VR Features**: Immersive practice environments

### Integration Possibilities
- **Zoom Integration**: Live practice sessions
- **Duolingo API**: Sync progress with Duolingo
- **Google Classroom**: Assignments and grading
- **Speech Recognition**: Advanced pronunciation analysis

## 📊 Performance Metrics

- **Initial Load Time**: < 3 seconds
- **Database Operations**: < 100ms
- **AI Response Time**: 1-3 seconds (with OpenAI)
- **Memory Usage**: ~200MB
- **Supported Browsers**: Chrome, Firefox, Safari, Edge

## 👥 Target Audience

- **English Learners**: All proficiency levels (A1-C2)
- **Students**: School and university students
- **Professionals**: Business English and workplace communication
- **Teachers**: Supplemental teaching tool
- **Travelers**: Practical conversation practice

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the web interface
- AI powered by [OpenAI GPT](https://openai.com/) (optional)
- Icons from [Flaticon](https://www.flaticon.com/)
- Color schemes from [Coolors](https://coolors.co/)
- Charts by [Plotly](https://plotly.com/)
