from chatgpt_plugin.model import OpenAIModel
from chatgpt_plugin.schema import ChatMessage, ChatRole, PluginResponse
from chatgpt_plugin.utils import extract_json


def _create_system_message(openapi_specs) -> ChatMessage:
    system_message = f"""You are a smart assistant that is responsible to match an user request with our service.
    The service has following openapi specs: "{openapi_specs}".
    You will receive an user prompt and you will generate me an JSON object. The JSON object should have all properties defined in: {PluginResponse.schema()}. Only respond in JSON. 
    Translate messages to language of the user prompt.
    Write easy-to-understand messages towards an non-technical person.
    If the prompt doesn't match, ask the user to write an prompt that is related to our service. Provide an example to the user."""
    return ChatMessage(role=ChatRole.SYSTEM, message=system_message)


class ChatPlugin(object):

    def __init__(self, openapi_specs):
        self.chat_model = OpenAIModel()
        self.memory = [_create_system_message(openapi_specs)]

    def chat(self, message: str, retries: int = 2):
        if retries < 0:
            retries = 0

        chat_response = ""
        for _ in range(retries + 1):
            self.memory.append(ChatMessage(role=ChatRole.USER, message=message))
            chat_response = self.chat_model.get_chat_response(self.memory)
            plugin_message = extract_json(chat_response)
            if plugin_message is not None:
                self.memory.append(ChatMessage(role=ChatRole.ASSISTANT, message=chat_response))
                return PluginResponse(**plugin_message)

        return chat_response
