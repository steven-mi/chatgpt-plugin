# ChatGPT Plugin

The ChatGPT Plugin simplifies chatbot creation by reverse engineering OpenAI's ChatGPT project. To build your own
LLM chatbot, **all you need is an OpenAPI specification**. LLM chatbots offer powerful features out of the box such as:

- Responds and understand multiple languages
- Able to generate responses by utilising past messages
- Good understanding of user intentions
- ...

## Getting Started

```bash
pip install chatgpt-plugin
```

### How does it work

The framework generates for you an JSON that contains:

- The endpoint that needs to be called
- The endpoint body & params that needs to be passed to fulfill the users wish
- A response message for each documented case

For the case of an **TODO app**:

```python
from chatgpt_plugin.plugin import ChatPlugin

with open("todo_openapi.json") as f:
    openapi_specs = f.read()

todo_plugin = ChatPlugin(openapi_specs=openapi_specs)
todo_plugin.chat(message="Add buying frozen pizza as an todo")
```

The plugin framework will generate following python object:

```
endpoint='/todos/' 
endpoint_params={} 
endpoint_body={'title': 'Buy frozen pizza', 'description': 'Remember to buy frozen pizza', 'completed': False} 
message=[MessageResponse(response_message='Todo created successfully', response_code=200), 
         MessageResponse(response_message='Validation Error', response_code=422)]
```

### Examples

You can find more examples under the `examples` folder.

## Tips and Tricks

Here are some recommendations to make full use of this framework.

- Add a description to your query parameter to make the usage more clear
- Make the language specific e.g. if your query parameter only accept English then specify it in the description
- Add all possible responses. If your API can fail for a reason, document it.

## Licenses

Apache License Version 2.0, see [LICENSE](LICENSE)
