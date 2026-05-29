import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://127.0.0.1:8000/api",
});

// For FormData (file uploads), don't set Content-Type header
// Let the browser set it automatically with the boundary
api.interceptors.request.use((config) => {
  if (config.data instanceof FormData) {
    // Don't set Content-Type for FormData - let browser handle it
    delete config.headers["Content-Type"];
  }
  return config;
});

export default api;
