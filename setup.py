from cx_Freeze import setup, Executable
import sys
import os

# Add any necessary includes and excludes here
build_exe_options = {
    "packages": ["os", "shutil", "time", "tkinter", "hashlib"],
    "excludes": [],
}

# Base="Win32GUI" is used only for Windows GUI applications
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "CarlosAutouploader",
    version = "1.0",
    description = "A directory copy utility",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base=base, icon="carlos.ico")]  # Change "carlos.ico" to your icon file
)