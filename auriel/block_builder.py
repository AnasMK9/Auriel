from .config import Config


class BlockBuilder:
    actions = {"executing": "Executing",
               "success": "Success", "failure": "Failure"}

    @classmethod
    def command_response_block(cls, action: str, command: str):
        block = {"blocks": [
            {
                "type": "section",
                        "text": [{
                            "type": "mrkdwn",
                            "text": "*"+cls.actions.get(action)+"*"
                        }]
            }, {
                "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "```"+command+"```"
                        }
            }]}
        return block

    @classmethod
    def command_update_block(cls, action: str, command: str):
        block = cls.command_response_block(action, command)
        block['blocks'][0]['text'].insert(0, {
            "type": "mrkdwn",
            "text": "*_"+Config.CLONE_NAME+"_*"
        })
        return block
