import sys
from .app import application

def check_name(directory):
    # TODO
    return None

def navigate(project_name):
    # TODO
    return None

def setup_directory(project_name, ide):
    # TODO
    return None

def setup_repo(project_name):
    # TODO
    return None

def open_project(project_name, ide):
    # TODO
    return None

def check_ide(ide):
    # TODO
    return True

project_name = None
ide = None

# add in checks that the number of arguments allows for below checks

if __name__ == "__main__":

    args = sys.argv
    nargs = len(args)
    if (nargs == 5): # ide and name are present
        if ((args[1] != 'i') or (args[3] != 'n')): # incorrect commands for ide or name
            raise ValueError
        if ((not check_ide(args[2])) or (not check_name(args[4]))): # invalid ide or name, maybe separate later
            raise ValueError
        app(args[2], args[4])
    elif (nargs == 3): # either only ide or only name present
        if ((args[1] == 'i') and (check_ide(agrs[2]))): # ide is present and valid
            app(args[2], None)
        elif ((args[1] == 'n') and (check_name(args[2]))): # name is present and valid
            app(None, args[2])
        else:
            raise ValueError
    else:
        app(None, None)