from groq import Client

GROQ_API_KEY = "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"

def get_career_suggestions(skills, interests):
    client = Client(api_key=GROQ_API_KEY)


    user_input = (
        f"Based on the following skills: {skills} and interests: {interests}, "
        "suggest possible career options that align with industry trends. "
        "Also, recommend relevant courses, certifications, and projects to achieve the predicted job."
    )

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            model="llama3-8b-8192"  # Change this to the appropriate model as necessary
        )

        # Extract the generated content from the response
        suggestions = chat_completion.choices[0].message.content.strip()
        return suggestions

    except Exception as e:
        print(f"Error fetching suggestions: {e}")
        return "Unable to fetch career suggestions at this time."

