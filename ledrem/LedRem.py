###################################
# LED Remote by Luca Cassioli 2008
###################################

# This program allows using any cellphone supporting stereo outout and
# python programming to be used like a remote control to control devices like
# TV sets, DVD recorder and any infrared remote controllable device.
# Task is accomplished by playing a proper WAV file which replicates signals
# of the original remote control.

# WAV file properties:
# -frequency among 36000 and 38000 Hz
# -"code" made up of carrier present / not present
# -sampling frequency and bits per sample should not affect performance (to be tested).

# WAV file can be created by hand starting from a 36000 Hz tone as wide as the remote
# signal and silencing it in needed parts.

# A suite of programs which automate the process in Windows environment is available:
# RAW2LIRC : turns the sampled remote control signal into LIRC raw format;
# LIRC2LEDREM: creates some DOS batch files from a LIRC raw file;
# each batch file creates a WAV file corresponding to the sampled command. 


from music import *
from appuifw import *
from graphics import *
from key_codes import *
import e32
import sysinfo

import keycapture
from e32 import ao_sleep,Ao_lock
import appswitch
import audio
import appuifw


def cb_capture(key):
    global img
    if key==keycapture.EKey0:
          SoundFile = audio.Sound.open("c:\\nokia\\sounds\\sky000_.wav")
          SoundFile.play()
          e32.ao_sleep(0.5)
          SoundFile.close()
          img.text((10,20),unicode("Tatsto1"))
          canv.blit(img)          
          return
    if key==keycapture.EKey1:
          SoundFile = audio.Sound.open("c:\\nokia\\sounds\\sky001_.wav")
          SoundFile.play()
          e32.ao_sleep(0.5)
          SoundFile.close()
          #img.text((10,20),unicode("Tatsto2"))
          canv.blit(img)          
          return
    if key==keycapture.EKey2:
          SoundFile = audio.Sound.open("c:\\nokia\\sounds\\sky002_.wav")
          SoundFile.play()
          e32.ao_sleep(0.5)
          SoundFile.close()
          #img.text((10,20),unicode("Tatsto2"))
          canv.blit(img)          
          return
    if key==keycapture.EKey3:
          return

def quit():
    app.exit_key_handler = None
    script_lock.signal()
    capturer.stop()
    print "TERMINATO."
    print
              
def inizio():
    global img
    img=Image.open("C:\\nokia\\images\\tasti2.JPG")
    canv.blit(img)
    
script_lock = Ao_lock()
app.exit_key_handler = quit
appuifw.app.body=canv=appuifw.Canvas()
appuifw.app.screen='full'
capturer=keycapture.KeyCapturer(cb_capture)
capturer.forwarding=0
capturer.keys=(
               keycapture.EKey0,
               keycapture.EKey1,
               keycapture.EKey2,
               keycapture.EKey3,
               keycapture.EKey4,
               keycapture.EKey5,
               keycapture.EKey6,
               keycapture.EKey7,
               keycapture.EKey8,
               keycapture.EKey9,
               keycapture.EKeyYes,
               keycapture.EKeyNo,
               keycapture.EKeySelect,
               keycapture.EKeyEdit,
               keycapture.EKeyStar,
               keycapture.EKeyHash
               )
capturer.start()
inizio()
script_lock.wait()
