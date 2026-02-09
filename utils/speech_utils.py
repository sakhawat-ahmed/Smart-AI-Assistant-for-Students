import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
import base64

class SpeechHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def record_audio(self, duration=5):
        """Record audio from microphone"""
        try:
            with sr.Microphone() as source:
                st.info("Listening... Speak now!")
                audio = self.recognizer.listen(source, timeout=duration)
                return audio
        except sr.WaitTimeoutError:
            st.error("No speech detected. Please try again.")
            return None
        except Exception as e:
            st.error(f"Recording error: {str(e)}")
            return None
    
    def speech_to_text(self, audio):
        """Convert speech to text"""
        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand the audio."
        except sr.RequestError:
            return "Sorry, speech service is unavailable."
        except Exception as e:
            return f"Error: {str(e)}"
    
    def text_to_speech(self, text, lang='en', slow=False):
        """Convert text to speech and save as MP3"""
        try:
            tts = gTTS(text=text, lang=lang, slow=slow)
            
            # Create temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
                tts.save(fp.name)
                return fp.name
        except Exception as e:
            st.error(f"Text-to-speech error: {str(e)}")
            return None
    
    def get_audio_html(self, audio_file):
        """Get HTML for playing audio"""
        if not audio_file or not os.path.exists(audio_file):
            return ""
        
        with open(audio_file, "rb") as f:
            audio_bytes = f.read()
        
        audio_b64 = base64.b64encode(audio_bytes).decode()
        audio_html = f"""
            <audio controls autoplay>
                <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
                Your browser does not support the audio element.
            </audio>
        """
        return audio_html