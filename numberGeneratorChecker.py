from playsound import playsound
import random
import convtodeva as deva
import time
#When user runs the prog, this func should be called
#Also should be called every time a new number is to be drawn


def obtainNumber():
    numberToWrite = random.randint(0,9)


    if numberToWrite == 0:
        playsound('./zero.mp3')
        time.sleep(1)
        playsound('./zero.mp3')
    elif numberToWrite == 1:
        playsound('./one.mp3')
        time.sleep(1)
        playsound('./one.mp3')
    elif numberToWrite == 2:
        playsound('./two.mp3')
        time.sleep(1)
        playsound('./two.mp3')
    elif numberToWrite == 3:
        playsound('./three.mp3')
        time.sleep(1)
        playsound('./three.mp3')
    elif numberToWrite == 4:
        playsound('./four.mp3')
        time.sleep(1)
        playsound('./four.mp3')
    elif numberToWrite == 5:
        playsound('./five.mp3')
        time.sleep(1)
        playsound('./five.mp3')
    elif numberToWrite == 6:
        playsound('./six.mp3')
        time.sleep(1)
        playsound('./six.mp3')
    elif numberToWrite == 7:
        playsound('./seven.mp3')
        time.sleep(1)
        playsound('./seven.mp3')
    elif numberToWrite == 8:
        playsound('./eight.mp3')
        time.sleep(1)
        playsound('./eight.mp3')
    elif numberToWrite == 9:
        playsound('./nine.mp3')
        time.sleep(1)
        playsound('./nine.mp3')

    return numberToWrite

#number that is to be drawn is now stored and audio work is done

#So, what number is to be drawn is generated at random and the student is asked to draw
#Number to be drawn
#Submit clicked by the user
#OnSubmit event to be triggered
#Accuracy checked by Mugdhas method
#mag he pudcha function call karaycha

def tryagain():
    playsound('./tryagain.mp3')

#number to be drawn and accuracy of resultant drawing to be passed as parameters
def accuracyTeller(accuracy, probability):
    if accuracy == 1 :
        pass
        #Call function to Display Number-Name
        #Call function to Display in devanagri
    else :
        pass
        #set devuni = None
        #NumberName = None
    #return [probability, devuni, NumberName]

if __name__ == '__main__':
    num = obtainNumber()
    print(num)
    #if (accuracy >= 50 ): #50 is dummy value, we can change it later
     #   return 1
    #else:
     #   return 0

# if 1 is returned, then valid drawing. So will print spelling (and Devanagari writing)? on the main screen
# if 0 is returned, then drawing is invalid. So will print Wrong Drawing on the screen. Then will give a new number?
