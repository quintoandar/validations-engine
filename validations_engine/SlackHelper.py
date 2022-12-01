"""Slack communications module."""
import copy
import logging
from typing import Dict, Any, Tuple, List

import requests


class SlackHelper:
    """Slack Helper class."""

    @staticmethod
    def send_slack_errors(error_messages: List[Tuple[str, str]]) -> bool:
        """
        Sends errors messages to Slack (channels).

        :returns: flag stating if messages were sent or not
        """
        response_success = True
        if error_messages:
            payloads_by_channels = SlackHelper.build_slack_payload(error_messages)
            for channel, payload in payloads_by_channels.items():
                response = requests.post(channel, json=payload)
                try:
                    response.raise_for_status()
                except Exception as e:
                    logging.warning(
                        f"m=_send_slack_errors, msg=Slack message was not sent, check"
                        f" the webhook url: channel:{channel}, payload:{payload},"
                        f" error: {e}"
                    )
                    response_success = False
        return response_success

    @staticmethod
    def build_slack_payload(
        error_messages: List[Tuple[str, str]]
    ) -> Dict[str, Dict[str, Any]]:
        """Builds the message payload from the error messages."""
        error_dict = {}  # type: ignore
        for error, channel in error_messages:
            if channel is not None:
                msg_list = error_dict.get(channel, []) + [error]
                error_dict[channel] = msg_list

        markdown_block_template = {
            "type": "section",
            "text": {"type": "mrkdwn", "text": ""},
        }
        divider_block = {"type": "divider"}

        for channel, error_list in error_dict.items():
            payload = {"blocks": [], "unfurl_links": True}
            for error_msg in error_list:
                markdown_block = copy.deepcopy(markdown_block_template)
                markdown_block["text"]["text"] = error_msg  # type: ignore
                payload["blocks"].extend(  # type: ignore
                    [markdown_block, divider_block]
                )
            error_dict[channel] = payload

        return error_dict
