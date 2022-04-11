from ..router import BaseRoute

class ReconFTWRoute(BaseRoute):
    def __init__(self, telemetry_channel, commands_channel, task_name, command, options):
        super().__init__(telemetry_channel, commands_channel, task_name, command, options)


    def send_message(self, channel, message):
        raise NotImplementedError

    def match(self, path):
        raise NotImplementedError