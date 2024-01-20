import openai
import os

def __init__():
    pass

def ask_question(messages):
    openai.api_key = os.environ['OPENAI_API_KEY']

    messages = [ {"role": "user", "content": message} for message in messages ]
    chat = openai.chat.completions.create( 
        model="gpt-3.5-turbo", messages=messages 
    ) 
        
    reply = chat.choices[0].message.content
    return reply
    