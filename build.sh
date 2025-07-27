#!/usr/bin/env bash
# LegalEase Build Script for Render Deployment
set -o errexit

echo "🚀 Starting LegalEase deployment build..."

# Upgrade pip and essential tools
echo "📦 Upgrading pip and build tools..."
pip install --upgrade pip setuptools wheel

# Install dependencies with fallback handling
echo "📚 Installing Python dependencies..."
pip install -r requirements.txt

echo "🗂️ Collecting static files..."
python manage.py collectstatic --no-input

echo "🗄️ Running database migrations..."
python manage.py migrate

echo "✅ Build completed successfully!"