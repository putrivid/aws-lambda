const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

// Proxy API Gateway
app.use('/api', createProxyMiddleware({
    target: 'https://bsgzh293hh.execute-api.ap-southeast-2.amazonaws.com/prod/',
    changeOrigin: true,
    pathRewrite: {
        '^/api': '', // Hapus prefix "/api" jika diperlukan
    },
}));

// Jalankan server di port 5000
app.listen(5000, () => {
    console.log('Proxy server berjalan di http://localhost:5000');
});
