#A program to translate and transmit strings to Morse code
#over the Raspberry pi GPIO. It uses BCM 17 and 22. That
#way you can use a buzzer and LED at the same time. Don't
#forget the resistor on your LED!

import RPi.GPIO as GPIO
from time import sleep

morse = {
    'a': 'dot-dash',
    'b': 'dash-dot-dot-dot',
    'c': 'dash-dot-dash-dot',
    'd': 'dash-dot-dot',
    'e': 'dot',
    'f': 'dot-dot-dash-dot',
    'g': 'dash-dash-dot',
    'h': 'dot-dot-dot-dot',
    'i': 'dot-dot',
    'j': 'dot-dash-dash-dash',
    'k': 'dash-dot-dash',
    'l': 'dot-dash-dot-dot',
    'm': 'dash-dash',
    'n': 'dash-dot',
    'o': 'dash-dash-dash',
    'p': 'dot-dash-dash-dot',
    'q': 'dot-dash-dash-dot',
    'r': 'dot-dash-dot',
    's': 'dot-dot-dot',
    't': 'dash',
    'u': 'dot-dot-dash',
    'v': 'dot-dot-dot-dash',
    'w': 'dot-dash-dash',
    'x': 'dash-dot-dot-dash',
    'y': 'dash-dot-dash-dash',
    'z': 'dash-dash-dot-dot',
    '1': 'dot-dash-dash-dash-dash',
    '2': 'dot-dot-dash-dash-dash',
    '3': 'dot-dot-dot-dash-dash',
    '4': 'dot-dot-dot-dot-dash',
    '5': 'dot-dot-dot-dot-dot',
    '6': 'dash-dot-dot-dot-dot',
    '7': 'dash-dash-dot-dot-dot',
    '8': 'dash-dash-dash-dot-dot',
    '9': 'dash-dash-dash-dash-dot',
    '0': 'dash-dash-dash-dash-dash',
    '.': 'dot-dash-dot-dash-dot-dash',
    ',': 'dash-dash-dot-dot-dash-dash',
    '?': 'dot-dot-dash-dash-dot-dot',
    '@': 'dot-dash-dash-dot-dash-dot',
    'start': 'dash-dot-dash-dot-dash',
    'end': 'dot-dot-dot-dash-dot-dash',
    ' ': '_'
}

message = str(raw_input('What is your message? '))

def translate(message):
    #Cleans up the user input message and translates it to morse.
    message_lower = message.lower()
    morse_message = morse['start']+'_______'

    for letter in message_lower:
        if letter in morse:
            morse_message += morse[letter]
            morse_message += '___'
    morse_message += '____'+ morse['end']
    return morse_message

print translate(message)

def broadcast(morse_message):
    #Takes the Morse output from translate() and transmits it
    #over the GPIO pins on a Raspberry Pi.
    broadcast_message = ''
    single_chars_to_broadcast = ['a', 'o', '_']
    pins = [17,22]
    dot = 0.15
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pins, GPIO.OUT)

    for letter in morse_message:
        if letter in single_chars_to_broadcast:
            broadcast_message += letter

    for char in broadcast_message:
        if char == 'a':
            GPIO.output(pins,True)
            sleep(dot * 3)
            GPIO.output(pins,False)
            sleep(dot)
        elif char == 'o':
            GPIO.output(pins, True)
            sleep(dot)
            GPIO.output(pins, False)
            sleep(dot)
        elif char == '_':
            sleep(dot)
        else:
            print 'Something went wrong.'
            break

    GPIO.cleanup()
    return broadcast_message


broadcast(translate(message))