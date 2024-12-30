#pip install openai
from openai import OpenAI
client=OpenAI(api_key="your api")
# Create the chat completion request
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a hvirtual assitant named Jarvis skilled in regular question answering tasks for everyday works"},
        {"role": "user", "content": "What is coding."}
    ]
)

# Print the response message
print(completion.choices[0].message.content)