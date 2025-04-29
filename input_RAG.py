import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_mom(rag_output_text):
    # Define a strong system prompt to guide the LLM
    system_prompt = """
You are an expert assistant that transforms rough meeting summaries into perfect, professional Minutes of Meeting (MOM). 
Always structure the MOM like this:
- Meeting Title
- Date
- Attendees
- Agenda
- Discussion Points
- Action Items
- Next Steps
Use formal tone. Fill in missing information with "Not Specified" if not provided.
"""

    # Define the user prompt dynamically
    user_prompt = f"""
Raw Meeting Summary:
\"\"\"
{rag_output_text}
\"\"\"

Generate a professional MOM based on the above.
"""

    # Call OpenAI (or any LLM) to process the prompt
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2  # low randomness for professional output
    )

    # Extract and return the MOM
    return response['choices'][0]['message']['content']

# Example usage:
rag_output = "The context states that the Sales Committee reviewed quarterly sales targets and assigned follow-ups. However, it doesn’t specify the exact sales targets."
mom = generate_mom(rag_output)
print(mom)
