# from .config import Config
from http.server import executable
from .block_builder import BlockBuilder
from slack_bolt.context.say.say import Say

'''
1- recv command
2- resolve channel -> class
3- decode options
4- pass options to class
5- execute command
'''


class BaseRoute:
    telemetry_channel: str  # = Config.SLACK_TELEMETRY_CHANNEL
    commands_channel: str
    task_name: str
    command: str
    options: dict
    say: Say
    executable: str
    actions = {"executing": "Executing",
               "success": "Success", "failure": "Failure"}

    def build_command(self):
        self.executable = self.command+''.join(' --'+key+' '+str(value)
                                   for key, value in self.options.items())
        self.executable.replace('None', '')

    def send_response(self, action):
        raise NotImplementedError

    def send_update(self, action):
        raise NotImplementedError

    def run(self, path):
        raise NotImplementedError


class EventRouter:
    """Given a channel and message, find the appropriate map the channel to the class appropriate class and execute container with the given options."""

    routes: dict = {}
    telemetry_channel: str

    def __init__(self, routes, telemetry_channel):
        self.routes = routes
        self.telemetry_channel = telemetry_channel

    def add_routes(self, route):
        "takes one or multiple routes as long as its a dict"
        self.routes.update(route)

    def resolve(self, event, say) -> BaseRoute:
        dest = self.routes.get(event['channel'])
        message = event['blocks'][0]['elements'][0]['elements'][1]['text']
        command_options = self.get_options(message)
        return dest(options = command_options, telemetry_channel=self.telemetry_channel, say=say)

    def get_options(self, message: str):

        args = message.strip().split(' ')
        arglist = [tuple(arg.strip('-').split(':', maxsplit=1))
                   for arg in args]
        dict_args = {}
        for arg in arglist:
            if len(arg) == 2:
                dict_args[arg[0]] = arg[1]
            else:
                dict_args[arg[0]] = None
        return dict_args
