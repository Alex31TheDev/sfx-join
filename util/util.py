import sys
from os import path

import shutil
from pydub import AudioSegment

from defaults import *
from sfx.ordermode import OrderMode

from util.file_util import create_dir
from util.file_util import get_paths

def error(msg):
    print('error: ' + str(msg))
    sys.exit(0)

def parse_order(merge_order):
    if merge_order is None:
        return default_merge_order
    
    merge_order = merge_order.lower()
    
    try:
        merge_order = OrderMode(merge_order)
    except ValueError:
        error('Invalid ordering mode: ' + merge_order)

    return merge_order

def sfx_paths(files, sfx_dir, in_format):
    sfx_paths = []

    if files is not None:
        sfx_paths = [path.abspath(file_path) for file_path in files]

    if sfx_dir is not None:
        try:
            sfx_paths = get_paths(sfx_dir, in_format)
        except FileNotFoundError:
            create_dir(sfx_dir)
            error('Input directory not found. Directory created.')

    if len(sfx_paths) == 0:
        error('No valid input files provided.')

    return sfx_paths

def check_ffmpeg():
    pydub_ffmpeg_path = AudioSegment.converter
    ffmpeg_path = shutil.which(pydub_ffmpeg_path)

    if ffmpeg_path is None:
        error(f"ffmpeg not found at path: {pydub_ffmpeg_path}")

    return ffmpeg_path

def set_ffmpeg(ffmpeg_path):
    if ffmpeg_path is not None:
        AudioSegment.converter = ffmpeg_path
