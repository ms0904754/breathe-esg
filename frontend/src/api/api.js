import axios from "axios";

// Ensure the baseURL matches your running backend exactly
const api = axios.create({
  baseURL: 'http://127.0.0.1:8080/api', // Use 127.0.0.1 if localhost fails
});

// For FormData (file uploads), don't set Content-Type header
api.interceptors.request.use((config) => {
  if (config.data instanceof FormData) {
    delete config.headers["Content-Type"];
  }
  return config;
});

// Better error logging
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Log the message directly so it's visible without expanding the object
    console.error(`API Error (${error.response?.status || 'Network Error'}):`, error.message);
    console.dir(error.response?.data); // Show server-side validation/error details
    return Promise.reject(error);
  }
);

export default api;
