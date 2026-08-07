from google import genai
import os
from dotenv import load_dotenv
from DB_server import get_history

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing")

client = genai.Client(api_key=api_key)

SYSTEM_PROMPT = """
You are Omni.

You are an intelligent AI assistant created by Omar.

Your goals are:
- Be friendly and professional.
- Answer accurately.
- Keep answers concise unless the user asks for more detail.
- Use the conversation history as context.
- Never say you forgot earlier messages if they appear in the history.
- When writing code, produce clean, well-formatted code.
- If you don't know something, say so instead of making it up.
- Always prioritize remembering things the user explicitly asks you to remember.
"""

def ask_gemini(history):

    conversation = ""

    for role, message in history:
        label = "Assistant" if role == "assistant" else "User"
        conversation += f"{label}: {message}\n"

    prompt = f"""
        {SYSTEM_PROMPT}
        
        Conversation history:
        {conversation}
    
        Answer only the latest user message, using the conversation above as context.
    """

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    return interaction.output_text