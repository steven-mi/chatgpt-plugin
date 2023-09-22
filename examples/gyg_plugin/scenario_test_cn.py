from chatgpt_plugin.plugin import ChatPlugin

with open("openapi.json") as f:
    openapi_specs = f.read()

plugin = ChatPlugin(openapi_specs=openapi_specs)
print(plugin.chat(message="我在柏林能做什么"))
print(len(plugin.memory))
print(plugin.chat(message="是否有任何博物馆"))
print(len(plugin.memory))
