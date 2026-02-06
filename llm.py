import openai, os

MODEL = "gpt-4o-mini"  # free tier compatible

def chat(q, memories):
    prompt = f"""
You are my personal assistant.
Be concise and practical.

MEMORIES ABOUT ME:
{memories}

User: {q}
"""
    r = openai.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return r.choices[0].message.content


def extract(q, a):
    """Decide what is worth remembering"""
    p = f"""
From this dialogue extract durable facts,
preferences, projects, or personal info.
Ignore small talk.

User: {q}
Assistant: {a}

Return one fact per line.
"""
    r = openai.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": p}]
    )
    return r.choices[0].message.content.split("\n")
