from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

import random
from functools import reduce

import os
from os import path

from sfx.ordermode import OrderMode
from util.util import error

default_crossfade = 200

def _load_sfx(sfx_path, format, remove_erroring=False, verbose=False):
    err_out = ''

    try:
        return (AudioSegment.from_file(sfx_path, format), err_out)
    except CouldntDecodeError as err:
        if verbose:
            out = str(err)
        else:
            split = str(err).split('\n')
            out = split[0]

        err_out += f'{out} \'{sfx_path}\''
    except Exception as err:
        msg = str(err)

        if 'No such file or directory' in msg:
            msg = f'File not found: \'{sfx_path}\''
        
        err_out += msg

    print(f'decode error: {err_out}')

    if remove_erroring:
        os.remove(sfx_path)
        print(f'removed: {sfx_path}')

    return None

def get_sfx_list(sfx_paths, format, remove_erroring=False, verbose=False):
    sfx_list = []

    for sfx_path in sfx_paths:
        sfx = _load_sfx(sfx_path, format, remove_erroring, verbose)

        if sfx == None:
            continue

        sfx_name = path.splitext(sfx_path)

        data = (sfx_name, sfx)
        sfx_list.append(data)

    return sfx_list

def _sfx_total_duration(sfx_list):
    sfx_durations = [sfx.duration_seconds * 1000 for sfx in sfx_list]
    total_duration = reduce(lambda a, b: a+b, sfx_durations)

    return total_duration

def _simple_merge(sfx_list, crossfade=default_crossfade):
    merged_sfx = sfx_list[0]
    sfx_list = sfx_list[1:]

    for sfx in sfx_list[1:]:
        merged_sfx = merged_sfx.append(sfx, crossfade=crossfade)

    return merged_sfx

def _simple_overlay(sfx_list, offset):
    position = 0

    overlayed_sfx = sfx_list[0]
    sfx_list = sfx_list[1:]

    additional_duration = _sfx_total_duration(sfx_list)
    silence = AudioSegment.silent(duration=additional_duration)
    overlayed_sfx = overlayed_sfx + silence

    for sfx in sfx_list:
        overlayed_sfx = overlayed_sfx.overlay(sfx, position=position)
        position += offset

    a = overlayed_sfx.duration_seconds
    return overlayed_sfx

def _overlay_merge(sfx_list):
    merge_list = sfx_list[1::2]
    overlay_list = sfx_list[::2]

    total_duration = _sfx_total_duration(sfx_list)
    overlay_offset = total_duration / len(sfx_list)

    merged_sfx = _simple_merge(merge_list)
    overlayed_sfx = _simple_overlay(overlay_list, overlay_offset)

    result_sfx = merged_sfx.overlay(overlayed_sfx, overlay_offset / 2)
    return result_sfx

def _order_sfx(sfx_list, order):
    if order == OrderMode.SORTED:
        sfx_list.sort(key=lambda tup: tup[0])
    elif order == OrderMode.RANDOM:
        random.shuffle(sfx_list)

def merge_sfx(sfx_list, order=OrderMode.DEFAULT, overlay=False):
    _order_sfx(sfx_list, order)
    sfx_list = [sfx[1] for sfx in sfx_list]
    
    if overlay:
        result_sfx = _overlay_merge(sfx_list)
    else:
        result_sfx = _simple_merge(sfx_list)

    return result_sfx

def save_sfx(sfx, filename, format):
    file_path = path.abspath(filename)

    try:
        sfx.export(file_path, format)
    except Exception as err:
        error(err)

    print(f'Created {format} file: {file_path}')
