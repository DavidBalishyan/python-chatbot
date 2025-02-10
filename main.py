from langchain_ollama import OllamaLLM


question = input(">>>")

model = OllamaLLM(model="llama3.2")
result = model.invoke(input=question)

print(f"qusetion: {question}")
print(f"answer: {result}")
