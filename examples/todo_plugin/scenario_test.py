from chatgpt_plugin.plugin import ChatPlugin

with open("openapi.json") as f:
    openapi_specs = f.read()

todo_plugin = ChatPlugin(openapi_specs=openapi_specs)
chat_response = todo_plugin.chat(message="Add buying frozen pizza as an todo")
print(chat_response)