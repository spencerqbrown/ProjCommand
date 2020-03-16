# imports
import os
import sys
from git_operations import git_local

# constants
default_project_directory = "/Documents/Projects"
dpd_config_line = 1
default_project_name = "New_Project"
dpn_config_line = 3
default_ide = "code" # VSCode
di_config_line = 5
config_length = 6

# load configs if possible
try:
    with open("ProjCommand/config.ini") as f:
        # get config text as a list of strings
        config_text = f.readlines()
    project_directory = ""
    project_name = ""
    ide = ""
    if (len(config_text)) == config_length:
        print("TEMP")

except IOError:
    project_directory = default_project_directory
    project_name = default_project_name
    ide = default_ide
    print("IO Error happened")



# change directory
os.system("")

def app(ide, name):
    if (ide is None):
        ide = default_ide
    if (name is None):
        name = default_project_name
    if ('/' in name):
        dirs = name.split('/')
        for d in dirs:
            # TODO check if d exists, else mkdir
    # TODO enter target directory and make project
    git_local(name)
    # TODO open project
