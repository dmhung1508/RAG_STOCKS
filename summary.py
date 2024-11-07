from openai import OpenAI
import config
client = OpenAI(
    base_url='http://localhost:11434/v1/',

    # required but ignored
    api_key='ollama',
)

def summary_text(text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",

                "content": config.prompt_summary
            },
            {
                'role': 'user',
                'content': text
            }
        ],
        temperature=0,
        max_tokens = 2024,
        
        #request_timeout=config.REQUEST_TIMEOUT,
        model='llama3.2',
    )
    keyword = chat_completion.choices[0].message.content
    return keyword