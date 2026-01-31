import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
import base64

class SpeechHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def speech_to_text(self, audio_file=None):
        """Convert speech to text"""
        try:
            if audio_file:
                with sr.AudioFile(audio_file) as source:
                    audio = self.recognizer.record(source)
            else:
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = self.recognizer.listen(source, timeout=5)
            
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand the audio."
        except sr.RequestError:
            return "Sorry, speech service is unavailable."
        except Exception as e:
            return f"Error: {str(e)}"
    
    def text_to_speech(self, text, lang='en'):
        """Convert text to speech and return audio file"""
        tts = gTTS(text=text, lang=lang, slow=False)
        
        # Create temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            tts.save(fp.name)
            return fp.name
    
    def autoplay_audio(self, audio_file):
        """Generate HTML for autoplaying audio"""
        with open(audio_file, "rb") as f:
            audio_bytes = f.read()
        
        audio_b64 = base64.b64encode(audio_bytes).decode()
        audio_html = f"""
            <audio autoplay>
                <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
            </audio>
        """
        return audio_html