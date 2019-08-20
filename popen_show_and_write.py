import subprocess
import sys
'''
import os
import shutil
import re
from distutils.dir_util import copy_tree
'''

def run():
    '''
    run
    :return: output
    '''
    output = []
    strt = "MY_COMMAND_LINE_COMMAND"
    process = subprocess.Popen(strt, cwd=".",
                               stdout=subprocess.PIPE, shell=True)  
    for line in iter(process.stdout.readline, b''):
        l = line.decode('utf-8')
        sys.stdout.write(l)
        output.append(l.rstrip())

    return output

if __name__ == "__main__":
    a = run()
