from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_KEY')

model = ChatOpenAI(
    api_key=api_key,
    model='gpt-4o-mini'
    
)

template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
) 

template2 = PromptTemplate(
    template='write a 5 line summary on the following text.\n {text}',
    input_variables=['text']
)

prompt1 = template1.format(topic='black hole')  # .format instead of .invoke
result = model.invoke(prompt1)

prompt2 = template2.format(text=result)
result1 = model.invoke(prompt2)

print(result)
print(result1)

