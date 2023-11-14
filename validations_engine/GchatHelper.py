"""Gchat communications module."""
from typing import List
import requests
import logging

from validations_engine.message import Message


class GchatHelper:
    """Gchat Helper class."""

    @staticmethod
    def send_message(message: Message) -> bool:
        """
        Sends a message to a GChat webhook.

        :returns: flag stating if messages were sent or not
        """
        if message.destination is not None:
            payload = {"text": message.content}
            response = requests.post(message.destination, json=payload)
            try:
                response.raise_for_status()
            except Exception as e:
                logging.warning(
                    "m=send_message, msg=Gchat message was not sent, check"
                    f" the webhook url: {message.destination}, payload:{payload},"
                    f" error: {e}"
                )
                return False
            return True

        logging.warning(
            "m=send_message, msg=Gchat message was not sent. "
            "The destination is empty!"
        )
        return False

    @staticmethod
    def send_messages(messages: List[Message]) -> bool:
        """
        Sends a list of messages to a GChat webhook.

        :returns: flag stating if messages were sent successfully or not.
        """
        all_success = all([GchatHelper.send_message(message) for message in messages])
        return all_success
