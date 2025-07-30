#!/usr/bin/env python3
"""
Test a real-world spelling correction scenario
"""

from app import WordDocumentAnalyzer

def test_spelling_correction():
    """Test the real vs reel spelling correction scenario"""
    
    analyzer = WordDocumentAnalyzer()
    
    # Simulate the original text with "real" 
    original_text = "The fishing reel was very real and cost a lot of money. Real fishermen know the difference."
    
    # Simulate the revised text where "real" was changed to "reel" in the fishing context
    revised_text = "The fishing reel was very reel and cost a lot of money. Real fishermen know the difference."
    
    # Test comment variations
    test_comments = [
        "correct spelling: real -> reel",
        "real? reel", 
        "should be reel not real",
        "reel"  # Single word comment
    ]
    
    print("🎣 Testing Real-World Spelling Correction Scenario")
    print(f"Original: {original_text}")
    print(f"Revised:  {revised_text}")
    print()
    
    for i, comment_text in enumerate(test_comments, 1):
        print(f"{i}. Comment: \"{comment_text}\"")
        
        # Parse the comment intent
        intent = analyzer.parse_comment_intent(comment_text)
        print(f"   Parsed: {intent['from_text']} -> {intent['to_text']} ({intent['type']})")
        
        # Validate the change
        validation = analyzer.validate_change_application(intent, original_text, revised_text)
        print(f"   Result: {validation['status']}")
        print(f"   Message: {validation['message']}")
        
        if 'details' in validation:
            details = validation['details']
            if 'original_count' in details:
                print(f"   Details: Original={details.get('original_count', 'N/A')}, "
                      f"Remaining={details.get('remaining_count', 'N/A')}, "
                      f"New={details.get('new_count', 'N/A')}")
        print()

if __name__ == "__main__":
    test_spelling_correction()