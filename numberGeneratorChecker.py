from pygame import mixer
import random
import convtodeva as deva
import time
#When user runs the prog, this func should be called
#Also should be called every time a new number is to be drawn

def obtainNumber():
    numberToWrite = random.randint(0,9)

    mixer.init()


    if numberToWrite == 0:
        mixer.music.load("./zero.mp3")
        mixer.music.play
        time.sleep(1)
        mixer.music.load("./zero.mp3")
        mixer.music.play
    elif numberToWrite == 1:
        mixer.music.load("./one.mp3")
        mixer.music.play
        time.sleep(1)
        mixer.music.load("./one.mp3")
        mixer.music.play
    elif numberToWrite == 2:
        mixer.music.load("./two.mp3")
        mixer.music.play
        time.sleep(1)
        mixer.music.load("./two.mp3")
        mixer.music.play
    elif numberToWrite == 3:
        mixer.music.load("./three.mp3")
        mixer.music.play
        time.sleep(1)
        mixer.music.load("./three.mp3")
        mixer.music.play
    elif numberToWrite == 4:
        mixer.music.load("./four.mp3")
        mixer.music.play
        time.sleep(1)
        mixer.music.load("./four.mp3")
        mixer.music.play
    elif numberToWrite == 5:
        mixer.music.load("./five.mp3")
        mixer.music.play
        time.sleep(1)
        mixer.music.load("./five.mp3")
        mixer.music.play
    elif numberToWrite == 6:
        mixer.music.load("./six.mp3")
        mixer.music.play
        time.sleep(1)
        mixer.music.load("./six.mp3")
        mixer.music.play
    elif numberToWrite == 7:
        mixer.music.load("./seven.mp3")
        mixer.music.play
        time.sleep(1)
        mixer.music.load("./seven.mp3")
        mixer.music.play
    elif numberToWrite == 8:
        mixer.music.load("./eight.mp3")
        mixer.music.play
        time.sleep(1)
        mixer.music.load("./eight.mp3")
        mixer.music.play
    elif numberToWrite == 9:
        mixer.music.load("./nine.mp3")
        mixer.music.play
        time.sleep(1)
        mixer.music.load("./nine.mp3")
        mixer.music.play

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
