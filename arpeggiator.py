import time
import rtmidi
import sys

#Create a MIDI out objext and open the port you want to use with it
moogsend = rtmidi.MidiOut()
moogsend.open_port(3)

# MIDI protocol for note on and off
note_on = 0x90
note_off = 0x80

# A function that plays the note at a velocity and rhythm set by the user
def playnote(note, velocity, rhythm):
    moogsend.send_message([note_on, note, velocity])
    time.sleep(rhythm)
    moogsend.send_message([note_off, note, velocity])

#In the try section of the loop you can create any pattern that you want between MIDI notes 1-127
while True:
    try:
        for i in range(8):
            if (i % 2) == 0:
                x = i*-7
            elif (i % 2) == 1:
                x = -24
            playnote(x + 53, 127, (i / 300)*4)
        continue
    except KeyboardInterrupt:
        moogsend.close_port()
        sys.exit()
