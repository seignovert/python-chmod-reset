# -*- coding: utf-8 -*-
import os

CHMOD_FILE = 0o644 # rw-r--r--
CHMOD_DIR =  0o755 # rwxr-xr-x

def scan(name, verbose=True):
    if os.path.isfile(name):
        if verbose:
            print('F > {}'.format(name))
        os.chmod(name, CHMOD_FILE)
    elif os.path.isdir(name):
        if verbose:
            print('D > {}'.format(name))
        os.chmod(name, CHMOD_DIR)
        for sub in os.listdir(name):
            scan(os.path.join(name,sub))
    elif os.path.islink(name):
        if verbose:
            print('L > {}'.format(name))
    else:
        raise ValueError('`{}` is neither a file nor a directory'.format(name))

if __name__ == '__main__':
    import sys

    name = '.' if len(sys.argv) <= 1 else sys.argv[1]

    scan(name)
