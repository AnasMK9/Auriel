# from .config import Config


class BlockBuilder:
    actions = {"executing": "Executing",
               "success": "Success", "failure": "Failure"}

    @classmethod
    def command_response_block(cls, action: str, command: str):
        block = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{cls.actions.get(action)}*"
                }
            }, {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"```{command}```"
                }
            }]
        return block

    @classmethod
    def command_update_block(cls, action: str, command: str, task_name: str):
        block = cls.command_response_block(action, command)
        block.insert(0, {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": task_name,
            }
        })
        return block
