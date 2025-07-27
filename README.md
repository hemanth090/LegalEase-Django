# LegalEase - AI Legal Document Simplifier

[![React](https://img.shields.io/badge/React-18.2.0-blue.svg)](https://reactjs.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow.svg)](https://python.org/)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)

> Transform complex legal documents into clear, understandable explanations using AI technology.

## 🎯 Project Overview

LegalEase is a full-stack web application that leverages artificial intelligence to simplify complex legal documents, making legal information accessible to everyone. The application features a modern, responsive interface built with React and a robust Django REST API backend.

## ✨ Key Features

### 🤖 AI-Powered Processing
- **Document Simplification**: Converts complex legal jargon into plain English
- **Multi-language Translation**: Supports 20+ languages for global accessibility
- **Intelligent Analysis**: Context-aware processing for accurate simplification

### 📄 File Processing
- **Multiple Formats**: PDF, DOCX, and image file support
- **OCR Technology**: Extract text from scanned documents and images
- **Drag & Drop Interface**: Intuitive file upload experience
- **File Validation**: Size and format validation with user feedback

### 🎨 Modern User Interface
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **Real-time Processing**: Live status updates with progress indicators
- **Clean Architecture**: Professional UI with smooth animations
- **Accessibility**: WCAG compliant design principles

### 🔒 Security & Privacy
- **Memory-only Processing**: Documents processed in memory, never stored
- **Data Protection**: No permanent storage of sensitive information
- **Secure API**: RESTful API with proper error handling

## 🛠️ Technology Stack

### Frontend
- **React 18.2** - Modern JavaScript library for building user interfaces
- **CSS3** - Custom styling with CSS variables and modern layout techniques
- **React Hooks** - State management with useState, useEffect
- **Responsive Design** - Mobile-first approach with CSS Grid and Flexbox

### Backend
- **Django 4.2** - High-level Python web framework
- **Django REST Framework** - Powerful toolkit for building Web APIs
- **Python 3.8+** - Core programming language
- **SQLite** - Lightweight database for development

### AI & Processing
- **Groq API** - Advanced language model for text simplification
- **OCR Integration** - Optical Character Recognition for image processing
- **Multi-language Support** - Translation capabilities for global reach

### Development Tools
- **Git** - Version control system
- **npm** - Package management for frontend dependencies
- **pip** - Python package management

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Node.js 14 or higher
- npm or yarn package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/hemanth090/LegalEase-Django.git
   cd LegalEase-Django
   ```

2. **Backend Setup**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Run migrations
   python manage.py migrate
   
   # Start Django server
   python manage.py runserver
   ```

3. **Frontend Setup**
   ```bash
   # Navigate to frontend directory
   cd frontend
   
   # Install dependencies
   npm install
   
   # Start development server
   npm start
   ```

4. **Environment Configuration**
   ```bash
   # Copy environment template
   cp .env.example .env
   
   # Add your API keys to .env file
   GROQ_API_KEY=your_groq_api_key_here
   ```

### Usage

1. Open your browser and navigate to `http://localhost:3000`
2. Upload a legal document (PDF, DOCX, or image)
3. Select your preferred language for translation (optional)
4. Click "Process Document" to start AI analysis
5. View simplified explanation and download results

## 📁 Project Structure

```
legalease/
├── frontend/                 # React frontend application
│   ├── public/              # Static files
│   ├── src/
│   │   ├── components/      # Reusable React components
│   │   ├── services/        # API service layer
│   │   ├── App.js          # Main application component
│   │   └── index.css       # Global styles
│   └── package.json        # Frontend dependencies
├── documents/               # Django app for document processing
│   ├── services/           # Business logic services
│   ├── views.py           # API endpoints
│   ├── models.py          # Data models
│   └── serializers.py     # API serializers
├── legalease/              # Django project configuration
│   ├── settings.py        # Project settings
│   └── urls.py           # URL routing
├── requirements.txt        # Python dependencies
├── manage.py              # Django management script
└── README.md             # Project documentation
```

## 🔧 API Endpoints

### Document Processing
- `POST /api/process-document/` - Process and simplify legal document
- `GET /api/health/` - API health check
- `GET /api/languages/` - Get supported languages

### Request/Response Examples

**Process Document:**
```json
POST /api/process-document/
Content-Type: multipart/form-data

{
  "file": "document.pdf",
  "target_language": "en"
}
```

**Response:**
```json
{
  "success": true,
  "file_info": {
    "name": "contract.pdf",
    "type": "pdf",
    "size_mb": 2.5
  },
  "results": {
    "original_text": "Complex legal text...",
    "simplified_text": "Simplified explanation...",
    "translated_text": "Translated content..."
  }
}
```

## 🎨 UI/UX Features

- **Professional Design**: Clean, modern interface with consistent styling
- **Interactive Elements**: Hover effects, smooth transitions, and visual feedback
- **Progress Indicators**: Real-time processing status with animated progress bars
- **Error Handling**: User-friendly error messages and validation
- **Responsive Layout**: Optimized for all screen sizes and devices
- **Accessibility**: Keyboard navigation and screen reader support

## 🧪 Testing

```bash
# Backend tests
python manage.py test

# Frontend tests
cd frontend
npm test
```

## 📈 Performance Optimizations

- **Code Splitting**: Lazy loading of React components
- **Optimized Assets**: Minified CSS and JavaScript in production
- **Efficient API**: RESTful design with proper HTTP status codes
- **Memory Management**: Efficient file processing without permanent storage
- **Responsive Images**: Optimized loading for different screen sizes

## 🔮 Future Enhancements

- [ ] User authentication and document history
- [ ] Batch document processing
- [ ] Advanced AI models for specialized legal domains
- [ ] Integration with cloud storage services
- [ ] Real-time collaboration features
- [ ] Mobile application development

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

**[Your Name]**
- LinkedIn: [linkedin.com/in/hemanthkokkonda](https://linkedin.com/in/hemanthkokkonda)
- Email: naveenhemanth4@gmail.com

## 🙏 Acknowledgments

- Groq API for advanced language processing capabilities
- Django and React communities for excellent documentation
- Open source contributors who make projects like this possible

---

⭐ **Star this repository if you found it helpful!**

*Making legal documents accessible to everyone through the power of AI.*
