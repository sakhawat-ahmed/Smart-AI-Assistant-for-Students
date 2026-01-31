import os
import openai
from dotenv import load_dotenv
import json

load_dotenv()

class AITutor:
    def __init__(self):
        # Initialize OpenAI
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
    def correct_grammar(self, text):
        """Correct grammar in user's text"""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an English teacher. Correct any grammar mistakes in the following text. Return only the corrected text."},
                    {"role": "user", "content": text}
                ],
                max_tokens=100
            )
            return response.choices[0].message.content.strip()
        except:
            return text  # Return original if API fails
    
    def generate_conversation_response(self, user_input, context):
        """Generate AI response for conversation"""
        prompt = f"""You are a friendly English tutor helping a student practice.
        Student level: {context['level']}
        Topic: {context['topic']}
        
        Previous conversation:
        {context.get('history', '')}
        
        Student says: "{user_input}"
        
        Respond naturally as a tutor:
        1. First, correct any mistakes gently if needed
        2. Then continue the conversation naturally
        3. Ask open-ended questions to encourage speaking
        4. Keep responses concise (2-3 sentences)
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7,
                max_tokens=150
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return "I'm here to help you practice English! Could you tell me more?"