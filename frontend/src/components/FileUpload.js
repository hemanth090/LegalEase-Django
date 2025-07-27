import React from 'react';

const FileUpload = ({ onFileSelect, disabled, selectedFile }) => {
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      // Validate file size (10MB limit)
      if (file.size > 10 * 1024 * 1024) {
        alert('File too large. Maximum size is 10MB.');
        return;
      }
      
      // Validate file type
      const allowedTypes = [
        'application/pdf',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'image/jpeg',
        'image/jpg',
        'image/png',
        'image/gif'
      ];
      
      if (!allowedTypes.includes(file.type)) {
        alert('Unsupported file type. Please upload PDF, DOCX, or image files.');
        return;
      }
      
      onFileSelect(file);
    }
  };

  const handleDrop = (event) => {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    if (file) {
      const fakeEvent = {
        target: {
          files: [file]
        }
      };
      handleFileChange(fakeEvent);
    }
  };

  const handleDragOver = (event) => {
    event.preventDefault();
  };

  const formatFileSize = (bytes) => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  const getFileIcon = (file) => {
    if (!file) return '📄';
    
    if (file.type.includes('pdf')) return '📕';
    if (file.type.includes('word') || file.type.includes('document')) return '📘';
    if (file.type.includes('image')) return '🖼️';
    return '📄';
  };

  return (
    <div className="file-upload-container">
      <div
        className={`dropzone ${disabled ? 'disabled' : ''}`}
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        onClick={() => !disabled && document.getElementById('file-input').click()}
      >
        <input
          id="file-input"
          type="file"
          accept=".pdf,.docx,.jpg,.jpeg,.png,.gif"
          onChange={handleFileChange}
          disabled={disabled}
          style={{ display: 'none' }}
        />
        
        {selectedFile ? (
          <div className="file-selected">
            <div className="file-icon">
              {getFileIcon(selectedFile)}
            </div>
            <div className="file-details">
              <div className="file-name">{selectedFile.name}</div>
              <div className="file-meta">
                <span className="file-size">{formatFileSize(selectedFile.size)}</span>
                <span className="file-type">{selectedFile.type.split('/')[1].toUpperCase()}</span>
              </div>
            </div>
            <div className="file-status">
              ✅ Ready to process
            </div>
          </div>
        ) : (
          <div className="dropzone-content">
            <div className="dropzone-icon">📁</div>
            <div className="dropzone-text">
              {disabled ? 'Processing...' : 'Drop your legal document here or click to browse'}
            </div>
            <div className="dropzone-subtext">
              Supports PDF, DOCX, and image files (max 10MB)
            </div>
          </div>
        )}
      </div>
      
      {selectedFile && !disabled && (
        <div className="file-actions">
          <button
            className="btn btn-secondary btn-small"
            onClick={() => onFileSelect(null)}
          >
            🗑️ Remove File
          </button>
        </div>
      )}
    </div>
  );
};

export default FileUpload;