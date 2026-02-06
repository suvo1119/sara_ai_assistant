#!/bin/bash

# 🌸 Start Sara - Your Cute AI Bestie 💕

echo "💕 Starting Sara..."
echo ""

# Kill any existing processes
pkill -f "agent.py" 2>/dev/null
pkill -f "next dev" 2>/dev/null
sleep 1

# Start the frontend in background
echo "🌐 Starting frontend..."
cd /home/suvadip/Desktop/sara_assistant/agent-starter-react
pnpm dev &
FRONTEND_PID=$!

# Wait a moment for frontend to start
sleep 3

# Start the agent
echo "🤖 Starting Sara agent..."
cd /home/suvadip/Desktop/sara_assistant/Jarvis_code
/home/suvadip/Desktop/sara_assistant/.venv/bin/python agent.py dev &
AGENT_PID=$!

echo ""
echo "✨ Sara is ready! 💕"
echo "🌐 Open https://localhost:3000 in your browser"
echo "📱 For mobile: https://$(hostname -I | awk '{print $1}'):3000"
echo ""
echo "Press Ctrl+C to stop Sara"

# Wait for both processes
wait $FRONTEND_PID $AGENT_PID
