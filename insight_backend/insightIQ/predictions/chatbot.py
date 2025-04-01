import openai

# Replace with your actual OpenAI API key
openai.api_key = "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"

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

