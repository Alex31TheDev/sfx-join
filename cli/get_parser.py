import types
from copy import copy

import cli.info as info
from cli.args import args, prefix

from cli.customparser import CustomParser

def _parser_info():
    props = {}

    for prop_name in dir(info):
        if prop_name.startswith('__') and prop_name.endswith('__'):
            continue

        prop = getattr(info, prop_name)

        if not isinstance(prop, types.MethodType):
            props[prop_name] = prop

    props['prefix_chars'] = prefix
    
    return props

def _argument_info(argument):
    name = argument.get('name')

    dest = argument.get('dest') or name
    required = argument.get('required') or False
    positional = argument.get('positional') or False

    arg_list = {}

    if positional:
        pref_name = name
    else:
        pref_name = prefix + name

        arg_list['required'] = required
        arg_list['dest'] = dest

    arg_info = copy(argument)
    arg_info.update(arg_list)

    arg_info.pop('name', None)
    arg_info.pop('positional', None)

    return [pref_name, arg_info]

def _define_args(parser):
    for argument in args:
        name, info = _argument_info(argument)
        parser.add_argument(name, **info)

    return parser

def get_parser():
    parser = CustomParser(**_parser_info())
    _define_args(parser)

    return parser
