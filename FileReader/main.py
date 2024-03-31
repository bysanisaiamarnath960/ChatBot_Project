import os
from secret_key import openai_key
from langchain.llms import OpenAI
os.environ['OPENAI_API_KEY']=openai_key

llm=OpenAI(temperature=0.6)
name=llm("I want to open a Restaurant for Indian Food. Suggest a Fancy name for this.")
print(name)


