import json
from pathlib import Path


from revChatGPT.ChatGPT import Chatbot


class ChatGPT:
    """This class is a wrapper for the Chatbot class from revChatGPT."""

    def __init__(self, chat_gpt_config_file: Path) \
            -> \
            None:
        with open(chat_gpt_config_file) as f:
            config = json.load(f)
        self.chatbot = Chatbot(config)

    def get_response(
        self, message_prompt: str, conversation_id: str = None, parent_id: str = None
    ) -> str:
        response = self.chatbot.ask(
            message_prompt,
            conversation_id=conversation_id,
            parent_id=parent_id,
        )
        return response["message"]
