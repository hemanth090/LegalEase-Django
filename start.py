#!/usr/bin/env python3
"""
LegalEase startup script.
Professional document processing service.
"""

import os
import sys
import subprocess

def main():
    """Start the LegalEase Django server."""
    print("🚀 Starting LegalEase API Server")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ Error: manage.py not found. Please run from project root.")
        sys.exit(1)
    
    # Check if database is set up
    if not os.path.exists('db.sqlite3'):
        print("📊 Setting up database...")
        subprocess.run([sys.executable, 'manage.py', 'migrate'], check=True)
    
    print("✅ LegalEase API starting...")
    print("📡 Server will be available at: http://127.0.0.1:8000")
    print("🔧 Admin panel: http://127.0.0.1:8000/admin/")
    print("📋 API endpoints: http://127.0.0.1:8000/api/")
    print("\n💡 Press Ctrl+C to stop the server")
    print("=" * 40)
    
    # Start Django development server
    try:
        subprocess.run([sys.executable, 'manage.py', 'runserver'], check=True)
    except KeyboardInterrupt:
        print("\n👋 LegalEase server stopped.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()