from http.server import executable
from .config import Config
from slack_bolt import App
from .functions import *


app = App(token=Config.SLACK_BOT_TOKEN,
          signing_secret=Config.SLACK_SIGNING_SECRET)

# //TODO: execute the command and send updates to output
# import subprocess
# process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
# process.wait()
# print process.returncode


@app.event("app_mention")  # that's how the app will recieve commands
def recieve_command(event, say):  # , say):
    command_options = decode_message(
        event['blocks'][0]['elements'][0]['elements'][1]['text'])
    executable = 'sudo docker run --rm -it abhartiya/tools_gitallsecrets'
    command = command_builder(executable, **command_options)
    response = 'executing: ' + "```" + command + "```"
    say(text='*_'+Config.CLONE_NAME+'_*\\n'+response,
        channel=Config.SLACK_COMMANDS_CHANNEL)
    say(text=response, channel=Config.SLACK_TELEMETRY_CHANNEL)


if __name__ == '__main__':
    app.start(port=Config.PORT)
    # message = {'token': 'mirwmsEjdkEoaaXfTbatU0qd', 'team_id': 'T03B7U1JK7B', 'api_app_id': 'A03AEPHQ1GF', 'event': {'client_msg_id': '2df7c978-658c-4b58-8a70-2fa2c9a49f17', 'type': 'app_mention', 'text': '<@U03AEPJ8LP9> -org:shein -cloneForks', 'user': 'U03AVA83V0T', 'ts': '1649542287.794229', 'team': 'T03B7U1JK7B', 'blocks': [{'type': 'rich_text', 'block_id': '2CR3', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'user', 'user_id': 'U03AEPJ8LP9'}, {'type': 'text', 'text': ' -org:shein -cloneForks'}]}]}], 'channel': 'C03AVAK00LA', 'event_ts': '1649542287.794229'}, 'type': 'event_callback', 'event_id': 'Ev03ASJ6NQ13', 'event_time': 1649542287, 'authorizations': [{'enterprise_id': None, 'team_id': 'T03B7U1JK7B', 'user_id': 'U03AEPJ8LP9', 'is_bot': True, 'is_enterprise_install': False}], 'is_ext_shared_channel': False, 'event_context': '4-eyJldCI6ImFwcF9tZW50aW9uIiwidGlkIjoiVDAzQjdVMUpLN0IiLCJhaWQiOiJBMDNBRVBIUTFHRiIsImNpZCI6IkMwM0FWQUswMExBIn0'}
    # event = {
    #     "client_msg_id": "1949CA5E-29D7-44F3-916E-9DE2856C44ED",
    #     "type": "app_mention",
    #     "text": "<@U03AEPJ8LP9> -org:shein -cloneForks",
    #     "user": "U03AVA83V0T",
    #     "ts": "1649542590.206229",
    #     "team": "T03B7U1JK7B",
    #     "blocks": [
    #         {
    #             "type": "rich_text",
    #             "block_id": "Gegpv",
    #             "elements": [
    #                 {
    #                     "type": "rich_text_section",
    #                     "elements": [
    #                         {"type": "user", "user_id": "U03AEPJ8LP9"},
    #                         {"type": "text", "text": " -org:shein -cloneForks"},
    #                     ],
    #                 }
    #             ],
    #         }
    #     ],
    #     "channel": "C03AVAK00LA",
    #     "event_ts": "1649542590.206229",
    # }
    # recieve_command(event, print)
