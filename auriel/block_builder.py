from .config import Config


class BlockBuilder:
    actions = {"executing": "Executing",
               "success": "Success", "failure": "Failure"}

    @classmethod
    def command_response_block(cls, action: str, command: str):
        block = [
            {
                "type": "section",
                "fields": [{
                    "type": "mrkdwn",
                    "text": "*"+cls.actions.get(action)+"*"
                }]
            }, {
                "type": "section",
                "fields": {
                    "type": "mrkdwn",
                    "text": "```"+command+"```"
                }
            }]
        return block

    @classmethod
    def command_update_block(cls, action: str, command: str):
        block = cls.command_response_block(action, command)
        block[0]['text'].insert(0, {
            "type": "header",
            "text": Config.CLONE_NAME
        })
        return block
