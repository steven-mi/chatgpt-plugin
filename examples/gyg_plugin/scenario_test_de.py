from chatgpt_plugin.plugin import ChatPlugin

with open("openapi.json") as f:
    openapi_specs = f.read()

plugin = ChatPlugin(openapi_specs=openapi_specs)
print(plugin.chat(message="Was kann ich in Berlin machen"))
print(len(plugin.memory))
print(plugin.chat(message="Gibt es irgendwelche Museen?"))
print(len(plugin.memory))
