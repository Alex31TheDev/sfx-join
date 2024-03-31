import os
from os import path

def _valid_file(file_path, extension):
    if not path.isfile(file_path):
        return False

    if extension == '.':
        return True

    _, file_ext = path.splitext(file_path)

    return file_ext == extension


def _valid_directory(dir_path):
    if not path.isdir(dir_path):
        return False
    
    dir_name, _ = path.splitext(dir_path)

    if dir_name.startswith('.'):
        return False
        
    if dir_name.startswith('__') and dir_name.endswith('__'):
        return False
    
    return True


def _rec_get(cur_path, extension, paths):
    items = os.listdir(cur_path)

    for item in items:
        itm_path = path.join(cur_path, item)

        if _valid_file(itm_path, extension):
            paths.append(itm_path)
        elif _valid_directory(itm_path):
            _rec_get(itm_path, extension, paths)

    return paths

def get_paths(dir_path, extension=None):
    if extension is None:
        extension = '.'
    else:
        extension = '.' + extension

    dir_path = path.abspath(dir_path)

    return _rec_get(dir_path, extension, [])

def create_dir(dir_path):
    if path.isdir(dir_path):
        return
    
    os.mkdir(dir_path)
