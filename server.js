const express = require('express');
const app = express();
const API_KEY = process.env.MY_API_KEY || 'brak-klucza';

app.get('/', (req, res) => {
    res.send(`Aplikacja pogodowa działa z kluczem: ${API_KEY}`);
});

app.listen(3000, () => console.log('Server runs on port 3000'));

