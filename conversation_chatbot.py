from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model("google_genai:gemini-2.5-flash-lite")

chat_history = [
    SystemMessage(content="You are a helpful AI assistant")
]

while True:
    user_input = input("User: ")
    chat_history.append(HumanMessage(content = user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content = result.content))
    print("AI: ", result.content)

print(chat_history)