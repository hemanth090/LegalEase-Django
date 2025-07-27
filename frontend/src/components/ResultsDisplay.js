import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';

const ResultsDisplay = ({ result }) => {
  const [activeTab, setActiveTab] = useState('simplified');
  const [copySuccess, setCopySuccess] = useState('');

  if (!result) return null;

  const { original_text = '', simplified_text = '', translated_text = '' } = result.results || {};
  const { name: fileName = 'document', type: fileType = 'unknown' } = result.file_info || {};

  const copyToClipboard = async (text, type) => {
    try {
      await navigator.clipboard.writeText(text);
      setCopySuccess(type);
      setTimeout(() => setCopySuccess(''), 2000);
    } catch (err) {
      console.error('Copy failed:', err);
    }
  };

  const downloadText = (content, filename) => {
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
  };

  const formatText = (text) => {
    if (!text) return 'No content available';
    return text.length > 8000 ? text.substring(0, 8000) + '...\n\n[Text truncated]' : text;
  };

  const tabs = [
    { id: 'simplified', label: '🤖 Simplified', content: simplified_text },
    { id: 'original', label: '📄 Original', content: original_text },
    ...(translated_text ? [{ id: 'translated', label: '🌐 Translation', content: translated_text }] : [])
  ];

  const activeContent = tabs.find(tab => tab.id === activeTab)?.content || '';

  return (
    <div className="results-display">
      <div className="results-header">
        <h2 className="results-title">✅ Processing Complete!</h2>
        <div className="file-info">
          <span>📄 {fileName}</span>
          <span>📊 {fileType.toUpperCase()}</span>
          <span>🌐 {result.target_language || 'English'}</span>
        </div>
      </div>

      <div className="results-tabs">
        {tabs.map(tab => (
          <button
            key={tab.id}
            className={`tab-button ${activeTab === tab.id ? 'active' : ''}`}
            onClick={() => setActiveTab(tab.id)}
          >
            {tab.label}
          </button>
        ))}
      </div>

      <div className="result-section">
        <div className="section-header">
          <h3 className="section-title">
            {tabs.find(tab => tab.id === activeTab)?.label}
          </h3>
          <div className="section-actions">
            <button
              className="btn btn-small"
              onClick={() => copyToClipboard(activeContent, activeTab)}
            >
              {copySuccess === activeTab ? '✅ Copied!' : '📋 Copy'}
            </button>
            <button
              className="btn btn-small"
              onClick={() => downloadText(activeContent, `${fileName}_${activeTab}.txt`)}
            >
              💾 Download
            </button>
          </div>
        </div>
        
        <div className="result-content">
          {activeTab === 'original' ? (
            <pre style={{ whiteSpace: 'pre-wrap', fontFamily: 'SF Mono, Monaco, monospace' }}>
              {formatText(activeContent)}
            </pre>
          ) : (
            <div className="markdown-content">
              <ReactMarkdown>{formatText(activeContent)}</ReactMarkdown>
            </div>
          )}
        </div>
      </div>

      <div className="results-footer">
        <div className="processing-info">
          <h4>📊 Summary</h4>
          <div className="info-grid">
            <div>Original: {original_text?.length || 0} chars</div>
            <div>Simplified: {simplified_text?.length || 0} chars</div>
            {translated_text && <div>Translation: {translated_text.length} chars</div>}
          </div>
        </div>
        
        <div className="privacy-notice">
          <h4>🔒 Privacy</h4>
          <p>Your document was processed in memory only and automatically deleted. No data is stored.</p>
        </div>
      </div>
    </div>
  );
};

export default ResultsDisplay;