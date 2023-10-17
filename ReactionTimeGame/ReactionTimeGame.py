#Matthew Schimmel
#This code was written in September of 2023 for Project 1 of IDEA310L class.
from machine import Pin
from machine import Timer

import time
import random
random.seed();

min_period = 1000 #minimum time before blink, in milliseconds
max_period = 10000 #maximum time before blink, in milliseconds

#lights
main_led = Pin(0, Pin.OUT)
player1 = Pin(1, Pin.OUT)
player2 = Pin(2, Pin.OUT)

#buttons
button1 = Pin(11, Pin.IN, Pin.PULL_UP)#player one's
button2 = Pin(12, Pin.IN, Pin.PULL_UP)#player two's

p1Score = 0
p2Score = 0

def blink(pin = main_led, iterations = 1, speed = 0.3):
    for i in range(iterations):
        pin.toggle()
        time.sleep(speed)
        pin.toggle()
        time.sleep(speed)
        
def flash_on(p = main_led):
    p.on()
    main_time = Timer(period = min_period, mode = Timer.ONE_SHOT, callback = flash_off)#recursive call to sustain forever
    
def flash_off(p = main_led):
    p.off()
    randTime = random.randrange(min_period, max_period)
    main_time = Timer(period = randTime, mode = Timer.ONE_SHOT, callback = flash_on)#recursive call to sustain forever
    
def checkButtons(button1, button2): #Waits and returns which int respective of which button gets pressed
    while(True):
        if button1.value() == 1:
            main_led.off()
            return 1
        elif button2.value() == 1:
            main_led.off()
            return 2
    #return random.randrange(1,3) # Dormat line from when the hardware didn't work.
            
def flashScore(): #displays score on the lights and on the terminal
    print("Player 1 Score:")
    print(p1Score)
    blink(player1, p1Score)
    time.sleep(0.5)
    print("Player 2 Score:")
    print(p2Score)
    blink(player2, p2Score)
    print("")
    
def checkForWinner(p1Score, p2Score): #checks if one of the players has won
    if p1Score is 5 or p2Score is 5:
        print("Winner!")
        return True


# -- Main Method Begins Here -- #
#Resets any buttons left toggled on from last run
main_led.off()
player1.off()
player2.off()

while (True):
    #lights Main LED at random interval
    time.sleep(random.randrange(1, 5))
    main_led.on()
    
    if checkButtons(button1, button2) == 1:
        p1Score += 1
    else:
        p2Score += 1
        
    flashScore()
    if checkForWinner(p1Score, p2Score):
        p1Score = 0
        p2Score = 0
        
    continue