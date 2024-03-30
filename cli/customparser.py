import sys
import argparse

class CustomParser(argparse.ArgumentParser):
    def get_args(self):
        proc_args = sys.argv[1:]

        if len(proc_args) == 0:
            self.print_help()
            sys.exit(0)

        args = self.parse_args(proc_args)
        return args

    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()

        sys.exit(0)
