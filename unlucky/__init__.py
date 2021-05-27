import os
import __main__

def cli():
    print("__main__ is: ", __main__)
    print("Does a file exist at __main__? ", os.path.exists(__main__.__file__))
