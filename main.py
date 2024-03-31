from cli.get_parser import get_parser
from util.util import parse_order, get_paths
from sfx.sfx_util import get_sfx_list, merge_sfx, save_sfx

from defaults import *

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

    merge_order = parse_order(args.order)
    overlay = args.overlay

    sfx_paths = get_paths(files, sfx_dir, in_format)

    sfx_list = get_sfx_list(sfx_paths, in_format, remove_erroring, verbose)
    merged_sfx = merge_sfx(sfx_list, merge_order, overlay)

    save_sfx(merged_sfx, out_path, out_format)


if __name__ == '__main__':
    main()
