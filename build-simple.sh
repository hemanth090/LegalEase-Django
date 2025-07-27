#!/usr/bin/env bash
set -o errexit

echo "=== Starting Simple Build ==="

# Upgrade pip
pip install --upgrade pip

# Install only essential packages
echo "Installing essential packages..."
pip install Django==4.2.7
pip install djangorestframework==3.14.0
pip install django-cors-headers==4.3.1
pip install python-dotenv>=1.0.0
pip install whitenoise>=6.6.0
pip install gunicorn>=21.2.0
pip install groq>=0.4.1

# Try to install PDF support
echo "Installing PDF support..."
pip install PyPDF2==3.0.1 || echo "PyPDF2 failed, continuing..."

echo "=== Package installation complete ==="

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Run migrations
echo "Running migrations..."
python manage.py migrate

echo "=== Build completed successfully ==="