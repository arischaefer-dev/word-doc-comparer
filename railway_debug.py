#!/usr/bin/env python3
"""
Railway deployment debug script.
This script helps diagnose Railway deployment issues by checking environment and dependencies.
"""

import os
import sys
import json
import importlib.util

def check_environment():
    """Check environment variables and system info"""
    print("🔍 Environment Check")
    print("=" * 40)
    
    # Python version
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    
    # Environment variables
    env_vars = ['PORT', 'ANTHROPIC_API_KEY', 'OPENAI_API_KEY', 'FLASK_SECRET_KEY', 'RAILWAY_ENVIRONMENT']
    for var in env_vars:
        value = os.environ.get(var)
        if var in ['ANTHROPIC_API_KEY', 'OPENAI_API_KEY', 'FLASK_SECRET_KEY']:
            # Don't print sensitive keys, just show if they exist
            print(f"{var}: {'✅ Set' if value else '❌ Not set'}")
        else:
            print(f"{var}: {value or '❌ Not set'}")
    
    print()

def check_packages():
    """Check if required packages can be imported"""
    print("📦 Package Import Check")
    print("=" * 40)
    
    packages = [
        'flask',
        'docx',
        'anthropic',
        'openai',
        'gunicorn',
    ]
    
    all_good = True
    for package in packages:
        try:
            if package == 'docx':
                # python-docx imports as docx
                import docx
            else:
                __import__(package)
            print(f"✅ {package}: OK")
        except ImportError as e:
            print(f"❌ {package}: FAILED - {e}")
            all_good = False
    
    print()
    return all_good

def test_app_creation():
    """Test if the Flask app can be created"""
    print("🚀 App Creation Test")
    print("=" * 40)
    
    try:
        import app
        print("✅ App import: OK")
        
        # Test creating a test client
        client = app.app.test_client()
        print("✅ Test client: OK")
        
        # Test health endpoint
        response = client.get('/health')
        if response.status_code == 200:
            data = json.loads(response.data)
            print("✅ Health check: OK")
            print(f"   Status: {data.get('status')}")
            print(f"   Service: {data.get('service')}")
            
            api_status = data.get('api_status', {})
            print(f"   Anthropic ready: {api_status.get('anthropic_ready', False)}")
            print(f"   OpenAI ready: {api_status.get('openai_ready', False)}")
        else:
            print(f"❌ Health check failed: HTTP {response.status_code}")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ App creation failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all checks"""
    print("🚀 Railway Deployment Debug Script")
    print("=" * 50)
    
    check_environment()
    
    packages_ok = check_packages()
    if not packages_ok:
        print("⚠️  Some packages failed to import. This may cause deployment issues.")
        print()
    
    app_ok = test_app_creation()
    
    print("=" * 50)
    if packages_ok and app_ok:
        print("🎉 All checks passed! App should deploy successfully to Railway.")
        
        # Show suggested environment variables for Railway
        print("\n📝 Railway Environment Variables to Set:")
        print("   ANTHROPIC_API_KEY=your_actual_api_key_here")
        print("   FLASK_SECRET_KEY=some_random_secure_string")
        
    else:
        print("⚠️  Some checks failed. Review the errors above.")
        print("\n🔧 Troubleshooting:")
        print("   1. Ensure all packages in requirements.txt are available")
        print("   2. Check that your API key format is correct")
        print("   3. Verify Railway environment variables are set properly")
    
    return packages_ok and app_ok

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)