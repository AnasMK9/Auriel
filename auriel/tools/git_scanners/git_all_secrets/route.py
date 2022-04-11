from auriel.router import BaseRoute
from slack_bolt.context.say.say import Say
from auriel.block_builder import BlockBuilder


class GitAllSecretsRoute(BaseRoute):
    commands_channel = 'C03AVAK00LA'
    command = 'sudo docker run --rm -it abhartiya/tools_gitallsecrets'
    options: dict = {}
    task_name = 'git-all-secrets'
    
    def __init__(self, options: dict, telemetry_channel: str, say: Say = None):
        self.options.update(options)
        self.say = say
        self.telemetry_channel = telemetry_channel

    def run(self):
        self.build_command()
        self.send_response('executing')
        self.send_update('executing')
        self.send_update('success')

    def send_response(self, action):
        blocks = BlockBuilder.command_response_block(
            action=action, command=self.command)
        self.say(channel=self.commands_channel, blocks=blocks)

    def send_update(self, action):
        blocks = BlockBuilder.command_update_block(
            action=action, command=self.command, task_name=self.task_name)
        self.say(channel=self.telemetry_channel, blocks=blocks)
