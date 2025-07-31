#!/usr/bin/env python3
"""
Simple startup test for Railway deployment validation.
This script tests if the app can start up properly with various environment configurations.
"""

import os
import sys
import json
import logging

# Test different scenarios
test_scenarios = [
    {"name": "No API keys", "env": {}},
    {"name": "Anthropic key only", "env": {"ANTHROPIC_API_KEY": "test-key-12345"}},
    {"name": "OpenAI key only", "env": {"OPENAI_API_KEY": "test-key-12345"}},
    {"name": "Both keys", "env": {"ANTHROPIC_API_KEY": "test-key-12345", "OPENAI_API_KEY": "test-key-67890"}},
]

def test_app_import(scenario):
    """Test if the app can be imported under different conditions"""
    print(f"\n=== Testing: {scenario['name']} ===")
    
    # Set environment variables
    for key, value in scenario["env"].items():
        os.environ[key] = value
    
    # Clear any existing environment variables not in this scenario
    all_keys = {"ANTHROPIC_API_KEY", "OPENAI_API_KEY"}
    for key in all_keys:
        if key not in scenario["env"]:
            os.environ.pop(key, None)
    
    try:
        # Try to import the app
        if 'app' in sys.modules:
            del sys.modules['app']
        
        import app
        print("✅ App import successful")
        
        # Test health check
        with app.app.test_client() as client:
            response = client.get('/health')
            health_data = json.loads(response.data)
            print(f"✅ Health check passed: {health_data['status']}")
            print(f"   API status: {health_data['api_status']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    
    finally:
        # Clean up environment
        for key in scenario["env"]:
            os.environ.pop(key, None)

def main():
    """Run all startup tests"""
    print("🚀 Testing Word Doc Comparer startup scenarios...")
    
    results = []
    for scenario in test_scenarios:
        success = test_app_import(scenario)
        results.append((scenario["name"], success))
    
    print("\n" + "="*50)
    print("📊 Test Results Summary:")
    print("="*50)
    
    all_passed = True
    for name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {name}")
        if not success:
            all_passed = False
    
    if all_passed:
        print("\n🎉 All tests passed! App should deploy successfully to Railway.")
        return True
    else:
        print("\n⚠️  Some tests failed. Check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)