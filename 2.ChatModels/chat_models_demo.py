from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.6)

res = model.invoke("3 Pickup lines that work")

print(res.content)