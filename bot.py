# 📦 Install required library
import requests

API_KEY = "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"
url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

chat_history = [
    {
        "role": "system",
        "content": "You are a kind and caring mental health assistant. Always reply in a gentle, supportive, and emotionally intelligent manner. Guide the user through breathing, calming, or helpful thoughts. Avoid medical advice."
    }
]

def get_bot_reply(user_input):
    chat_history.append({"role": "user", "content": user_input})

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": chat_history
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        bot_reply = response.json()["choices"][0]["message"]["content"]
        chat_history.append({"role": "assistant", "content": bot_reply})
        return bot_reply
    else:
        chat_history.pop()
        return "Sorry, something went wrong. Please try again later."



