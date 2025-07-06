from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
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

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)