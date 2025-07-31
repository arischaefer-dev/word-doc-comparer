#!/usr/bin/env python3
"""
Test the specific contraction case from the user: "Storm's" should become "Storm has"
"""

import sys
import os

# Add the app directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import WordDocumentAnalyzer

def test_storms_contraction():
    """Test the specific Storm's contraction case"""
    
    analyzer = WordDocumentAnalyzer()
    
    # The exact text from the user
    comment = {
        'text': "Don't use contractions",
        'associated_text': '"Phone lines are down," Elias said gruffly, handing her a blanket and a cup of tea. "Storm\'s cut the signal."',
        'user_scope': 'local'
    }
    
    original_text = '"Phone lines are down," Elias said gruffly, handing her a blanket and a cup of tea. "Storm\'s cut the signal."'
    revised_text = '"Phone lines are down," Elias said gruffly, handing her a blanket and a cup of tea. "Storm has cut the signal."'
    
    print("🧪 Testing Specific Storm's Contraction Case")
    print("=" * 60)
    print(f"Comment: '{comment['text']}'")
    print(f"Associated text: '{comment['associated_text']}'")
    print(f"Expected: Storm's → Storm has")
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
        
        # Test with fallback method (what happens without AI)
        fallback_result = analyzer.fallback_analyze_comment(comment, original_text, revised_text)
        print("\n📋 Fallback analysis result:")
        print(f"   Status: {fallback_result['validation']['status']}")
        print(f"   Message: {fallback_result['validation']['message']}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("Expected behavior:")
    print("- Should detect 'Storm's' as a contraction")
    print("- Should show: Storm's → Storm has")
    print("- Should validate that the change was correctly applied")

if __name__ == "__main__":
    test_storms_contraction()