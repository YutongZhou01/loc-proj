import { fileURLToPath, URL } from 'node:url'
import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      // Set up an alias for the "src" directory
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    // Allow access to the development server from the network
    host: true,
    // Use port 80 for the development server
    port: 80,
    // Watch for file changes using polling (useful in some setups)
    watch: {
      usePolling: true
    }
  }
})
