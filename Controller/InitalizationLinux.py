import Initialization
import os
import sys

class InitializationLinux(Initialization):
    def __init__(self):
        pass

    def enable_automatic_initialization(self):
        crontab_line = f'@reboot /usr/bin/python3 {os.path.abspath(sys.argv[0])}\n'
        os.system(f'(crontab -l ; echo "{crontab_line}") | crontab -')

    def disable_automatic_initialization(self):
        os.system('(crontab -l | grep -v "{}" ) | crontab -'.format(os.path.abspath(sys.argv[0])))