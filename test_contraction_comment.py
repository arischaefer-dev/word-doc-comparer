#!/usr/bin/env python3
"""
Test the specific contraction comment case that was failing.
"""

import sys
import os

# Add the app directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import WordDocumentAnalyzer

def test_contraction_comment():
    """Test the contraction comment case specifically"""
    
    analyzer = WordDocumentAnalyzer()
    
    # The exact test case from the user
    comment = {
        'text': "Don't use contractions",
        'associated_text': '"Phone lines are down," Eli said gruffly, handing her a blanket and a cup of tea. "Storm has cut the signal."',
        'user_scope': 'local'
    }
    
    original_text = '"Phone lines are down," Eli said gruffly, handing her a blanket and a cup of tea. "Storm has cut the signal."'
    revised_text = '"Phone lines are down," Eli said gruffly, handing her a blanket and a cup of tea. "Storm has cut the signal."'
    
    print("🧪 Testing Contraction Comment Analysis")
    print("=" * 50)
    print(f"Comment: '{comment['text']}'")
    print(f"Associated text: '{comment['associated_text'][:50]}...'")
    print(f"Scope: {comment['user_scope']}")
    print()
    
    # Check if AI is available
    if not os.getenv('ANTHROPIC_API_KEY') and not os.getenv('OPENAI_API_KEY'):
        print("⚠️  No AI API key found. Testing with pattern matching fallback.")
        
        # Test the fallback method
        try:
            result = analyzer.fallback_analyze_comment(comment, original_text, revised_text)
            print("📝 Fallback Analysis Result:")
            print(f"   Type: {result['intent']['type']}")
            print(f"   From: {result['intent']['from_text']}")
            print(f"   To: {result['intent']['to_text']}")
            print(f"   Status: {result['validation']['status']}")
            print(f"   Message: {result['validation']['message']}")
        except Exception as e:
            print(f"❌ Fallback failed: {e}")
    else:
        print("🤖 Testing with AI analysis...")
        
        try:
            # Test the AI method
            result = analyzer.ai_analyze_comment(comment, original_text, revised_text)
            print("✅ AI Analysis Result:")
            print(f"   Type: {result['intent']['type']}")
            print(f"   Interpretation: {result['intent'].get('ai_interpretation', 'N/A')}")
            print(f"   From: {result['intent']['from_text']}")
            print(f"   To: {result['intent']['to_text']}")
            print(f"   Status: {result['validation']['status']}")
            print(f"   Evidence: {result['validation'].get('evidence', 'N/A')}")
            print(f"   Confidence: {result['validation'].get('confidence', 'N/A')}")
        except Exception as e:
            print(f"❌ AI analysis failed: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 50)
    print("Expected behavior:")
    print("- Should recognize this as a STYLE comment")
    print("- Should identify that there are NO contractions in the text")
    print("- Should mark as 'correctly_applied' (no contractions to fix)")
    print("- Should NOT return 'unknown' type")

if __name__ == "__main__":
    test_contraction_comment()