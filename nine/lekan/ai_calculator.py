from chatterbot import ChatBot

Bot = ChatBot(name='Calculator',
              read_only=True,
              logic_adapters=["chatterbot.logic.MathematicalEvaluation"],
              storage_adapters="chatterbot.storage.SQLStorageAdapter")

print('\033c')
print("Hello, I am a calculator. How may I help you?")
while(True):
    user_input = input("me: ")

    if user_input.lower() == 'quit':
        print("Exiting")
        break
