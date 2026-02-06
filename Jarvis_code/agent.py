from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions, ChatContext, ChatMessage
from livekit.plugins import google, noise_cancellation

# Import your custom modules
from Jarvis_prompts import instructions_prompt, Reply_prompts
from memory_loop import MemoryExtractor
from memory_store import ConversationMemory
from jarvis_reasoning import thinking_capability
load_dotenv()


def get_past_memories(max_messages: int = 30) -> str:
    """Load past conversation memories and format them as context string"""
    memory = ConversationMemory("default_user")
    recent_messages = memory.get_recent_context(max_messages)
    
    if not recent_messages:
        return ""
    
    memory_context = "\n\n--- पिछली बातचीत से याद ---\n"
    for msg in recent_messages:
        role = msg.get('role', 'unknown')
        content = msg.get('content', '')
        if role == 'user':
            memory_context += f"User ने बोला था: {content}\n"
        elif role == 'assistant':
            memory_context += f"Sara ने बोला था: {content}\n"
    memory_context += "--- याद समाप्त ---\n\n"
    
    return memory_context


class Assistant(Agent):
    def __init__(self, chat_ctx, memory_context: str = "") -> None:
        # Add memory context to instructions
        full_instructions = instructions_prompt
        if memory_context:
            full_instructions += f"\n\n{memory_context}\nइन पिछली बातों को याद रखो और conversation में naturally refer करो जब relevant हो।"
        
        super().__init__(chat_ctx = chat_ctx,
                        instructions=full_instructions,
                        llm=google.beta.realtime.RealtimeModel(
                            model="gemini-2.5-flash-native-audio-latest",
                            voice="Kore",  # Cute female voice for Sara 💕
                        ),
                        tools=[thinking_capability]
                                )

async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        preemptive_generation=True
    )
    
    # Load past memories
    past_memories = get_past_memories()
    
    #getting the current memory chat
    current_ctx = session.history.items
    

    await session.start(
        room=ctx.room,
        agent=Assistant(chat_ctx=current_ctx, memory_context=past_memories), #sending currenet chat to llm in realtime
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC()
        ),
    )
    await session.generate_reply(
        instructions=Reply_prompts
    )
    conv_ctx = MemoryExtractor()
    await conv_ctx.run(current_ctx)
    


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))

    