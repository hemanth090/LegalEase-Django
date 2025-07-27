import React, { useState, useEffect } from 'react';
import FileUpload from './components/FileUpload';
import LanguageSelector from './components/LanguageSelector';
import ProcessingStatus from './components/ProcessingStatus';
import ResultsDisplay from './components/ResultsDisplay';
import ApiService from './services/ApiService';

function App() {
  const [file, setFile] = useState(null);
  const [language, setLanguage] = useState('en');
  const [processing, setProcessing] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [apiStatus, setApiStatus] = useState('checking');

  useEffect(() => {
    checkApiHealth();
  }, []);

  const checkApiHealth = async () => {
    try {
      await ApiService.healthCheck();
      setApiStatus('connected');
    } catch (error) {
      setApiStatus('error');
      console.error('API Health Check Failed:', error);
    }
  };

  const handleFileSelect = (selectedFile) => {
    setFile(selectedFile);
    setResult(null);
    setError(null);
  };

  const handleLanguageChange = (selectedLanguage) => {
    setLanguage(selectedLanguage);
  };

  const handleProcessDocument = async () => {
    if (!file) {
      setError('Please select a file first');
      return;
    }

    setProcessing(true);
    setError(null);
    setResult(null);

    try {
      const response = await ApiService.processDocument(file, language);
      setResult(response);
    } catch (error) {
      setError(error.message || 'Failed to process document');
      console.error('Processing error:', error);
    } finally {
      setProcessing(false);
    }
  };

  const handleReset = () => {
    setFile(null);
    setResult(null);
    setError(null);
    setProcessing(false);
  };

  return (
    <div className="App">
      <div className="container">
        <header className="app-header">
          <h1 className="app-title">
            🏛️ LegalEase
          </h1>
          <p className="app-subtitle">
            Transform complex legal documents into clear, understandable explanations
          </p>
          <div className={`api-status ${apiStatus}`}>
            {apiStatus === 'checking' && '🔄 Checking API connection...'}
            {apiStatus === 'connected' && '✅ Connected to Django backend'}
            {apiStatus === 'error' && '❌ Cannot connect to backend - make sure Django server is running'}
          </div>
        </header>

        <main className="app-main">
          <div className="glass-card">
            <div className="upload-section">
              <h2 className="section-title">📄 Upload Document</h2>
              <FileUpload 
                onFileSelect={handleFileSelect}
                disabled={processing}
                selectedFile={file}
              />
            </div>

            {file && !processing && !result && (
              <div className="options-section">
                <h2 className="section-title">⚙️ Processing Options</h2>
                <LanguageSelector
                  selectedLanguage={language}
                  onLanguageChange={handleLanguageChange}
                  disabled={processing}
                />
                
                <div className="action-buttons">
                  <button
                    className="btn btn-primary"
                    onClick={handleProcessDocument}
                    disabled={processing || !file}
                  >
                    🚀 Process Document
                  </button>
                  
                  <button
                    className="btn btn-secondary"
                    onClick={handleReset}
                    disabled={processing}
                  >
                    🔄 Reset
                  </button>
                </div>
              </div>
            )}

            {processing && <ProcessingStatus />}

            {error && (
              <div className="alert alert-error">
                <strong>Error:</strong> {error}
                <button
                  className="btn btn-small"
                  onClick={() => setError(null)}
                  style={{ marginLeft: '12px' }}
                >
                  ✕ Dismiss
                </button>
              </div>
            )}

            {result && (
              <div>
                <ResultsDisplay result={result} />
                <div style={{ 
                  textAlign: 'center', 
                  marginTop: '20px',
                  paddingTop: '20px',
                  borderTop: '1px solid var(--border)'
                }}>
                  <button
                    className="btn btn-secondary"
                    onClick={handleReset}
                  >
                    🔄 Process Another Document
                  </button>
                </div>
              </div>
            )}
          </div>
        </main>

        <footer className="app-footer">
          <p>
            Made with ❤️ to make legal documents accessible to everyone
          </p>
          <div className="footer-links">
            <a href="/admin" target="_blank" rel="noopener noreferrer">
              Admin Panel
            </a>
            <a href="https://github.com" target="_blank" rel="noopener noreferrer">
              GitHub
            </a>
          </div>
        </footer>
      </div>
    </div>
  );
}

export default App;