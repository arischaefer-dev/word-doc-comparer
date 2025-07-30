#!/usr/bin/env python3
"""
Test the improved comment pattern recognition
"""

from app import WordDocumentAnalyzer

def test_comment_patterns():
    """Test various comment patterns"""
    
    analyzer = WordDocumentAnalyzer()
    
    test_comments = [
        # Spelling corrections
        "correct spelling: real -> reel",
        "real? reel",  
        "should be reel not real",
        "typo: real should be reel",
        "fix: real to reel",
        "reel",  # Single word
        
        # Other common patterns
        "change nice to excellent",
        "replace good with great",
        "delete this sentence",
        "add very before nice",
        "make bold",
        
        # Variations
        "correct: nice -> excellent", 
        "error: good should be great",
        "use great instead of good"
    ]
    
    print("🧪 Testing Comment Pattern Recognition\n")
    
    for i, comment in enumerate(test_comments, 1):
        print(f"{i:2d}. Comment: \"{comment}\"")
        
        intent = analyzer.parse_comment_intent(comment)
        
        print(f"    Type: {intent['type']}")
        print(f"    From: '{intent.get('from_text', 'N/A')}'")
        print(f"    To: '{intent.get('to_text', 'N/A')}'")
        print(f"    Scope: {intent['scope']}")
        
        if intent['type'] == 'unknown':
            print("    ❌ FAILED - Unrecognized pattern")
        else:
            print("    ✅ RECOGNIZED")
        print()

if __name__ == "__main__":
    test_comment_patterns()