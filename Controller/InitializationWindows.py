import Initialization
import os
import sys

class InitializationWindows(Initialization):
    def __init__(self):
        pass

    def enable_automatic_initialization(self):
        startup_folder = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
        script_path = os.path.abspath(sys.argv[0])
        shortcut_path = os.path.join(startup_folder, "meuscript.lnk")

        with open(shortcut_path, "w") as shortcut:
            shortcut.write(f"@echo off\npython {script_path}")

    def disable_automatic_initialization(self):
        startup_folder = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
        shortcut_path = os.path.join(startup_folder, "meuscript.lnk")
        os.remove(shortcut_path)