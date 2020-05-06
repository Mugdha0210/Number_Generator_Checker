
#send number to be drawn as argument, receive corresponding devanagari value stores in devauni
def obtaindeva(numtoprint):
    if (numtoprint == 0):
        devauni = u'\u0966'
    elif (numtoprint == 1):
        devauni = u'\u0967'
    elif (numtoprint == 2):
        devauni = u'\u0968'
    elif (numtoprint == 3):
        devauni = u'\u0969'
    elif (numtoprint == 4):
        devauni = u'\u0970'
    elif (numtoprint == 5):
        devauni = u'\u0971'
    elif (numtoprint == 6):
        devauni = u'\u0972'
    elif (numtoprint == 7):
        devauni = u'\u0973'
    elif (numtoprint == 8):
        devauni = u'\u0974'
    elif (numtoprint == 9):
        devauni = u'\u0975'
    print(devauni)

#will print the number in the terminal
#dont know where we have to print it on the display
