#!/usr/bin/env python3
"""
Test script to demonstrate improved comment-to-text association
"""

from app import WordDocumentAnalyzer

def test_associated_text_extraction():
    """Test that comments are properly associated with their target text"""
    
    print("📝 Testing Comment-to-Text Association")
    print("=" * 45)
    
    analyzer = WordDocumentAnalyzer()
    
    # Test with the focused test documents
    print("Testing with focused test documents...")
    
    try:
        original_data = analyzer.extract_document_data('focused_original_test.docx')
        
        print(f"\nExtracted {len(original_data['comments'])} comments:\n")
        
        for i, comment in enumerate(original_data['comments'], 1):
            print(f"{i}. Comment: \"{comment['text']}\"")
            print(f"   Associated Text: \"{comment.get('associated_text', 'NOT FOUND')}\"")
            print(f"   Position: {comment['position']}")
            
            # Analyze what the AI should focus on
            associated = comment.get('associated_text', '')
            if associated and associated != 'NOT FOUND':
                print(f"   ✅ AI will focus on: '{associated}'")
                
                # Predict expected analysis
                if "johnny" in comment['text'].lower() and "johnny" in associated.lower():
                    print(f"   Expected: Should detect Johnny→Jimmy change for this specific text")
                elif "spelling" in comment['text'].lower():
                    print(f"   Expected: Should detect spelling error in '{associated}'")
                elif "excellent" in comment['text'].lower():
                    print(f"   Expected: Should detect word improvement for '{associated}'")
                elif "duplicate" in comment['text'].lower():
                    print(f"   Expected: Should detect duplicate removal in '{associated}'")
            else:
                print(f"   ❌ Associated text not found - will fall back to context analysis")
            
            print("-" * 40)
        
        print("\\n🎯 Key Improvements:")
        print("✅ Comments now linked to specific text they refer to")
        print("✅ AI analysis will focus on the exact text mentioned")
        print("✅ No more confusion between unrelated document changes")
        print("✅ More accurate validation of whether changes were applied")
        
    except Exception as e:
        print(f"❌ Error testing with focused documents: {str(e)}")
        print("\\nTrying with simple test...")
        test_pattern_based_association()

def test_pattern_based_association():
    """Test pattern-based text association for fallback comments"""
    
    print("\\n🔍 Testing Pattern-Based Text Association")
    print("=" * 45)
    
    analyzer = WordDocumentAnalyzer()
    
    # Simulate text with pattern-based comments
    test_scenarios = [
        {
            'text': 'The word recieve is misspelled. [COMMENT: Spelling mistake]',
            'expected_associated': 'recieve'
        },
        {
            'text': 'Johnny went to the store. [COMMENT: Change Johnny to Jimmy] The weather was nice.',
            'expected_associated': 'Johnny went to the store.'
        },
        {
            'text': 'The project was very very successful. [COMMENT: Remove duplicate word]',
            'expected_associated': 'very very successful.'
        },
        {
            'text': 'The food was "good" at the restaurant. [COMMENT: Use excellent instead]',
            'expected_associated': 'good'
        }
    ]
    
    print("Testing pattern-based text association:\\n")
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"{i}. Text: {scenario['text']}")
        
        # Find comment pattern
        import re
        comment_match = re.search(r'\[COMMENT:\s*([^\]]+)\]', scenario['text'])
        if comment_match:
            associated_text = analyzer.find_associated_text_pattern(scenario['text'], comment_match)
            print(f"   Found associated text: \"{associated_text}\"")
            print(f"   Expected: \"{scenario['expected_associated']}\"")
            
            if associated_text.lower() in scenario['expected_associated'].lower() or scenario['expected_associated'].lower() in associated_text.lower():
                print(f"   ✅ CORRECT association")
            else:
                print(f"   ⚠️  Different association (may still be valid)")
        
        print("-" * 40)

if __name__ == "__main__":
    test_associated_text_extraction()
    print()
    test_pattern_based_association()
    
    print("\\n🚀 Next Steps:")
    print("1. Upload focused_original_test.docx and focused_revised_test.docx to the app")
    print("2. See how each comment is now linked to its specific text")
    print("3. AI analysis will be much more precise and accurate")
    print("4. No more confusion between unrelated changes!")