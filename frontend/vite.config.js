import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    outDir: '../dist',  // Output build files in `frontend/dist/`
    emptyOutDir: true,   // Clean old builds before building
  },
  server: {
    port: 5173,          // Vite development server port
    proxy: {
      '/api': 'http://127.0.0.1:5000' // Proxy Flask API calls
    }
  }
});
