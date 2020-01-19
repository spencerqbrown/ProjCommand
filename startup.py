import sys
from .local_functions import check_language
from .local_functions import check_ide

language = None
project_name = None
ide = None

# add in checks that the number of arguments allows for below checks

if __name__ == "__main__":
    language_check = sys.argv[1]
    if (len(sys.argv) > 1):
        if (language_check == "l"):
            # checks if language is valid
            if (len(sys.argv) > 2 and check_language(sys.argv[2])):
                language = sys.argv[2]
            else:
                raise ValueError
        elif (language_check == "i"):
            if (len(sys.argv) > 2 and check_ide(sys.argv[2])):
                ide = sys.argv[2]
            else:
                raise ValueError
        elif (language_check == "n"):
            if (len(sys.argv) > 2):
                project_name = sys.argv[2]
            else:
                raise ValueError
    elif (len(sys.argv) > 2 and sys.argv == "i"):
        # checks if ide is valid
        if (len(sys.argv) > 3 and check_ide(sys.argv[4])):
            ide = sys.argv
        else:
            raise ValueError

    