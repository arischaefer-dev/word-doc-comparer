#!/usr/bin/env python3
"""
Test script to demonstrate AI-powered comment analysis
"""

import os
import sys
from app import WordDocumentAnalyzer

def test_ai_analysis():
    """Test AI-powered comment analysis"""
    
    print("🤖 Testing AI-Powered Comment Analysis")
    print("=" * 50)
    
    # Check if API keys are set
    anthropic_key = os.getenv('ANTHROPIC_API_KEY')
    openai_key = os.getenv('OPENAI_API_KEY')
    
    if not anthropic_key and not openai_key:
        print("❌ No AI API keys found!")
        print("\nTo enable AI analysis, set one of these environment variables:")
        print("  export ANTHROPIC_API_KEY='your-claude-api-key'")
        print("  export OPENAI_API_KEY='your-openai-api-key'")
        print("\nFalling back to pattern matching...")
        return False
    
    if anthropic_key:
        print("✅ Using Anthropic Claude API")
    elif openai_key:
        print("✅ Using OpenAI API")
    
    print()
    
    # Test with realistic scenarios
    analyzer = WordDocumentAnalyzer()
    
    test_scenarios = [
        {
            'comment': {'text': 'fix spelling - should be "receive" not "recieve"', 'id': '1'},
            'original': 'We will recieve your application tomorrow. The recieve date is important.',
            'revised': 'We will receive your application tomorrow. The receive date is important.',
            'expected': 'correctly_applied'
        },
        {
            'comment': {'text': 'real vs reel - wrong word used', 'id': '2'},
            'original': 'The fishing real was broken.',
            'revised': 'The fishing reel was broken.',
            'expected': 'correctly_applied'
        },
        {
            'comment': {'text': 'remove redundant word', 'id': '3'},
            'original': 'The project was very very successful.',
            'revised': 'The project was very successful.',
            'expected': 'correctly_applied'
        },
        {
            'comment': {'text': 'change all instances of "Company X" to "Acme Corp"', 'id': '4'},
            'original': 'Company X provides services. Company X is reliable. We trust Company X.',
            'revised': 'Acme Corp provides services. Acme Corp is reliable. We trust Acme Corp.',
            'expected': 'correctly_applied'
        }
    ]
    
    print("Testing various comment scenarios...")
    print()
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"Test {i}: \"{scenario['comment']['text']}\"")
        print(f"Original: {scenario['original']}")
        print(f"Revised:  {scenario['revised']}")
        
        try:
            # Analyze with AI
            result = analyzer.ai_analyze_comment(
                scenario['comment'], 
                scenario['original'], 
                scenario['revised']
            )
            
            status = result['validation']['status']
            message = result['validation']['message']
            confidence = result['validation'].get('confidence', 0)
            
            print(f"AI Result: {status} (confidence: {confidence:.1%})")
            print(f"Message: {message}")
            
            if status == scenario['expected']:
                print("✅ CORRECT")
            else:
                print(f"❌ INCORRECT (expected: {scenario['expected']})")
                
        except Exception as e:
            print(f"❌ ERROR: {str(e)}")
        
        print("-" * 50)
    
    return True

def setup_instructions():
    """Show setup instructions for AI APIs"""
    
    print("\n🚀 AI-Powered Word Document Comparer Setup")
    print("=" * 50)
    print()
    print("To enable intelligent comment analysis, you need an AI API key:")
    print()
    print("Option 1: Anthropic Claude (Recommended)")
    print("  1. Get API key from: https://console.anthropic.com/")
    print("  2. Set environment variable:")
    print("     export ANTHROPIC_API_KEY='your-api-key-here'")
    print()
    print("Option 2: OpenAI")
    print("  1. Get API key from: https://platform.openai.com/api-keys")
    print("  2. Set environment variable:")
    print("     export OPENAI_API_KEY='your-api-key-here'")
    print()
    print("Then restart the Flask app to enable AI analysis!")
    print()
    print("Benefits of AI Analysis:")
    print("  ✅ Understands natural language comments")
    print("  ✅ Handles ambiguous or complex requests")
    print("  ✅ Better accuracy than pattern matching")
    print("  ✅ Provides confidence scores")

if __name__ == "__main__":
    success = test_ai_analysis()
    
    if not success:
        setup_instructions()
    else:
        print("\n🎉 AI analysis test completed!")
        print("\nThe app will now use AI to analyze comments intelligently,")
        print("greatly reducing the number of comments requiring manual review.")