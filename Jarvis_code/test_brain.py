import asyncio
import logging
from jarvis_reasoning import thinking_capability
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(level=logging.INFO)
load_dotenv()

async def main():
    print("🧠 Jarvis Brain Tester (Linux)")
    print("Type 'exit' to quit.\n")
    
    while True:
        query = input("You: ")
        if query.lower() in ['exit', 'quit']:
            break
            
        print("Thinking...")
        try:
            response = await thinking_capability(query)
            print(f"Jarvis: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    asyncio.run(main())
