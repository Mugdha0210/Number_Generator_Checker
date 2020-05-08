import pyttsx3
import random
from . import convtodeva as deva
#When user runs the prog, this func should be called
#Also should be called every time a new number is to be drawn

def obtainNumber():
    numberToWrite = random.randint(0,9)
    engine = pyttsx3.init()

    if numberToWrite == 0:
        engine.say("Draw Zero")
        engine.runAndWait()
    elif numberToWrite == 1:
        engine.say("Draw One")
        engine.runAndWait()
    elif numberToWrite == 2:
        engine.say("Draw Two")
        engine.runAndWait()
    elif numberToWrite == 3:
        engine.say("Draw Three")
        engine.runAndWait()
    elif numberToWrite == 4:
        engine.say("Draw Four")
        engine.runAndWait()
    elif numberToWrite == 5:
        engine.say("Draw Five")
        engine.runAndWait()
    elif numberToWrite == 6:
        engine.say("Draw Six")
        engine.runAndWait()
    elif numberToWrite == 7:
        engine.say("Draw Seven")
        engine.runAndWait()
    elif numberToWrite == 8:
        engine.say("Draw Eight")
        engine.runAndWait()
    elif numberToWrite == 9:
        engine.say("Draw Nine")
        engine.runAndWait()

    return numberToWrite

#number that is to be drawn is now stored and audio work is done

#So, what number is to be drawn is generated at random and the student is asked to draw
#Number to be drawn
#Submit clicked by the user
#OnSubmit event to be triggered
#Accuracy checked by Mugdhas method
#mag he pudcha function call karaycha

#number to be drawn and accuracy of resultant drawing to be passed as parameters
def accuracyTeller(accuracy, probability):
    if accuracy == 1 :
        #Call function to Display Number-Name
        #Call function to Display in devanagri
    else :
        #pass
        #set devuni = None
        #NumberName = None
    #return [probability, devuni, NumberName]
    
    
    #if (accuracy >= 50 ): #50 is dummy value, we can change it later
     #   return 1
    #else:
     #   return 0

# if 1 is returned, then valid drawing. So will print spelling (and Devanagari writing)? on the main screen
# if 0 is returned, then drawing is invalid. So will print Wrong Drawing on the screen. Then will give a new number?
