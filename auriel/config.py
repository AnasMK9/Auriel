from os import environ


class Config:
    SLACK_SIGNING_SECRET = environ.get('SLACK_SIGNING_SECRET')
    SLACK_BOT_TOKEN = environ.get('SLACK_BOT_TOKEN')
    PORT = 3000
    SLACK_COMMANDS_CHANNEL = 'C03AVAK00LA'
    SLACK_TELEMETRY_CHANNEL = 'C03AXMGQPEY'
    CLONE_NAME = 'git-all-secrets'
