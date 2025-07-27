#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Starting minimal build for Render deployment..."

# Upgrade pip and setuptools
pip install --upgrade pip setuptools wheel

# Try minimal requirements first
echo "Installing minimal requirements..."
pip install -r requirements-minimal.txt

# Try to install additional packages one by one
echo "Attempting to install additional packages..."

# Try to install Pillow
pip install Pillow || echo "Pillow installation failed, continuing without it..."

# Try to install python-docx
pip install python-docx || echo "python-docx installation failed, continuing without it..."

# Try to install pytesseract
pip install pytesseract || echo "pytesseract installation failed, continuing without it..."

echo "Package installation completed."

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Run migrations
echo "Running migrations..."
python manage.py migrate

echo "Build completed successfully!"