from openai import OpenAI

client = OpenAI(
    api_key="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",
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