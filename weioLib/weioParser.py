###
#
# WEIO Web Of Things Platform
# Copyright (C) 2013 Nodesign.net, Uros PETREVSKI, Drasko DRASKOVIC
# All rights reserved
#
#               ##      ## ######## ####  #######
#               ##  ##  ## ##        ##  ##     ##
#               ##  ##  ## ##        ##  ##     ##
#               ##  ##  ## ######    ##  ##     ##
#               ##  ##  ## ##        ##  ##     ##
#               ##  ##  ## ##        ##  ##     ##
#                ###  ###  ######## ####  #######
#
#                    Web Of Things Platform
#
# This file is part of WEIO
# WEIO is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# WEIO is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors :
# Uros PETREVSKI <uros@nodesign.net>
# Drasko DRASKOVIC <drasko.draskovic@gmail.com>
#
###

from weioLib.weioIO import *
from weioLib import weioRunnerGlobals
import platform, sys

# WeIO API bindings from websocket to lower levels
# Each data argument is array of data
# Return value is dictionary
def callPinMode(data) :
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        pinMode(data[0],data[1])
    else :
        print "pinMode ON PC", data
    return None

def callPortMode(data) :
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        portMode(data[0],data[1])
    else :
        print "pinMode ON PC", data
    return None

def callDigitalWrite(data) :
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        digitalWrite(data[0], data[1])
    else :
        print "digitalWrite ON PC", data
    return None

def callDigitalRead(data) :
    bck = {}
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        value = digitalRead(data[0])
        bck["data"] = value
        bck["pin"] = data[0]
    else :
        print "digitalRead ON PC", data
        bck["data"] = 1 # faked value
        bck["pin"] = data[0] # pin
    return bck

def callPortWrite(data) :
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        portWrite(data[0], data[1])
    else :
        print "portWrite ON PC", data
    return None

def callPortRead(data) :
    bck = {}
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        value = portRead(data[0])
        bck["data"] = value
        bck["port"] = data[0]
    else :
        print "digitalRead ON PC", data
        bck["data"] = 1 # faked value
        bck["port"] = data[0] # pin
    return bck

def callDHTRead(data) :
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        dhtRead(data[0])
    else :
        print "dhtRead ON PC", data
    return None

def callAnalogRead(data) :
    bck = {}
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        #print "From browser ", data
        value = analogRead(data[0]) # this is pin number
        bck["data"] = value
        bck["pin"] = data[0]
    else :
        print "analogRead ON PC", data
        bck["data"] = 1023 # faked value
        bck["pin"] = data[0]
    return bck

def callSetPwmPeriod(data) :
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        setPwmPeriod(data[0],data[1])
    else:
        print "setPwmPeriod ON PC", data
    return None

# def callSetPwmLimit(data) :
#     if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
#         setPwmLimit(data[0])
#     else:
#         print "setPwmLimit ON PC", data
#     return None

def callPwmWrite(data) :
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        pwmWrite(data[0], data[1])
    else :
        print "pwmWrite ON PC", data
    return None

def callProportion(data) :
    bck = {}
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        #print "From browser ", data
        value = proportion(data[0],data[1],data[2],data[3],data[4])
        bck["data"] = value
    else :
        print "proportion ON PC", data
        bck["data"] = data
    return bck

def callAttachInterrupt(data) :
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        attachInterrupt(data[0], data[1])
    else:
        print "attachInterrupt ON PC", data
    return None

def callDetachInterrupt(data) :
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        detachInterrupt(data[0])
    else:
        print "detachInterrupt ON PC", data
    return None

def callDelay(data) :
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        delay(data[0])
    else :
        print "delay ON PC", data
    return None

def callTone(data) :
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        print "TONE VALS", len(data)
        if (len(data)==2):
            tone(data[0], data[1])
        elif (len(data)==3):
            tone(data[0], data[1], data[2])
    else :
        print "tone ON PC", data
    return None

