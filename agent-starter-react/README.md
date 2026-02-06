# Sara - AI Voice Assistant 💕

A cute, caring AI bestie voice assistant powered by Google Gemini and LiveKit. Sara speaks Hinglish and remembers your conversations!

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge" alt="Made with love">
  <img src="https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Next.js-15-black?style=for-the-badge&logo=next.js" alt="Next.js">
  <img src="https://img.shields.io/badge/LiveKit-Agents-purple?style=for-the-badge" alt="LiveKit">
</p>

## ✨ Features

- 🎤 **Real-time Voice Interaction** - Talk naturally with Sara using your microphone
- 🧠 **Memory System** - Sara remembers past conversations and context
- 🌤️ **Weather Integration** - Get real-time weather updates for your location
- 🗣️ **Hinglish Support** - Speaks in a mix of Hindi and English naturally
- 📱 **Mobile Support** - Access from your phone via HTTPS
- 🌙 **Dark/Light Theme** - Automatic theme switching
- 💕 **Cute Personality** - A caring bestie who's always there for you

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Node.js 18+
- pnpm

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/suvo1119/Sara-AI-Assistant.git
   cd Sara-AI-Assistant
   ```

2. **Install Python dependencies**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   pip install -r Jarvis_code/requirements.txt
   ```

3. **Install frontend dependencies**
   ```bash
   cd agent-starter-react
   pnpm install
   ```

4. **Configure environment variables**
   
   Create `.env` file in `agent-starter-react/`:
   ```env
   LIVEKIT_API_KEY=your_api_key
   LIVEKIT_API_SECRET=your_api_secret
   LIVEKIT_URL=wss://your-livekit-url
   ```

   Create `.env` file in `Jarvis_code/`:
   ```env
   LIVEKIT_API_KEY=your_api_key
   LIVEKIT_API_SECRET=your_api_secret
   LIVEKIT_URL=wss://your-livekit-url
   GOOGLE_API_KEY=your_google_gemini_api_key
   OPENWEATHER_API_KEY=your_openweather_api_key
   ```

5. **Run Sara**
   ```bash
   ./start_sara.sh
   ```

6. **Open in browser**
   - Desktop: https://localhost:3000
   - Mobile: https://YOUR_IP:3000

## 📁 Project Structure

```
Sara-AI-Assistant/
├── agent-starter-react/    # Frontend (Next.js)
│   ├── app/
│   ├── components/
│   └── ...
├── Jarvis_code/           # Backend (Python)
│   ├── agent.py           # Main voice agent
│   ├── Jarvis_prompts.py  # Sara's personality
│   ├── memory_store.py    # Conversation memory
│   └── ...
├── start_sara.sh          # Start script
└── Sara.desktop           # Desktop launcher
```

## 🛠️ Technologies

- **Frontend**: Next.js 15, React, TailwindCSS, LiveKit Components
- **Backend**: Python, LiveKit Agents, Google Gemini AI
- **Voice**: Google Gemini Realtime Audio (Kore voice)
- **Memory**: JSON-based conversation storage

## 📱 Mobile Access

Sara runs on HTTPS for mobile microphone access. When accessing from mobile:
1. Connect to the same WiFi network as your computer
2. Open `https://YOUR_COMPUTER_IP:3000`
3. Accept the self-signed certificate warning
4. Allow microphone access

## 🎨 Customization

Edit `app-config.ts` to customize:
- App name and branding
- Colors and themes
- Feature toggles

Edit `Jarvis_code/Jarvis_prompts.py` to customize:
- Sara's personality
- Response style
- Language preferences

## 📄 License

MIT License - feel free to use and modify!

## 👨‍💻 Author

**Suvadip Mondal**
- GitHub: [@suvo1119](https://github.com/suvo1119)

---

<p align="center">
  Made with 💕 by Suvadip Mondal
</p>

<p align="center">
  © 2026 Suvadip Mondal. All rights reserved.
</p>
