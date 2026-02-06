import os
import asyncio
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from livekit.agents import function_tool


# ---- Import your Jarvis Tools ----
from Jarvis_ddg_search import duckduckgo_search
from Jarvis_google_search import get_current_datetime
from jarvis_get_weather import get_weather
from Jarvis_window_CTRL import open_app, close_app, folder_file
from Jarvis_file_opener import Play_file
from Jarvis_system_tools import system_status, take_screenshot, read_clipboard, write_clipboard

# ---- Load environment variables ----
load_dotenv()

# ---- Initialize Gemini Model ----
# valid models: gemini-flash-latest
model = ChatGoogleGenerativeAI(model="gemini-flash-latest", google_api_key=os.getenv("GOOGLE_API_KEY"))


@function_tool(
    name="thinking_capability",
    description=(
        "Main reasoning and action function for Jarvis. "
        "It can perform DuckDuckGo searches, open or close apps, fetch weather, access files, "
        "check system status, take screenshots, and manage clipboard."
    )
)
async def thinking_capability(query: str) -> dict:
    """
    Main LangChain-powered reasoning tool for Jarvis.
    Takes a natural language query and executes the correct workflow.
    """
    try:
        tools = [
            duckduckgo_search,
            get_current_datetime,
            get_weather,
            open_app,
            close_app,
            folder_file,
            Play_file,
            system_status,
            take_screenshot,
            read_clipboard,
            write_clipboard
        ]

        from langchain.agents import initialize_agent, AgentType
        
        # Use initialize_agent which handles prompt and executor creation automatically
        agent_executor = initialize_agent(
            tools=tools,
            llm=model,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            handle_parsing_errors=True
        )

        # Execute the agent asynchronously
        result = await agent_executor.ainvoke({"input": query})
        
        return {"result": result["output"]}

    except Exception as e:
        return {"error": f"Agent execution failed: {str(e)}"}


# ---------------- Manual Testing Section ---------------- #
# This section runs only if you execute this file directly.
# Remove or comment it out when using from agents.py
if __name__ == "__main__":
    async def main():

        while True:
            user_input = input("💬 Command: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print("👋 Goodbye, shutting down Jarvis...")
                break

            try:
                response = await thinking_capability(user_input)
                print("\n🧠 Response:", response, "\n")
            except Exception as e:
                print("\n⚠️ Error:", str(e), "\n")

    asyncio.run(main())