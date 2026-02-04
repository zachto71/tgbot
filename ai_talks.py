from openai import OpenAI

import os

from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("AI_TOKEN"),
)

def ai_response(all_messages):
  try:
    response = client.chat.completions.create(
      model="stepfun/step-3.5-flash:free",
      messages=[
        {"role": "system",
         "content": """Ты пишешь новости для желтушного онлайн сообщества. Выбери из полученной информации самые интересные
               новости (3-5 штук) и напиши о них добавляя много смайликов."""
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