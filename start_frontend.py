#!/usr/bin/env python3
"""
Frontend startup script for LegalEase React application.
"""

import os
import sys
import subprocess
import platform

def main():
    """Start the React frontend development server."""
    print("⚛️  Starting LegalEase React Frontend")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('frontend'):
        print("❌ frontend directory not found. Please run this script from the project root.")
        sys.exit(1)
    
    # Check if package.json exists
    if not os.path.exists('frontend/package.json'):
        print("❌ package.json not found in frontend directory.")
        sys.exit(1)
    
    # Check if node_modules exists
    if not os.path.exists('frontend/node_modules'):
        print("📦 Installing frontend dependencies...")
        try:
            subprocess.run(['npm', 'install'], cwd='frontend', check=True)
            print("✅ Dependencies installed successfully")
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies")
            print("Please run: cd frontend && npm install")
            sys.exit(1)
        except FileNotFoundError:
            print("❌ npm not found. Please install Node.js and npm")
            print("Download from: https://nodejs.org/")
            sys.exit(1)
    
    print("\n🚀 Starting React development server...")
    print("📍 Frontend will be available at: http://localhost:3000")
    print("🔗 Make sure Django backend is running at: http://localhost:8000")
    print("\n💡 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        # Start the React development server
        subprocess.run(['npm', 'start'], cwd='frontend', check=True)
    except KeyboardInterrupt:
        print("\n\n👋 Frontend server stopped. Thank you for using LegalEase!")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Failed to start frontend server: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("❌ npm not found. Please install Node.js and npm")
        print("Download from: https://nodejs.org/")
        sys.exit(1)

if __name__ == "__main__":
    main()