# Main
import sys

sys.path.append()
# from Modules import *
# import Modules as mod

from Modules import find_index as fi, test

courses = ['History', 'Math', 'Physics', 'CompSci']
# index = Modules.find_index(courses, 'CompSci')
# index = mod.find_index(courses, 'CompSci')
index = fi(courses, 'CompSci')
print(index)
print(test)
print(sys.path)

# when module is at another location
# import sys
# sys.path.append('location address')

# changing the environment variable
# on mac
# goto terminal
# we can set by adding them to ._profile file in our home directory and you can edit this file with any text editor
# but here we are going to use built into th terminal here called nano since nano is easy for anyone to use

# $ nano ~/.bash_profile .....then press enter
# you will see alias python=python3 at the end of the terminal

# we are going to set this by saying export as

# export PYTHONPATH="Location address"
# to save this press ctrl+X and then Y to save and then enter to keep the same file name
# restart the terminal

# to set this environmental variable on windows
# right click on computer andnd go to properties then advance system settings
# and from here at the very bottom we can click on environment variables and now we can create new environmental variable
# click new and we'll name this python path all uppercase and then for the location that's going to be then add click ok ok tghen close
# check this by opening command prompt
# to import our module say import my_module
# import sys and sys.path we can see that the directory that we added to python path is the second one

# sys.path allows us to import modules directly from the standard library