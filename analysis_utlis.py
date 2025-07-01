from openai import OpenAI
from config import DATABRICKS_TOKEN, BASE_URL

claude_client = OpenAI(
    api_key=DATABRICKS_TOKEN,
    base_url=BASE_URL
)

def analyze_with_claude(prompt, text):
    try:
        messages = [
            {"role": "system", "content": prompt[:1000]},
            {"role": "user", "content": text[:3000]}
        ]
        response = claude_client.chat.completions.create(
            model="databricks-claude-3-7-sonnet",
            messages=messages,
            temperature=0.5,
            max_tokens=400,
            timeout=10
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Analysis error: {str(e)}"
