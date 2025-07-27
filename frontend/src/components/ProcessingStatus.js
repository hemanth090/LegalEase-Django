import React, { useState, useEffect } from 'react';

const ProcessingStatus = () => {
  const [currentStep, setCurrentStep] = useState(0);
  const [progress, setProgress] = useState(0);

  const steps = [
    { id: 1, title: 'Uploading file', description: 'Sending your document to the server...', icon: '📤' },
    { id: 2, title: 'Extracting text', description: 'Reading and extracting text from your document...', icon: '📖' },
    { id: 3, title: 'AI Analysis', description: 'Simplifying legal language with AI...', icon: '🤖' },
    { id: 4, title: 'Translation', description: 'Translating to your selected language...', icon: '🌐' },
    { id: 5, title: 'Finalizing', description: 'Preparing your results...', icon: '✨' }
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentStep(prev => {
        const next = prev + 1;
        if (next >= steps.length) {
          clearInterval(interval);
          return steps.length - 1;
        }
        return next;
      });
      
      setProgress(prev => {
        const newProgress = prev + 20;
        return newProgress > 100 ? 100 : newProgress;
      });
    }, 1500);

    return () => clearInterval(interval);
  }, [steps.length]);

  return (
    <div className="processing-status">
      <div className="processing-header">
        <h3 className="processing-title">
          <span className="loading-spinner"></span>
          Processing Your Document
        </h3>
        <div className="progress-bar">
          <div 
            className="progress-fill" 
            style={{ width: `${progress}%` }}
          ></div>
        </div>
        <div className="progress-text">{progress}% Complete</div>
      </div>

      <div className="processing-steps">
        {steps.map((step, index) => (
          <div 
            key={step.id}
            className={`processing-step ${
              index < currentStep ? 'completed' : 
              index === currentStep ? 'active' : 'pending'
            }`}
          >
            <div className="step-icon">
              {index < currentStep ? '✅' : 
               index === currentStep ? step.icon : '⏳'}
            </div>
            <div className="step-content">
              <div className="step-title">{step.title}</div>
              <div className="step-description">{step.description}</div>
            </div>
            {index === currentStep && (
              <div className="step-spinner">
                <span className="loading-spinner"></span>
              </div>
            )}
          </div>
        ))}
      </div>

      <div className="processing-tips">
        <div className="tip-title">💡 Did you know?</div>
        <div className="tip-content">
          {currentStep === 0 && "Your documents are processed in memory only and never stored permanently."}
          {currentStep === 1 && "We support PDF, DOCX, and image files with OCR text extraction."}
          {currentStep === 2 && "Our AI simplifies complex legal jargon into plain English."}
          {currentStep === 3 && "We support translation to over 75 languages worldwide."}
          {currentStep >= 4 && "All processing is done securely and your data is never saved."}
        </div>
      </div>
    </div>
  );
};

export default ProcessingStatus;