# Sara - AI Voice Assistant 💕

A cute, caring AI  voice assistant powered by Google Gemini and LiveKit. Sara speaks Hinglish and remembers your conversations!

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge" alt="Made with love">
  <img src="https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Next.js-15-black?style=for-the-badge&logo=next.js" alt="Next.js">
  <img src="https://img.shields.io/badge/Google%20Gemini-AI-4285F4?style=for-the-badge&logo=google" alt="Gemini">
  <img src="https://img.shields.io/badge/LiveKit-Agents-purple?style=for-the-badge" alt="LiveKit">
</p>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎤 **Voice Interaction** | Real-time conversation with natural voice |
| 🧠 **Memory System** | Remembers past conversations |
| 🌤️ **Weather Updates** | Real-time weather for your city |
| 🗣️ **Hinglish** | Speaks Hindi-English mix naturally |
| 📱 **Mobile Support** | Access from phone via HTTPS |
| 🌙 **Themes** | Auto dark/light mode |
| 💕 **Personality** | A caring bestie vibe |

---

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/suvo1119/Sara-AI-Assistant.git
cd Sara-AI-Assistant

# Setup Python
python -m venv .venv
source .venv/bin/activate
pip install -r Jarvis_code/requirements.txt

# Setup Frontend
cd agent-starter-react
pnpm install
cd ..

# Run Sara
./start_sara.sh
```

Open **https://localhost:3000** in your browser 🎉

---

## 📁 Project Structure

```
Sara-AI-Assistant/
├── agent-starter-react/   # 🌐 Frontend (Next.js)
├── Jarvis_code/           # 🤖 Backend (Python Agent)
│   ├── agent.py           # Main voice agent
│   ├── Jarvis_prompts.py  # Sara's personality
│   └── memory_store.py    # Conversation memory
├── start_sara.sh          # 🚀 Start script
└── Sara.desktop           # 🖥️ Desktop launcher
```

---

## ⚙️ Configuration

### Environment Variables

Create `.env` files with your API keys:

**Jarvis_code/.env:**
```env
LIVEKIT_API_KEY=your_key
LIVEKIT_API_SECRET=your_secret
LIVEKIT_URL=wss://your-livekit-url
GOOGLE_API_KEY=your_gemini_key
OPENWEATHER_API_KEY=your_weather_key
```

---

## 📱 Mobile Access

1. Run Sara with `./start_sara.sh`
2. Open `https://YOUR_IP:3000` on mobile
3. Accept the certificate warning
4. Allow microphone access

---

## 🛠️ Tech Stack

- **Frontend**: Next.js 15, React, TailwindCSS
- **Backend**: Python, LiveKit Agents
- **AI**: Google Gemini Realtime Audio
- **Voice**: Kore (Female voice)

---

## 👨‍💻 Author

**Suvadip Mondal**

[![GitHub](https://img.shields.io/badge/GitHub-suvo1119-181717?style=for-the-badge&logo=github)](https://github.com/suvo1119)

---

<p align="center">
  Made with 💕 by Suvadip Mondal<br>
  © 2026 Suvadip Mondal. All rights reserved.
</p>
