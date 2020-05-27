
#send number to be drawn as argument, receive corresponding devanagari value stores in devauni
def obtaindeva(numtoprint):
    if (numtoprint == 0):
        devauni = b'\u0966'
        numName = "\nzero"
    elif (numtoprint == 1):
        devauni = b'\u0967'
        numName = "\none"
    elif (numtoprint == 2):
        devauni = b'\u0968'
        numName = "\ntwo"
    elif (numtoprint == 3):
        devauni = b'\u0969'
        numName = "\nthree"
    elif (numtoprint == 4):
        devauni = b'\u096A'
        numName = "\nfour"
    elif (numtoprint == 5):
        devauni = b'\u096B'
        numName = "\nfive"
    elif (numtoprint == 6):
        devauni = b'\u096C'
        numName = "\nsix"
    elif (numtoprint == 7):
        devauni = b'\u096D'
        numName = "\nseven"
    elif (numtoprint == 8):
        devauni = b'\u096E'
        numName = "\neight"
    elif (numtoprint == 9):
        devauni = b'\u096F'
        numName = "\nnine"
    #print(devauni, numName)
    return (devauni, numName)

#will print the number in the terminal
#dont know where we have to print it on the display
