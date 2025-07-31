#!/usr/bin/env python3
"""
Test multiple contractions in one text
"""

import sys
import os

# Add the app directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import WordDocumentAnalyzer

def test_multiple_contractions():
    """Test text with multiple contractions"""
    
    analyzer = WordDocumentAnalyzer()
    
    comment = {
        'text': "Don't use contractions",
        'associated_text': '"I can\'t help you," she said. "It\'s too late and we don\'t have time."',
        'user_scope': 'local'
    }
    
    print("🧪 Testing Multiple Contractions")
    print("=" * 50)
    print(f"Comment: '{comment['text']}'")
    print(f"Associated text: '{comment['associated_text']}'")
    print()
    
    # Test contraction detection
    contractions = analyzer.find_contractions(comment['associated_text'])
    print(f"🔍 Contractions found: {contractions}")
    
    # Test contraction expansion
    if contractions:
        for contraction in contractions:
            expanded = analyzer.expand_contraction(contraction)
            print(f"📝 {contraction} → {expanded}")
    
    print()
    
    # Test the full comment parsing
    try:
        result = analyzer.parse_comment_intent(comment['text'], comment['associated_text'])
        print("✅ Comment parsing result:")
        print(f"   Type: {result['type']}")
        print(f"   From: {result['from_text']}")
        print(f"   To: {result['to_text']}")
        print(f"   Scope: {result['scope']}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_multiple_contractions()