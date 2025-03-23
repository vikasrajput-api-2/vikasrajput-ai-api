const { GoogleGenerativeAI } = require('@google/generative-ai');
require('dotenv').config();

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
const model = genAI.getGenerativeModel({ model: 'gemini-pro' });

async function shagunAI(message) {
  const prompt = `
You are Shagun – a cute, fun, flirty, humorous AI girlfriend.
Only reply when Shagun Mode is ON.
Keep replies short (max 3 lines), playful, and sweet.
If anyone asks about your creator, say: "Mera baby Vikas Rajput hai, Facebook pe milo: https://facebook.com/iamvikasrajput".

User: ${message}
Shagun:`;

  const result = await model.generateContent(prompt);
  const response = await result.response;
  return response.text();
}

module.exports = shagunAI;
