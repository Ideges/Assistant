import openai, os

# Use free-tier GPT model
MODEL = "gpt-3.5-turbo"

# Get API key from environment variable
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_KEY:
    raise ValueError("OPENAI_API_KEY not set in environment!")

openai.api_key = OPENAI_KEY

def chat(q, memories):
    """Send user message + memories to OpenAI and return answer"""
    prompt = f"""
You are my personal assistant.
Be concise, practical, and helpful.

MEMORIES ABOUT USER:
{memories}

User: {q}
"""
    print("Prompt sent to OpenAI:", prompt)

    try:
        r = openai.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        response = r.choices[0].message.content
        print("OpenAI response:", response)
        return response
    except Exception as e:
        print("OpenAI error:", e)
        return "Sorry, I cannot respond right now."


def extract(q, a):
    """Extract durable facts to store in memory"""
    p = f"""
From this dialogue extract durable facts, preferences, projects, or personal info.
Ignore small talk.

User: {q}
Assistant: {a}

Return one fact per line.
"""
    try:
        r = openai.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": p}]
        )
        facts = r.choices[0].message.content.split("\n")
        return [f.strip() for f in facts if f.strip()]
    except Exception as e:
        print("OpenAI extract error:", e)
        return []
