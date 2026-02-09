import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import re

class Assessment:
    def __init__(self):
        # Download NLTK data if not present
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
    
    def assess_pronunciation(self, text, audio_features=None):
        """Assess pronunciation (simplified version)"""
        # This is a simplified version. In production, you'd use actual audio analysis
        
        # Calculate word count
        words = word_tokenize(text)
        word_count = len(words)
        
        # Calculate sentence count
        sentences = sent_tokenize(text)
        sentence_count = len(sentences)
        
        # Calculate average word length
        avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
        
        # Calculate complexity score (simple heuristic)
        complexity_score = min(100, (word_count * 2) + (sentence_count * 5))
        
        return {
            "word_count": word_count,
            "sentence_count": sentence_count,
            "avg_word_length": avg_word_length,
            "complexity_score": complexity_score,
            "pronunciation_score": 85,  # Placeholder
            "fluency_score": 78,  # Placeholder
            "clarity_score": 92  # Placeholder
        }
    
    def assess_vocabulary(self, text):
        """Assess vocabulary usage"""
        words = word_tokenize(text.lower())
        
        # Common words list (simplified)
        common_words = set([
            'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i',
            'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at'
        ])
        
        # Count unique words
        unique_words = set(words)
        
        # Count uncommon words
        uncommon_words = [w for w in unique_words if w not in common_words and w.isalpha()]
        
        # Calculate vocabulary score
        total_words = len(words)
        uncommon_count = len(uncommon_words)
        
        if total_words > 0:
            vocabulary_score = min(100, (uncommon_count / total_words) * 200)
        else:
            vocabulary_score = 0
        
        return {
            "total_words": total_words,
            "unique_words": len(unique_words),
            "uncommon_words": uncommon_count,
            "vocabulary_score": vocabulary_score
        }
    
    def assess_grammar(self, text):
        """Basic grammar assessment"""
        # This is simplified. In production, use proper grammar checking
        
        # Check for common errors
        errors = []
        
        # Check for subject-verb agreement (simplified)
        if re.search(r'\b(I|you|we|they)\s+(is|was)', text):
            errors.append("Subject-verb agreement error")
        
        # Check for article usage (simplified)
        if re.search(r'\b(a|an)\s+[aeiouAEIOU]', text):
            # Check for "a" before vowel sound (should be "an")
            errors.append("Article usage error")
        
        # Check for common mistakes
        common_mistakes = [
            (r'\b(i)\b', 'Use "I" instead of "i"'),
            (r'\b(dont|cant|wont)\b', 'Use contractions properly: don\'t, can\'t, won\'t'),
            (r'\b(their|there|they\'re)\b', 'Check usage of their/there/they\'re'),
            (r'\b(your|you\'re)\b', 'Check usage of your/you\'re')
        ]
        
        for pattern, message in common_mistakes:
            if re.search(pattern, text, re.IGNORECASE):
                if message not in errors:
                    errors.append(message)
        
        # Calculate grammar score
        error_count = len(errors)
        sentences = sent_tokenize(text)
        sentence_count = len(sentences)
        
        if sentence_count > 0:
            grammar_score = max(0, 100 - (error_count * 20))
        else:
            grammar_score = 100
        
        return {
            "error_count": error_count,
            "errors": errors,
            "sentence_count": sentence_count,
            "grammar_score": grammar_score
        }