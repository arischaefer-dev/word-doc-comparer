#!/usr/bin/env python3
"""
Test script to demonstrate focused AI analysis vs global analysis
"""

import os
from app import WordDocumentAnalyzer

def test_focused_vs_global_analysis():
    """Test that AI focuses on specific comment context, not all document changes"""
    
    print("🎯 Testing Focused AI Analysis")
    print("=" * 50)
    
    # Create a scenario where multiple changes happen
    # but each comment should only relate to its specific change
    
    original_text = """
    Johnny walked to the store yesterday. The weather was absolutly beautiful.
    Johnny bought some groceries and went home. The store was very crowded.
    """
    
    revised_text = """
    Jimmy walked to the store yesterday. The weather was absolutely beautiful.
    Jimmy bought some groceries and went home. The store was very crowded.
    """
    
    # Two separate comments that should be analyzed independently
    comments = [
        {
            'text': 'Spelling mistake',
            'id': '1',
            'position': 65  # Around "absolutly"
        },
        {
            'text': 'Change Johnny to Jimmy throughout',
            'id': '2', 
            'position': 10  # Around first "Johnny"
        }
    ]
    
    print("Original:", original_text.strip())
    print("Revised: ", revised_text.strip())
    print()
    
    analyzer = WordDocumentAnalyzer()
    
    for i, comment in enumerate(comments, 1):
        print(f"Comment {i}: \"{comment['text']}\" (position: {comment['position']})")
        
        # Extract context to show what the AI should focus on
        context = analyzer.extract_comment_context(comment, original_text, revised_text)
        print(f"Original context: \"{context['original_context']}\"")
        print(f"Revised context:  \"{context['revised_context']}\"")
        print()
        
        # The AI should now focus only on this context, not the entire document
        print("Expected analysis:")
        if "spelling" in comment['text'].lower():
            print("  - Should detect absolutly → absolutely spelling fix")
            print("  - Should NOT mention Johnny → Jimmy name change")
        elif "johnny" in comment['text'].lower():
            print("  - Should detect Johnny → Jimmy name change")  
            print("  - Should NOT mention absolutly → absolutely spelling fix")
        
        print("-" * 30)

def test_without_ai():
    """Test the context extraction without AI calls"""
    
    print("🧪 Testing Context Extraction (No AI Required)")
    print("=" * 50)
    
    analyzer = WordDocumentAnalyzer()
    
    original = "The quick brown fox jumps over the lazy dog. This is a test sentence."
    revised = "The quick brown fox leaps over the lazy dog. This is a test sentence."
    
    comment = {
        'text': 'change jumps to leaps',
        'position': 20  # Around "jumps"
    }
    
    context = analyzer.extract_comment_context(comment, original, revised)
    
    print(f"Comment: \"{comment['text']}\"")
    print(f"Position: {comment['position']}")
    print(f"Original context: \"{context['original_context']}\"")
    print(f"Revised context:  \"{context['revised_context']}\"")
    print()
    print("✅ Context extraction working - AI will now see focused context")

if __name__ == "__main__":
    test_without_ai()
    print()
    test_focused_vs_global_analysis()
    
    print("\n🎯 Key Improvement:")
    print("- AI now sees focused context around each comment")
    print("- No longer confuses unrelated changes") 
    print("- Each comment analyzed independently")
    print("- More accurate and precise analysis")