#!/usr/bin/env python3
"""
Test the generalized AI comment analysis system.
"""

import sys
import os

# Add the app directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import WordDocumentAnalyzer

def test_ai_generalized_analysis():
    """Test the new generalized AI comment analysis"""
    
    analyzer = WordDocumentAnalyzer()
    
    # Test cases with various comment types and complexities
    test_cases = [
        {
            'comment': {
                'text': 'Change her name to Claire',
                'associated_text': 'Diane',
                'user_scope': 'global'
            },
            'original_text': 'Diane walked to the store. Later, Diane met her friend.',
            'revised_text': 'Claire walked to the store. Later, Claire met her friend.',
            'description': 'Global name change with pronoun reference'
        },
        {
            'comment': {
                'text': 'This should be more exciting',
                'associated_text': 'boring',
                'user_scope': 'local'
            },
            'original_text': 'The movie was boring and slow. The book was boring too.',
            'revised_text': 'The movie was exciting and slow. The book was boring too.',
            'description': 'Local adjective change with contextual instruction'
        },
        {
            'comment': {
                'text': 'Fix the spelling error here',
                'associated_text': 'recieve',
                'user_scope': 'auto'
            },
            'original_text': 'I will recieve the package tomorrow.',
            'revised_text': 'I will receive the package tomorrow.',
            'description': 'Spelling correction with auto scope'
        },
        {
            'comment': {
                'text': 'Make this character more friendly',
                'associated_text': 'grumpy old man',
                'user_scope': 'local'
            },
            'original_text': 'The grumpy old man yelled at children.',
            'revised_text': 'The friendly old man smiled at children.',
            'description': 'Complex character description change'
        },
        {
            'comment': {
                'text': "Don't use contractions",
                'associated_text': '"Phone lines are down," Eli said gruffly, handing her a blanket and a cup of tea. "Storm has cut the signal."',
                'user_scope': 'local'
            },
            'original_text': '"Phone lines are down," Eli said gruffly, handing her a blanket and a cup of tea. "Storm has cut the signal."',
            'revised_text': '"Phone lines are down," Eli said gruffly, handing her a blanket and a cup of tea. "Storm has cut the signal."',
            'description': 'Style comment - contraction removal (no contractions found)'
        },
        {
            'comment': {
                'text': "Don't use contractions", 
                'associated_text': '"I can\'t help you," she said. "It\'s too late."',
                'user_scope': 'local'
            },
            'original_text': '"I can\'t help you," she said. "It\'s too late."',
            'revised_text': '"I cannot help you," she said. "It is too late."',
            'description': 'Style comment - contraction removal (contractions found and fixed)'
        }
    ]
    
    print("🤖 Testing Generalized AI Comment Analysis")
    print("=" * 60)
    
    # Check if AI is available
    if not os.getenv('ANTHROPIC_API_KEY') and not os.getenv('OPENAI_API_KEY'):
        print("⚠️  No AI API key found. Set ANTHROPIC_API_KEY or OPENAI_API_KEY to test AI analysis.")
        print("   This test will use pattern matching fallback instead.")
        print()
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test['description']}")
        print(f"  Comment: '{test['comment']['text']}'")
        print(f"  On text: '{test['comment']['associated_text']}'")
        print(f"  Scope: {test['comment']['user_scope']}")
        
        try:
            # Run the AI analysis
            result = analyzer.ai_analyze_comment(
                test['comment'], 
                test['original_text'], 
                test['revised_text']
            )
            
            print(f"  ✅ Analysis completed")
            print(f"     Status: {result['validation']['status']}")
            print(f"     Interpretation: {result['intent'].get('ai_interpretation', 'N/A')}")
            print(f"     Expected: {result['intent']['from_text']} → {result['intent']['to_text']}")
            print(f"     Evidence: {result['validation'].get('evidence', 'N/A')}")
            print(f"     Confidence: {result['validation'].get('confidence', 'N/A')}")
            print(f"     AI Powered: {result.get('ai_powered', False)}")
            
        except Exception as e:
            print(f"  ❌ ERROR: {str(e)}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("🎯 Generalized AI Analysis Test Complete")
    print("\nThis system now:")
    print("- Uses AI to understand any comment in context")
    print("- Respects user-specified scope (global/local)")
    print("- Provides detailed evidence and reasoning")
    print("- Falls back gracefully when AI is unavailable")

if __name__ == "__main__":
    test_ai_generalized_analysis()