def callNotone(data) :
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        noTone(data[0])
    else :
        print "notone ON PC", data
    return None

def callConstrain(data) :
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        constrain(data[0], data[1], data[2],)
        bck["data"] = value
    else :
        print "contrain ON PC", data
        bck["data"] = 1 # faked value
        bck["pin"] = data[0] # pin
    return bck


def callMillis(data) :
    bck = {}
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        value = millis() 
        bck["data"] = value
    else :
        print "millis ON PC", data
        bck["data"] = 0 # faked value
    return bck

def callGetTemperature(data):
    bck = {}
    if (weioRunnerGlobals.WEIO_SERIAL_LINKED is True):
        value = getTemperature()
        bck["data"] = value
    else :
        print "getTemperature ON PC", data
        bck["data"] = 0 # faked value
    return bck

def genericInterrupt(data):
    #type = data["type"]
    #data = {}
    #data["requested"] = 'analogRead'
    #data["data"] = value
    #self.write_message(json.dumps(data))
    pass

def callUserMesage(data):
    print "USER TALKS", data
    #weioRunnerGlobals.userMain

def pinsInfo(data) :
    bck = {}
    bck["data"] = weioRunnerGlobals.DECLARED_PINS
    #print("GET PIN INFO ASKED!", bck["data"])
    return bck

def callListSerials(data):
    bck = {}
    bck["data"] = listSerials()
    return bck

# UART SECTION
clientSerial = None
def callInitSerial(data):
    global clientSerial
    if (clientSerial is None) :
        clientSerial = initSerial(data[0], data[1])

def callSerialWrite(data):
    global clientSerial
    if not(clientSerial is None) :
        clientSerial.write(data)
    else :
        sys.stderr.write("Serial port is not initialized. Use initSerial function first")

def callSerialRead(data):
    global clientSerial
    bck = {}
    if not(clientSerial is None) :
        bck["data"] = clientSerial.read()
    else :
        sys.stderr.write("Serial port is not initialized. Use initSerial function first")
    return bck
    
# SPI SECTION
SPI = None
def callInitSPI(data):
    global SPI
    if (SPI is None) :
        SPI = initSPI(data[0])

def callWriteSPI(data):
    global SPI
    if not(SPI is None) :
        SPI.write(data[0])
    else :
        sys.stderr.write("SPI port is not initialized. Use initSerial function first")

def callReadSPI(data):
    global SPI
    bck = {}
    if not(SPI is None) :
        bck["data"] = SPI.read(data[0])
    else :
        sys.stderr.write("SPI port is not initialized. Use initSerial function first")
    return bck
        
###
# WeIO native spells
###
weioSpells = {
    "digitalWrite":callDigitalWrite,
    "digitalRead":callDigitalRead,
    "portWrite":callPortWrite,
    "portRead":callPortRead,
    "dhtRead":callDHTRead,
    "analogRead":callAnalogRead,
    "pinMode":callPinMode,
    "portMode":callPortMode,
    "setPwmPeriod":callSetPwmPeriod,
    "pwmWrite":callPwmWrite,
    "proportion":callProportion,
    "attachInterrupt":callAttachInterrupt,
    "detachInterrupt":callDetachInterrupt,
    "tone": callTone,
    "noTone": callNotone,
    "constrain":callConstrain,
    "millis":callMillis,
    "getTemperature": callGetTemperature,
    "delay":callDelay,
    "pinsInfo": pinsInfo,
    "listSerials": callListSerials,
    "initSerial": callInitSerial,
    "serialWrite": callSerialWrite,
    "initSPI": callInitSPI,
    "readSPI": callReadSPI,
    "writeSPI": callWriteSPI
  # "message":callUserMesage
}

###
# User added spells (handlers)
###
weioUserSpells = {}

def addUserEvent(event, handler):
    global weioUserSpells
    #print "Adding event ", event
    #print "and handler ", handler
    weioUserSpells[event] = handler

def removeUserEvents():
    global weioUserSpells
    weioUserSpells.clear()

