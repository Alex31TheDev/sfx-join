prefix = '-'

args = [
    {
        'name': 'files',
        'metavar': 'input',
        'nargs': '*',
        'positional': True,
        'help': 'Input file list'
    },
    {
        'name': 'i',
        'dest': 'input',
        'help': 'Input directory'
    },
    {
        'name': 'o',
        'dest': 'out',
        'help': 'Output filename'
    },
    {
        'name': 'f',
        'dest': 'format',
        'help': 'Output format'
    },
    {
        'name': 'if',
        'dest': 'in_format',
        'help': 'Input format'
    },
    {  
        'name': 'order',
        'help': 'Merge order'
    },
    {
        'name': 'overlay',
        'action': 'store_true',
        'help': 'Overlay sound effects'
    },
    {
        'name': 'remove',
        'dest': 'remove_erroring',
        'action': 'store_true',
        'help': 'Remove erroring files'
    },
    {
        'name': 'verbose',
        'action': 'store_true',
        'help': 'Show verbose ffmpeg errors'
    }
]
