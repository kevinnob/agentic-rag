from langchainhub import Client
from langchain_core.load import loads
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)
hub = Client()
prompt = loads(hub.pull("rlm/rag-prompt"))

generation_chain = prompt | llm | StrOutputParser()