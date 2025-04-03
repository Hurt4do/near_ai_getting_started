import requests

def handle_message(message: str) -> str:
    message = message.lower()
    if "hello" in message:
        return "Hello, welcome to NEAR AI!"
    elif "info" in message:
        return "I am a customized agent created by Lau and ready for action!"
    elif "joke" in message:
        try:
            # Fetch a random joke from a public API
            response = requests.get("https://official-joke-api.appspot.com/random_joke")
            if response.status_code == 200:
                data = response.json()
                return f"Here's a joke: {data['setup']} ... {data['punchline']}"
            else:
                return "Sorry, I couldn't fetch a joke at the moment."
        except Exception as e:
            return f"Error fetching joke: {e}"
    elif "quote" in message:
        try:
            # Fetch a random quote from a public API
            response = requests.get("https://api.quotable.io/random")
            if response.status_code == 200:
                data = response.json()
                return f"Motivational Quote: '{data['content']}' — {data['author']}"
            else:
                return "Sorry, I couldn't fetch a quote right now."
        except Exception as e:
            return f"Error fetching quote: {e}"
    else:
        return "I'm sorry, I didn't understand your message."

