import React, { useState, useEffect } from 'react';
import ApiService from '../services/ApiService';

const LanguageSelector = ({ selectedLanguage, onLanguageChange, disabled }) => {
  const [languages, setLanguages] = useState({});
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');

  // Default languages in case API fails
  const defaultLanguages = {
    'en': 'English (No translation)',
    'es': 'Spanish - Español',
    'fr': 'French - Français',
    'de': 'German - Deutsch',
    'hi': 'Hindi - हिंदी',
    'zh': 'Chinese - 中文',
    'ar': 'Arabic - العربية',
    'pt': 'Portuguese - Português',
    'ru': 'Russian - Русский',
    'ja': 'Japanese - 日本語',
    'it': 'Italian - Italiano',
    'ko': 'Korean - 한국어',
    'th': 'Thai - ไทย',
    'vi': 'Vietnamese - Tiếng Việt',
    'nl': 'Dutch - Nederlands',
    'pl': 'Polish - Polski',
    'sv': 'Swedish - Svenska',
    'da': 'Danish - Dansk',
    'no': 'Norwegian - Norsk',
    'fi': 'Finnish - Suomi'
  };

  useEffect(() => {
    loadLanguages();
  }, []);

  const loadLanguages = async () => {
    try {
      const response = await ApiService.getSupportedLanguages();
      if (response.success && response.languages) {
        setLanguages(response.languages);
      } else {
        setLanguages(defaultLanguages);
      }
    } catch (error) {
      console.error('Failed to load languages:', error);
      setLanguages(defaultLanguages);
    } finally {
      setLoading(false);
    }
  };

  const filteredLanguages = Object.entries(languages).filter(([code, name]) =>
    name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    code.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const popularLanguages = ['en', 'es', 'fr', 'de', 'hi', 'zh', 'ar', 'pt'];

  const handleLanguageSelect = (languageCode) => {
    onLanguageChange(languageCode);
    setSearchTerm('');
  };

  if (loading) {
    return (
      <div className="language-selector">
        <label className="form-label">🌐 Target Language</label>
        <div className="loading-container">
          <span className="loading-spinner"></span>
          Loading languages...
        </div>
      </div>
    );
  }

  return (
    <div className="language-selector">
      <label className="form-label">🌐 Target Language</label>
      
      <div className="language-search">
        <input
          type="text"
          className="form-input"
          placeholder="Search languages..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          disabled={disabled}
        />
      </div>

      {!searchTerm && (
        <div className="popular-languages">
          <div className="popular-title">Popular Languages:</div>
          <div className="language-chips">
            {popularLanguages.map(code => (
              languages[code] && (
                <button
                  key={code}
                  className={`language-chip ${selectedLanguage === code ? 'selected' : ''}`}
                  onClick={() => handleLanguageSelect(code)}
                  disabled={disabled}
                >
                  {languages[code].split(' - ')[0]}
                </button>
              )
            ))}
          </div>
        </div>
      )}

      <div className="language-list">
        {filteredLanguages.length > 0 ? (
          filteredLanguages.map(([code, name]) => (
            <div
              key={code}
              className={`language-option ${selectedLanguage === code ? 'selected' : ''} ${disabled ? 'disabled' : ''}`}
              onClick={() => !disabled && handleLanguageSelect(code)}
            >
              <div className="language-code">{code.toUpperCase()}</div>
              <div className="language-name">{name}</div>
              {selectedLanguage === code && (
                <div className="language-selected">✓</div>
              )}
            </div>
          ))
        ) : (
          <div className="no-languages">
            No languages found matching "{searchTerm}"
          </div>
        )}
      </div>

      <div className="selected-language-display">
        <strong>Selected:</strong> {languages[selectedLanguage] || selectedLanguage}
      </div>
    </div>
  );
};

export default LanguageSelector;