from openai import OpenAI

from datetime import timezone

from utils import *

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=AI_TOKEN,
)


def ai_response(message):
    try:
        with open(f"data/{message.chat.id}.txt", "r") as sms:
            all_messages = sms.read() + "\n" + str(datetime.now(timezone.utc))
        print(all_messages)
        response = client.chat.completions.create(
            model=AI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": AI_PROMPT
                },
                {
                    "role": "user",
                    "content": all_messages
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ошибка: {e}"
