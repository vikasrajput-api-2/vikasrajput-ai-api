const express = require('express');
const bodyParser = require('body-parser');
require('dotenv').config();
const shagunAI = require('./gemini');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());

app.get('/', (req, res) => {
  res.send('Shagun AI Bot is running… kya haal hai baby?');
});

app.post('/ask', async (req, res) => {
  const { message } = req.body;

  if (!message) return res.status(400).json({ error: 'Message is required!' });

  try {
    const reply = await shagunAI(message);
    res.json({ reply });
  } catch (error) {
    res.status(500).json({ error: 'Something went wrong!' });
  }
});

app.listen(PORT, () => {
  console.log(`Shagun is live at http://localhost:${PORT}`);
});
