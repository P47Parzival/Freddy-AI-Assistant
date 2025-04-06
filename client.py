from openai import OpenAI

client = OpenAI(
    api_key="",
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant named kaizen, consisting general task like alexa.",
        },
        {
            "role": "user",
            "content": "What is the capital of France?",
        },
    ],
)

print(completion.choices[0].message.content)