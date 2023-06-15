module.exports = {
  devServer: {
    proxy: {
      '/social-auth/login/google-oauth2': {
        target: 'http://localhost:8000',
        ws: true,
        changeOrigin: true
      }
    }
  }
}
