from os import path

from cli.get_parser import get_parser

from util.util import error
from util.file_util import get_paths, create_dir

from sfx.ordermode import OrderMode
from sfx.sfx_util import get_sfx_list, merge_sfx, save_sfx

from defaults import *

def parseOrder(merge_order):
    if merge_order == None:
        return default_merge_order
    
    merge_order = merge_order.lower()
    
    try:
        merge_order = OrderMode(merge_order)
    except ValueError:
        error('Invalid ordering mode: ' + merge_order)

    return merge_order

def getPaths(files, sfx_dir, in_format):
    sfx_paths = []

    if files != None:
        sfx_paths = [path.abspath(file_path) for file_path in files]

    if sfx_dir != None:
        try:
            sfx_paths = get_paths(sfx_dir, in_format)
        except FileNotFoundError:
            create_dir(sfx_dir)
            error('Input directory not found. Directory created.')

    if len(sfx_paths) == 0:
        error('No valid input files provided.')

    return sfx_paths

def main():
    parser = get_parser()
    args = parser.get_args()

    remove_erroring = args.remove_erroring
    verbose = args.verbose

    files = args.files
    sfx_dir = args.input

    out_path = args.out or default_out
    out_format = args.format or default_out_format
    in_format = args.in_format or default_in_format

    merge_order = parseOrder(args.order)
    overlay = args.overlay

    sfx_paths = getPaths(files, sfx_dir, in_format)

    sfx_list = get_sfx_list(sfx_paths, in_format, remove_erroring, verbose)
    merged_sfx = merge_sfx(sfx_list, merge_order, overlay)

    save_sfx(merged_sfx, out_path, out_format)


if __name__ == '__main__':
    main()
