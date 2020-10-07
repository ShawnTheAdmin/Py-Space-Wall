# Py-Space-Wall
A simple Python application that changes your Windows wallpaper every 20 minutes to the latest satellite image of earth. Inpsired by the Downlink app for Mac.

# Introduction

This application is intended to be ran via the executable but the source code can be found in ./src folder. Future builds will have the ability to manage scheduled task through the GUI but this does not exist currently.

These are some planned future improvements: 
* Build a GUI with Tkinter
* Automate scheduled task creation
* Add wallpaper options via JSON file

# Requirements

NOTE: These are packaged with the EXE, you only have to import these if you want to work with the source code.

The following pip packages are required to run the source code, version numbers used in project included:

    Requests

These are in use but packaged into Python by default:

    Shutil
    Ctypes
    OS

See the requirements.txt file to import them with pip: pip install -r requirements.txt

# Instructions

  1. Download project and extract contents. 
  2. Create a scheduled task on Windows with the frequency you want this to run, use the EXE in the scheduled task.
  
# Credit

This was written by me but largely inspired by the Downlink app for Mac (https://downlinkapp.com/). Many thanks to Anthony Colangelo for the inspiration! If you have a Mac check this out, it's awesome.

