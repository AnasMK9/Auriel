
def command_builder(executable: str, **options: dict):
    cmd = executable+''.join(' --'+key+' '+str(value)
                             for key, value in options.items())
    cmd = cmd.replace('None', '')
    return cmd


def decode_message(message: str):
    args = message.strip().split(' ')
    arglist = [tuple(arg.strip('-').split(':', maxsplit=1)) for arg in args]
    dict_args = {}
    for arg in arglist:
        if len(arg) == 2:
            dict_args[arg[0]] = arg[1]
        else:
            dict_args[arg[0]] = None
    return dict_args

