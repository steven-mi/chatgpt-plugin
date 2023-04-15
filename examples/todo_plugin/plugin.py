import fire

from chatgpt_plugin.plugin import ChatPlugin


def chat(text):
    with open("openapi.json") as f:
        openapi_specs = f.read()

    todo_plugin = ChatPlugin(openapi_specs=openapi_specs)
    return todo_plugin.chat(message=text)


if __name__ == '__main__':
    fire.Fire(chat)
