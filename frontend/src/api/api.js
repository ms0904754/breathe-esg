import axios from "axios";

const api = axios.create({
  baseURL: "https://breathe-esg-production-6dd5.up.railway.app/api",
});

export default api;