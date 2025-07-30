#!/usr/bin/env python3
"""
Test script to simulate uploading documents to the Flask app
"""

import requests
import os

def test_upload_and_analysis():
    """Test the complete workflow"""
    
    base_url = "http://localhost:8081"
    
    # Check if files exist
    original_file = "test_original_with_comments.docx"
    revised_file = "test_revised_applied.docx"
    
    if not os.path.exists(original_file) or not os.path.exists(revised_file):
        print("❌ Test files not found. Please run create_test_doc.py first.")
        return
    
    print("🚀 Testing document upload and analysis...")
    
    # Upload files
    try:
        with open(original_file, 'rb') as orig, open(revised_file, 'rb') as rev:
            files = {
                'original_doc': orig,
                'revised_doc': rev
            }
            
            print("📤 Uploading documents...")
            response = requests.post(f"{base_url}/upload", files=files)
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Upload successful!")
                print(f"   Session ID: {data['session_id']}")
                print(f"   Original comments: {data['original_comments']}")
                print(f"   Message: {data['message']}")
                
                session_id = data['session_id']
                
                # Test the debug endpoint
                print(f"\n🔍 Testing debug endpoint...")
                debug_response = requests.get(f"{base_url}/debug/{session_id}")
                if debug_response.status_code == 200:
                    debug_data = debug_response.json()
                    print(f"✅ Debug data retrieved:")
                    print(f"   Original comments: {len(debug_data['original_comments'])}")
                    for i, comment in enumerate(debug_data['original_comments'][:3]):  # Show first 3
                        print(f"     {i+1}. {comment['text']}")
                    if len(debug_data['original_comments']) > 3:
                        print(f"     ... and {len(debug_data['original_comments']) - 3} more")
                
                # Run analysis
                print(f"\n⚙️ Running analysis...")
                analysis_response = requests.post(f"{base_url}/analyze/{session_id}")
                if analysis_response.status_code == 200:
                    analysis_data = analysis_response.json()
                    print(f"✅ Analysis complete!")
                    
                    # Get the report
                    report_response = requests.get(f"{base_url}/report/{session_id}")
                    if report_response.status_code == 200:
                        print(f"✅ Report generated successfully!")
                        print(f"   You can view it at: {base_url}/report/{session_id}")
                    else:
                        print(f"❌ Report generation failed: {report_response.status_code}")
                else:
                    print(f"❌ Analysis failed: {analysis_response.status_code}")
                    print(f"   Error: {analysis_response.text}")
            else:
                print(f"❌ Upload failed: {response.status_code}")
                print(f"   Error: {response.text}")
                
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Flask app. Make sure it's running on port 8081.")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    test_upload_and_analysis()