
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create chatbot
bot = ChatBot(
    "HariniBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///chatbot.sqlite3"
)

# Train chatbot with simple conversations
trainer = ListTrainer(bot)

trainer.train([
    "Hello",
    "Hi! Welcome to HariniBot.",
    "How are you?",
    "I am fine. Thank you!",
    "What is your name?",
    "My name is HariniBot.",
    "What can you do?",
    "I can answer simple questions.",
    "Bye",
    "Goodbye! Have a nice day!"
])

print("\n🤖 Welcome to HariniBot!")
print("Type 'exit' to stop the chatbot.\n")

while True:
    message = input("You: ").strip()

    if message.lower() == "exit":
        print("HariniBot: Goodbye!")
        break

    response = bot.get_response(message)
    print("HariniBot:", response)
