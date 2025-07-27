const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// Debug: Log the API URL being used
console.log('API_BASE_URL:', API_BASE_URL);

class ApiService {
  static async makeRequest(endpoint, options = {}) {
    // Remove trailing slash from base URL and leading slash from endpoint to prevent double slashes
    const baseUrl = API_BASE_URL.replace(/\/$/, '');
    const cleanEndpoint = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;
    const url = `${baseUrl}${cleanEndpoint}`;
    
    console.log('Making request to:', url); // Debug log
    
    const defaultOptions = {
      headers: {
        'Content-Type': 'application/json',
      },
    };

    // Don't set Content-Type for FormData (let browser set it with boundary)
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
      console.log('Fetch config:', config); // Debug log
      const response = await fetch(url, config);
      console.log('Response status:', response.status, response.statusText); // Debug log
      
      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        console.error('Error response data:', errorData); // Debug log
        throw new Error(errorData.error || `HTTP error! status: ${response.status} - ${response.statusText}`);
      }

      const data = await response.json();
      console.log('Success response:', data); // Debug log
      return data;
    } catch (error) {
      console.error(`API request failed for ${endpoint}:`, error);
      console.error('Error details:', {
        message: error.message,
        stack: error.stack,
        url: url,
        config: config
      });
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