import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'
import { viteSingleFile } from "vite-plugin-singlefile"

export default defineConfig({
  plugins: [vue(), viteSingleFile()],
  build: {
    cssCodeSplit: false,
    assetsInlineLimit: 100000000,
    emptyOutDir: true,
    rollupOptions: {
      outputOptions: {
        inlineDynamicImports: true,
        manualChunks: () => "everything.js",
      },
    },
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),
    },
  },
  server: {
    open: true,
  },
})
