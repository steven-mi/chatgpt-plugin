from chatgpt_plugin.plugin import ChatPlugin

with open("openapi.json") as f:
    openapi_specs = f.read()

plugin = ChatPlugin(openapi_specs=openapi_specs)

messages = ["What are good headphones for 150 Euro?",
            "What about monitors for the same budget?"]
for msg in messages:
    print(msg)
    chat_response = plugin.chat(message=msg)
    print(chat_response)
