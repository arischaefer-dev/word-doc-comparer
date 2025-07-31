#!/usr/bin/env python3
"""
Test the improved comment parsing logic for context-aware comments.
"""

import sys
import os

# Add the app directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import WordDocumentAnalyzer

def test_comment_parsing():
    """Test various comment parsing scenarios"""
    
    analyzer = WordDocumentAnalyzer()
    
    test_cases = [
        {
            'comment': 'His name should be Eli',
            'associated_text': 'Elias',
            'expected_from': 'Elias',
            'expected_to': 'Eli',
            'expected_type': 'replace_global',
            'description': 'Context-aware name change'
        },
        {
            'comment': 'should be sunny',
            'associated_text': 'rainy',
            'expected_from': 'rainy',
            'expected_to': 'sunny', 
            'expected_type': 'replace_local',
            'description': 'Simple should be replacement'
        },
        {
            'comment': 'change this to happy',
            'associated_text': 'sad',
            'expected_from': 'sad',
            'expected_to': 'happy',
            'expected_type': 'replace_local', 
            'description': 'Change this to instruction'
        },
        {
            'comment': 'Jimmy',
            'associated_text': 'Johnny',
            'expected_from': 'Johnny',
            'expected_to': 'Jimmy',
            'expected_type': 'replace_local',
            'description': 'Single word replacement'
        },
        {
            'comment': 'change all Johnny to Jimmy',
            'associated_text': 'Johnny',
            'expected_from': 'Johnny',
            'expected_to': 'Jimmy',
            'expected_type': 'replace_global',
            'description': 'Explicit global change (should not use context-aware parsing)'
        },
        {
            'comment': 'Her name should be Sarah',
            'associated_text': 'Sally',
            'expected_from': 'Sally',
            'expected_to': 'Sarah',
            'expected_type': 'replace_global',
            'description': 'Another context-aware name change'
        },
        {
            'comment': 'The character should be called Mike',
            'associated_text': 'John',
            'expected_from': 'John',
            'expected_to': 'Mike', 
            'expected_type': 'replace_global',
            'description': 'Character name change pattern'
        }
    ]
    
    print("🧪 Testing Comment Parsing Logic")
    print("=" * 50)
    
    all_passed = True
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test['description']}")
        print(f"  Comment: '{test['comment']}'")
        print(f"  Associated text: '{test['associated_text']}'")
        
        try:
            result = analyzer.parse_comment_intent(test['comment'], test['associated_text'])
            
            # Check results
            passed = True
            issues = []
            
            if result['from_text'] != test['expected_from']:
                passed = False
                issues.append(f"from_text: got '{result['from_text']}', expected '{test['expected_from']}'")
            
            if result['to_text'] != test['expected_to']:
                passed = False
                issues.append(f"to_text: got '{result['to_text']}', expected '{test['expected_to']}'")
            
            if result['type'] != test['expected_type']:
                passed = False
                issues.append(f"type: got '{result['type']}', expected '{test['expected_type']}'")
            
            if passed:
                print(f"  ✅ PASSED")
                print(f"     → {result['from_text']} → {result['to_text']} ({result['type']})")
            else:
                print(f"  ❌ FAILED")
                for issue in issues:
                    print(f"     - {issue}")
                all_passed = False
                
        except Exception as e:
            print(f"  ❌ ERROR: {str(e)}")
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Comment parsing logic is working correctly.")
    else:
        print("⚠️  Some tests failed. Review the issues above.")
    
    return all_passed

if __name__ == "__main__":
    success = test_comment_parsing()
    sys.exit(0 if success else 1)