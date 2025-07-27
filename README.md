# LegalEase

**Professional legal document simplification service with AI-powered translation.**

LegalEase transforms complex legal documents into clear, understandable content using advanced AI technology. The application processes documents entirely in memory without storing sensitive user data.

## 🎯 Features

- **Document Processing**: Extract text from PDF, DOCX, and image files
- **AI Simplification**: Convert complex legal language to plain English
- **Multi-language Translation**: Support for 75+ languages
- **Privacy-First**: No document content stored on servers
- **Professional API**: RESTful endpoints for integration
- **Modern Frontend**: React-based user interface

## 🏗️ Architecture

```
LegalEase/
├── backend/                 # Django REST API
│   ├── documents/          # Main application
│   │   ├── services/       # Business logic
│   │   │   ├── ai_service.py
│   │   │   ├── text_extractor.py
│   │   │   └── translation_service.py
│   │   ├── views.py        # API endpoints
│   │   ├── models.py       # Database models
│   │   └── serializers.py  # Request validation
│   └── legalease/          # Django configuration
└── frontend/               # React application
    ├── src/
    │   ├── components/     # React components
    │   └── services/       # API communication
    └── public/
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- Groq API key (for AI features)

### Backend Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your Groq API key
   ```

3. **Initialize database:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Start server:**
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. **Install dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Start development server:**
   ```bash
   npm start
   ```

## 📡 API Endpoints

### Document Processing
```http
POST /api/process/
Content-Type: multipart/form-data

{
  "file": <document_file>,
  "target_language": "es" (optional)
}
```

### Text Simplification
```http
POST /api/simplify/
Content-Type: application/json

{
  "text": "Legal text to simplify",
  "target_language": "fr" (optional)
}
```

### Supported Languages
```http
GET /api/languages/
```

### Health Check
```http
GET /api/health/
```

## 🔒 Privacy & Security

- **Stateless Processing**: Documents processed in memory only
- **No Data Storage**: No document content saved to database
- **HTTPS Required**: Secure data transmission
- **File Validation**: Strict file type and size limits
- **Rate Limiting**: Protection against abuse

## 🛠️ Development

### Running Tests
```bash
python manage.py test
```

### Code Quality
```bash
flake8 .
black .
```

### API Documentation
Visit `/admin/` for Django admin interface and API exploration.

## 📦 Deployment

### Environment Variables
```bash
SECRET_KEY=your-secret-key
DEBUG=False
GROQ_API_KEY=your-groq-api-key
ALLOWED_HOSTS=yourdomain.com
```

### Production Setup
1. Set `DEBUG=False`
2. Configure proper `ALLOWED_HOSTS`
3. Use production database (PostgreSQL recommended)
4. Set up reverse proxy (Nginx)
5. Configure SSL certificates

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Check the documentation
- Review API endpoints

## 🔧 Technical Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: React, Axios
- **AI**: Groq API (Llama models)
- **Text Extraction**: PyPDF2, python-docx, Tesseract OCR
- **Database**: SQLite (development), PostgreSQL (production)
- **Deployment**: Docker, Nginx, Gunicorn