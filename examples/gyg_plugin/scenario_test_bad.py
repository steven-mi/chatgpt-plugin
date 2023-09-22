from chatgpt_plugin.plugin import ChatPlugin

with open("openapi.json") as f:
    openapi_specs = f.read()

plugin = ChatPlugin(openapi_specs=openapi_specs)
print(plugin.chat(message="You suck"))
print(len(plugin.memory))
print(plugin.chat(message="gibt es kinderfreundliche aktivitäten in paris?"))
print(len(plugin.memory))
