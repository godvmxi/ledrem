# SMS Recorder by Luca Cassioli 2008
#
# Program allows controlling Psiloc IR Remote application in such a way
# that upon receiving properly formatted SMS, proper remote-control
# commands are emulated by the phone to start recording on a 
# VCR/DVD Recorder

import e32
import appswitch
import messaging
import os
import appuifw
import key_codes
import keypress


'APPLICATION_NAME = u'Phone'
APPLICATION_NAME = u'Psiloc Total IR Remote'
CONFIGURATION_FILE = u'SMSRecLC.ini'




#def read_sms(id): #DEBUG
def read_sms():
    ##############################à
    sms_text="#REC#START" # DEBUG*********
    ##############################à
    e32.ao_sleep(0.1)
    #i=inbox.Inbox() #DEBUG
    #sms_text=i.content(id) #DEBUG
    appuifw.note(u"Messaggio da elaborare: " + sms_text, "info")

    # Execute different actions depending on SMS contents:
    if sms_text[0:5] == '#REC#':
      print 'Message received'
      if appswitch.switch_to_fg(APPLICATION_NAME) == 1:
        e32.ao_sleep(1)
        keypress.simulate_key(53,53)
        keypress.simulate_key(54,54)
        keypress.simulate_key(55,55)
        keypress.simulate_key(63495,63495)
        keypress.simulate_key(63495,63495)
        keypress.simulate_key(52,52)
      else:
        print "ERROR: Couldnt bring " + APPLICATION_NAME + " to foreground."  
      #i.delete(id) # Delete just received message DEBUG
      #SendMess(Recipient_number,'#REC# Message received!')


def ReadSettings():
    global Recipient_number
    global FILEPATH
    try:
        f=open(FILEPATH,'rt')  # Open for reading
        print "file aperto"
        try:
            content = f.read()
            print "contenuto letto"
            parameters=eval(content) # Store values
            print "valori presi"
            f.close()
            Recipient_number = parameters.get('recipient','')  # read values
            #print Recipient_number
        except:
            print 'Couldnt read file - err 001'
    except:
        print 'Couldnt open file - err 002'
        
apps = appswitch.application_list(False) # Get list of all running applications

RemoteFound = False
for app in apps:
    if app == APPLICATION_NAME:
      RemoteFound = True    
if RemoteFound == False:
  print 'Error: no suitable application found ( ' + APPLICATION_NAME + ')'
  print 'List of running applications:'
  print appswitch.application_list(False)

print 'connecting to inbox...'
read_sms()
#i=inbox.Inbox()  #DEBUG
# Connect messages receiving to program:   
#i.bind(read_sms) #DEBUG
print 'Connected. Waiting for incoming messages...'        
