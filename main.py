from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3.2")

result = model.invoke(input="Hello World")

print(result)