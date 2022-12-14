from typing import Dict

from revChatGPT.revChatGPT import Chatbot


class ChatGPT:
    """This class is a wrapper for the Chatbot class from revChatGPT."""

    def __init__(self):
        self.chatbot = Chatbot({})

    def get_response(
        self, message_prompt: str, conversation_id: str = None, parent_id: str = None
    ) -> str:
        response = self.chatbot.get_chat_response(
            message_prompt,
            output="text",
            conversation_id=conversation_id,
            parent_id=parent_id,
        )
        return response["message"]


if __name__ == "__main__":
    chatgpt = ChatGPT()
    print(chatgpt.get_response("Hello"))
