from cli.get_parser import get_parser
from util.util import parse_order, sfx_paths
from sfx.sfx_util import get_sfx_list, order_sfx, merge_sfx, save_sfx

from defaults import *

def main():
    parser = get_parser()
    args = parser.get_args()

    remove_erroring = args.remove_erroring
    verbose = args.verbose

    files = args.files
    sfx_dir = args.input
    count = args.count

    out_path = args.out or default_out
    out_format = args.format or default_out_format
    in_format = args.in_format or default_in_format

    merge_order = parse_order(args.order)
    overlay = args.overlay

    paths = sfx_paths(files, sfx_dir, in_format)
    paths = order_sfx(paths, merge_order, count)
    
    sfx_list = get_sfx_list(paths, in_format, remove_erroring, verbose)

    merged = merge_sfx(sfx_list, overlay)
    save_sfx(merged, out_path, out_format)


if __name__ == '__main__':
    main()
