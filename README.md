# sfx-merge

Merge multiple audio files into a single file

# Usage

Run `python main.py --help` to view the command line help:

    usage: main.py [-h] [-i INPUT] [-o OUT] [-f FORMAT] [-if IN_FORMAT] [-order ORDER] [-overlay] [-remove] [-verbose] [input ...]

    Sound effect combiner

    positional arguments:
      input          Input file list

    options:
      -h, --help     show this help message and exit
      -i INPUT       Input directory
      -o OUT         Output filename
      -f FORMAT      Output format
      -if IN_FORMAT  Input format
      -order ORDER   Merge order
      -overlay       Overlay sound effects
      -remove        Remove erroring files
      -verbose       Show verbose ffmpeg errors

# Input

You can specify the input as a list of filenames, e.g.

    $ python main.py a.mp3 b.mp3 c.mp3

Or you can specify an entire directory of files to merge, e.g.

    $ python main.py -input /path/to/directory

The `if` argument also determines the extension of the files that are taken from a directory.

# Ordering modes

-   default: Default filesystem order
-   sorted: Alphabetical sorting by filename
-   random: Random shuffle
