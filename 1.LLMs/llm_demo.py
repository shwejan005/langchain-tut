from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

res = llm.invoke("Write a poem about the sea.")
print(res.content)