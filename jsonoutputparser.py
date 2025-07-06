from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_KEY')

model = ChatOpenAI(
    api_key=api_key,
    model='gpt-4o-mini'
    
)

parser = JsonOutputParser()

template = PromptTemplate(
    template= 'give me the name, age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({})

print(result)
