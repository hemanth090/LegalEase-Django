#!/usr/bin/env bash
# exit on error
set -o errexit

# Upgrade pip and setuptools
pip install --upgrade pip setuptools wheel

# Install system dependencies that might be needed
# (Render usually has these, but just in case)

# Install Python dependencies with more verbose output
pip install -r requirements.txt --verbose

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate