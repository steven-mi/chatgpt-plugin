import os
from typing import List

import openai

from chatgpt_plugin.schema import ChatMessage


class OpenAIModel(object):

    def __init__(self):
        token = os.environ.get("OPENAI_TOKEN", None)
        if token is None:
            raise Exception("OPENAI_TOKEN is not set.")
        openai.api_key = token

    def get_chat_response(self, message_history: List[ChatMessage]) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[msg.openai_dict() for msg in message_history],
            temperature=0
        ).to_dict_recursive()["choices"][0]["message"]["content"]
        return response
