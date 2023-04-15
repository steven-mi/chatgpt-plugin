from enum import Enum
from typing import List, Dict

from pydantic import BaseModel, Field


class ChatRole(str, Enum):
    ASSISTANT = "assistant"
    USER = "user"
    SYSTEM = "system"


class ChatMessage(BaseModel):
    role: ChatRole
    message: str

    def openai_dict(self):
        return {"role": self.role, "content": self.message}

    class Config:
        use_enum_values = True


class MessageResponse(BaseModel):
    response_message: str = Field(..., description="Message to explain the user the result")
    response_code: int = Field(..., description="Response code of the message")


class PluginResponse(BaseModel):
    endpoint: str = Field(..., description="The endpoint that needs to be called without the URL")
    endpoint_params: Dict = Field(..., description="All endpoint parameters that needs to be set to call the endpoint")
    endpoint_body: Dict = Field(..., description="The endpoint request body that needs to be set to call the endpoint")
    message: List[MessageResponse] = Field(...,
                                           description="An message response object for each possible response code")