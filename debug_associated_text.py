#!/usr/bin/env python3
"""
Debug script to identify why associated text might be empty
"""

from app import WordDocumentAnalyzer
import os

def debug_associated_text():
    """Debug associated text extraction across different scenarios"""
    
    print("🐛 Debugging Associated Text Issues")
    print("=" * 40)
    
    analyzer = WordDocumentAnalyzer()
    
    # Test scenarios
    test_files = [
        'focused_original_test.docx',
        'realistic_original_with_comments.docx',
        'test_original_with_comments.docx'
    ]
    
    for test_file in test_files:
        if os.path.exists(test_file):
            print(f"\n📄 Testing: {test_file}")
            print("-" * 30)
            
            try:
                data = analyzer.extract_document_data(test_file)
                
                print(f"Comments found: {len(data['comments'])}")
                
                for i, comment in enumerate(data['comments'], 1):
                    associated = comment.get('associated_text', '').strip()
                    print(f"\n{i}. \"{comment['text'][:40]}...\"")
                    print(f"   ID: {comment.get('id', 'NO_ID')}")
                    print(f"   Position: {comment.get('position', 'NO_POS')}")
                    print(f"   Associated: \"{associated}\" (len: {len(associated)})")
                    
                    if not associated:
                        print("   ❌ ISSUE: Associated text is empty!")
                        
                        # Try to debug why
                        print(f"   Full comment data: {comment}")
                    else:
                        print(f"   ✅ GOOD: Associated text found")
                        
            except Exception as e:
                print(f"   Error: {e}")
        else:
            print(f"\n📄 {test_file} - NOT FOUND")
    
    print(f"\n🔍 Testing Real Document Analysis")
    print("-" * 30)
    
    # Test the full analysis flow to see if associated text is preserved
    if os.path.exists('focused_original_test.docx') and os.path.exists('focused_revised_test.docx'):
        
        print("Testing full analysis workflow...")
        
        original_data = analyzer.extract_document_data('focused_original_test.docx')
        revised_data = analyzer.extract_document_data('focused_revised_test.docx')
        
        # Test just the fallback analysis (no AI)
        result = analyzer.fallback_analyze_comment(
            original_data['comments'][0],  # First comment
            original_data['full_text'],
            revised_data['full_text']
        )
        
        comment = result['comment']
        associated = comment.get('associated_text', '').strip()
        
        print(f"\nFallback analysis result:")
        print(f"Comment: \"{comment['text']}\"")
        print(f"Associated: \"{associated}\" (len: {len(associated)})")
        print(f"Status: {result['validation']['status']}")
        print(f"Message: {result['validation']['message']}")
        
        if not associated:
            print("❌ CRITICAL: Associated text lost in analysis flow!")
        else:
            print("✅ Associated text preserved in analysis")

def simulate_ai_prompt():
    """Simulate what the AI sees to identify the issue"""
    
    print(f"\n🤖 Simulating AI Prompt")
    print("=" * 25)
    
    analyzer = WordDocumentAnalyzer()
    
    if os.path.exists('focused_original_test.docx'):
        data = analyzer.extract_document_data('focused_original_test.docx')
        
        if data['comments']:
            comment = data['comments'][0]  # First comment
            associated_text = comment.get('associated_text', '').strip()
            
            print(f"Comment: \"{comment['text']}\"")
            print(f"Associated text: \"{associated_text}\"")
            print(f"Length: {len(associated_text)}")
            print(f"Empty?: {not associated_text}")
            
            # Show what gets passed to AI
            if associated_text:
                print(f"\n✅ AI would see:")
                print(f"TEXT THIS COMMENT REFERS TO: \"{associated_text}\"")
            else:
                print(f"\n❌ AI would see empty associated text!")
                print("AI prompt would use fallback mode")

if __name__ == "__main__":
    debug_associated_text()
    simulate_ai_prompt()
    
    print(f"\n💡 Possible Issues:")
    print("1. Associated text extraction failing for specific document types")
    print("2. Text getting lost during analysis workflow")
    print("3. Real Word comments vs test comments behaving differently")
    print("4. AI misinterpreting non-empty text as empty")
    print(f"\nNext: Check the actual documents you uploaded to see their structure")