'''This is the main python file that will run the system '''

#importing modules
import os, sys
from core import system

def startApplication():

    ''' This function starts the application '''

    arguments = sys.argv
    try:
        if arguments[1] == 'start' or arguments[1] =='run':
            system.window()
    
    except Exception as e:
        print("Error Occured")

startApplication()