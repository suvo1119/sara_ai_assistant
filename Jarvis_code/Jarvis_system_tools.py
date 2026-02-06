import os
import psutil
import logging
import subprocess
import datetime
import pyperclip
from langchain.tools import tool

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@tool
async def system_status(query: str = "") -> str:
    """
    Returns the current system status including CPU usage, RAM usage, and Disk space.
    
    Use this tool when the user asks about computer health, performance, or resources.
    Example: "System status kya hai?", "kitna RAM use ho raha hai?"
    """
    try:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        status = (f"🖥️ System Status:\n"
                  f"- CPU Usage: {cpu}%\n"
                  f"- RAM Usage: {memory.percent}% ({memory.used // (1024**3)}GB / {memory.total // (1024**3)}GB)\n"
                  f"- Disk Usage: {disk.percent}% ({disk.free // (1024**3)}GB free)")
        
        logger.info("Fetched system status")
        return status
    except Exception as e:
        logger.error(f"Error fetching system status: {e}")
        return "❌ System status fetch karne mein error aaya."

@tool
async def take_screenshot(query: str = "") -> str:
    """
    Takes a screenshot of the current screen and saves it to the Pictures folder.
    
    Use this tool when the user asks to take a screenshot or capture the screen.
    """
    try:
        pictures_dir = os.path.join(os.path.expanduser("~"), "Pictures")
        if not os.path.exists(pictures_dir):
            os.makedirs(pictures_dir)
            
        filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(pictures_dir, filename)
        
        # Try gnome-screenshot first, then fallback to scrot, then import (imagemagick)
        if os.system(f"gnome-screenshot -f {filepath}") == 0:
            return f"📸 Screenshot saved to {filepath}"
        elif os.system(f"scrot {filepath}") == 0:
            return f"📸 Screenshot saved to {filepath}"
        else:
            # Fallback using python library if system tools fail (Linux specific usually require tools)
            return "❌ Screenshot tools (gnome-screenshot/scrot) not found. Please install them."
            
    except Exception as e:
        logger.error(f"Error taking screenshot: {e}")
        return f"❌ Screenshot lene mein failed: {e}"

@tool
async def read_clipboard(query: str = "") -> str:
    """
    Reads the text currently copied to the clipboard.
    """
    try:
        content = pyperclip.paste()
        return f"📋 Clipboard Content: {content}"
    except Exception as e:
        return f"❌ Clipboard read fail: {e}"

@tool
async def write_clipboard(text: str) -> str:
    """
    Writes text to the system clipboard.
    """
    try:
        pyperclip.copy(text)
        return "✅ Text clipboard par copy ho gaya."
    except Exception as e:
        return f"❌ Clipboard write fail: {e}"
