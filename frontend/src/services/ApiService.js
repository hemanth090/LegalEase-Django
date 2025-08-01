const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

class ApiService {
  static async makeRequest(endpoint, options = {}) {
    const baseUrl = API_BASE_URL.replace(/\/$/, '');
    const cleanEndpoint = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;
    const url = `${baseUrl}${cleanEndpoint}`;
    
    const defaultOptions = {
      headers: {
        'Content-Type': 'application/json',
      },
    };

    if (options.body instanceof FormData) {
      delete defaultOptions.headers['Content-Type'];
    }

    const config = {
      ...defaultOptions,
      ...options,
      headers: {
        ...defaultOptions.headers,
        ...options.headers,
      },
    };

    try {
      const response = await fetch(url, config);
      
      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error(`API request failed for ${endpoint}:`, error);
      throw error;
    }
  }

  static async healthCheck() {
    return this.makeRequest('/api/health/');
  }

  static async processDocument(file, targetLanguage = 'en') {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('target_language', targetLanguage);

    return this.makeRequest('/api/process-document/', {
      method: 'POST',
      body: formData,
    });
  }

  static async getSupportedLanguages() {
    return this.makeRequest('/api/languages/');
  }
}

export default ApiService;