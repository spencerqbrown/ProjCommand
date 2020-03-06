import sys

def check_for_directory(directory):
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

    nargs = len(sys.argv)
    if nargs > 1:
        switch (sys.argv[1]):
            case ('i'):
                
            case ('n'):
    else:
        # TODO use default ide, name, directory
    
    


    # after checks
    navigate(project_name)
    setup_directory(project_name, ide)
    setup_repo(project_name)
    open_project(project_name, ide)