import openai
import os
from dotenv import load_dotenv

load_dotenv()

class AIHandler:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if self.api_key:
            openai.api_key = self.api_key
    
    def get_conversation_response(self, user_message, context=None):
        """Get AI response for conversation"""
        if not self.api_key:
            return self._get_fallback_response(user_message)
        
        try:
            messages = [
                {"role": "system", "content": "You are a friendly English tutor helping students practice."},
                {"role": "user", "content": user_message}
            ]
            
            if context:
                messages.insert(1, {"role": "system", "content": f"Context: {context}"})
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=150,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            print(f"OpenAI API error: {e}")
            return self._get_fallback_response(user_message)
    
    def _get_fallback_response(self, user_message):
        """Fallback response when API is not available"""
        fallback_responses = [
            "That's interesting! Could you tell me more about that?",
            "Good point! How do you feel about that?",
            "I understand. What happened next?",
            "That's a great question! What do you think about it?",
            "Interesting perspective! Could you elaborate?"
        ]
        
        import random
        return random.choice(fallback_responses)
    
    def check_grammar(self, text):
        """Check grammar of the given text"""
        if not self.api_key:
            return {"corrected": text, "feedback": "No grammar check available. Please check with a teacher."}
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an English grammar teacher. Correct any grammar mistakes in the text and provide brief feedback."},
                    {"role": "user", "content": f"Text to check: {text}"}
                ],
                max_tokens=100
            )
            
            result = response.choices[0].message.content.strip()
            
            # Simple parsing (in real app, you'd want better parsing)
            return {
                "corrected": result.split('\n')[0] if '\n' in result else result,
                "feedback": "Grammar checked by AI"
            }
        
        except Exception as e:
            return {"corrected": text, "feedback": f"Grammar check failed: {str(e)}"}