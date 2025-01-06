import openai
import os

openai.api_key = os.getenv("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")

def Chat_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("ChatBot is running! Type 'quit', 'bye', or 'exit' to end the conversation.")
    while True:
        user = input('You: ')
        if user.lower() in ('quit', 'bye', 'exit'):
            print('ChatBot: Ok bye! Have a nice day :)')
            break
        response = Chat_gpt(user)
        print(f'ChatBot: {response}')
